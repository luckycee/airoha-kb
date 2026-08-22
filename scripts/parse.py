"""解析 raw/ 目录下的工单 HTML，生成 Markdown 到 docs/tickets/。

用法:
    python scripts/parse.py                    # 解析全部 raw/*.html
    python scripts/parse.py 15 100             # 只解析指定工单
"""
import html as html_mod
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
OUT_DIR = ROOT / "docs" / "tickets"
NAMES_FILE = ROOT / "sensitive_words.txt"  # 敏感词库（不入库，见 .gitignore）

TICKET_PREFIX = "ABT"  # 工单代号（脱敏用途：MIUIX1565 → ABT，展示与文件名使用）

# 系统自动通知账号（回复无人工内容，整条忽略）
AUTHOR_SKIP = re.compile(r"sysadmin|bot|notification|support-team|admin", re.IGNORECASE)
# 自动提醒内容关键词（兜底过滤）
AUTO_REPLY_PATTERN = re.compile(r"gentle reminder|automated|do not reply|noreply", re.IGNORECASE)

NAMES = []          # 人名（长名优先）
NAME_GROUPS = []    # 人名别名组：[[名字...], ...] 同组视为同一人
NAME_TO_GROUP = {}  # 名字 -> 所属组
NAME_MAP = {}       # 组(排序后小写元组) -> [人名N]
CUSTOMER_TERMS = [] # 客户名
PROJECT_TERMS = []  # 项目/代号
TERM_MAP = {}       # 类型 -> {词(小写): 占位符}

# ---------- 通用工具 ----------

def decode_json_string(s: str) -> str:
    """手动解码 JSON 字符串转义（json.loads 对非标准转义过于严格）。"""
    # 注意顺序：先处理 \\ 组合，再处理单个转义
    s = s.replace('\\\\', '\x00')  # 字面反斜杠占位
    s = s.replace('\\"', '"').replace("\\'", "'")
    s = s.replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
    s = s.replace('\\/', '/').replace('\x00', '\\')
    s = s.replace('\xa0', ' ')  # 不换行空格 → 普通空格
    return s


def extract_value(decoded: str, key: str, default=""):
    """从 JSON 文本中提取指定 key 的值（支持字符串/数组/对象，括号匹配）。"""
    m = re.search(r'"%s"\s*:\s*' % re.escape(key), decoded)
    if not m:
        return default
    i = m.end()
    c = decoded[i]
    if c == '"':  # 字符串值（含转义）
        chars = []
        j = i + 1
        while j < len(decoded):
            ch = decoded[j]
            if ch == "\\" and j + 1 < len(decoded):
                chars.append(decoded[j:j+2]); j += 2
            elif ch == '"':
                break
            else:
                chars.append(ch); j += 1
        try:
            return json.loads("".join(chars))
        except Exception:
            return decode_json_string("".join(chars))
    if c in "[{":  # 数组/对象：括号匹配
        stack = [c]
        j = i + 1
        in_str = False
        while j < len(decoded) and stack:
            ch = decoded[j]
            if ch == "\\":
                j += 2; continue
            if ch == '"':
                in_str = not in_str
            elif not in_str:
                if ch in "[{":
                    stack.append(ch)
                elif ch in "]}":
                    stack.pop()
            j += 1
        frag = decoded[i:j]
        try:
            return json.loads(frag)
        except Exception:
            return default
    # 数字/布尔/null
    m2 = re.match(r'(-?\d+(?:\.\d+)?|true|false|null)', decoded[i:])
    return m2.group(1) if m2 else default


def html_to_text(h: str) -> str:
    """HTML 片段 → 纯文本（保留段落/换行）。"""
    if not h:
        return ""
    soup = BeautifulSoup(h, "lxml")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    for p in soup.find_all("p"):
        p.append("\n\n")
    for li in soup.find_all("li"):
        li.append("\n")
    return re.sub(r"\n{3,}", "\n\n", soup.get_text()).strip()


def mask_sensitive(text: str) -> str:
    """脱敏流水线：邮箱 / 电话 / 长数字串 / 人名 / Jira @提及格式。"""
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[邮箱已隐藏]", text)
    text = re.sub(r"\+?886[- ]?\d{3,4}[- ]?\d{3,4}[- ]?\d{2,4}", "[电话已隐藏]", text)
    text = re.sub(r"09\d{2}[- ]?\d{3}[- ]?\d{3}", "[电话已隐藏]", text)
    text = re.sub(r"(?<!\d)\d{12,}(?!\d)", "[序列号已隐藏]", text)
    text = mask_names(text)  # 人名词库
    text = mask_terms(text, CUSTOMER_TERMS, "客户")  # 客户名
    text = mask_terms(text, PROJECT_TERMS, "项目")   # 项目/代号
    text = re.sub(r"\[~([^\]]*)\]", r"@\1", text)  # Jira 提及 [~xxx] → @xxx
    # 工单引用 → 代号 + 交叉链接（.md 相对链接，MkDocs 构建时自动转换为正确 URL）
    text = re.sub(r"MIUIX1565-(\d+)", rf"[{TICKET_PREFIX}-\1]({TICKET_PREFIX}-\1.md)", text)
    return text


def load_names():
    """加载敏感词库。

    文件格式（sensitive_words.txt）：
        # 人名：主名=别名1,别名2，同组视为同一人（同一编号 [人名N]）
        王友巍=Youwei,Youwei Wang
        Fason Wu
        # 客户名（[客户A]、[客户B]...）
        @客户 某某电子科技有限公司
        # 项目/代号（[项目A]、[项目B]...）
        @项目 ABC-Project
    """
    global NAMES, NAME_GROUPS, NAME_TO_GROUP, CUSTOMER_TERMS, PROJECT_TERMS
    NAME_GROUPS, CUSTOMER_TERMS, PROJECT_TERMS = [], [], []
    if NAMES_FILE.exists():
        for line in NAMES_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("@客户"):
                term = line[len("@客户"):].strip()
                if term:
                    CUSTOMER_TERMS.append(term)
            elif line.startswith("@项目"):
                term = line[len("@项目"):].strip()
                if term:
                    PROJECT_TERMS.append(term)
            elif "=" in line:
                main, _, aliases = line.partition("=")
                group = [main.strip()] + [a.strip() for a in aliases.split(",") if a.strip()]
                if group:
                    NAME_GROUPS.append(group)
            else:
                NAME_GROUPS.append([line])
    NAMES = sorted((n for g in NAME_GROUPS for n in g), key=len, reverse=True)
    NAME_TO_GROUP = {n: g for g in NAME_GROUPS for n in g}


def mask_names(text: str) -> str:
    """人名 → [人名N]，同一组别名（同一人）共用同一编号。"""
    for name in NAMES:
        if name in text:
            group = NAME_TO_GROUP.get(name, [name])
            key = tuple(sorted(n.lower() for n in group))
            if key not in NAME_MAP:
                NAME_MAP[key] = f"[人名{len(NAME_MAP) + 1}]"
            text = text.replace(name, NAME_MAP[key])
    return text


def mask_terms(text: str, terms: list, kind: str) -> str:
    """客户/项目词 → [客户A]/[项目A]，按字母编号。"""
    for term in sorted(terms, key=len, reverse=True):
        if term in text:
            key = term.lower()
            if key not in TERM_MAP.setdefault(kind, {}):
                n = len(TERM_MAP[kind]) + 1
                TERM_MAP[kind][key] = f"[{kind}{chr(64 + n) if n <= 26 else n}]"
            text = text.replace(term, TERM_MAP[kind][key])
    return text


def mask_author(author: str, role: str) -> str:
    """回复作者脱敏：名字 → [人名N]；非词库名（如 sysadmin）保留原样。"""
    if not author:
        return role
    a = mask_names(author)
    a = re.sub(r"[()（）]", " ", a)
    a = re.sub(r"\s+", " ", a).strip()
    seen = []
    for p in re.findall(r"\[人名\d+\]", a):
        if p not in seen:
            seen.append(p)
    return " ".join(seen) if seen else a


def clean_wiki(text: str) -> str:
    """清理 Confluence wiki 附件/图片语法 → 附件提示；附件的 http 链接转纯文本。"""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)\|thumbnail!", "[图片附件]", text)
    text = re.sub(r"!([^!|]+?)\|thumbnail!", r"[图片: \1]", text)
    text = re.sub(r"!([^!|]+?)!", r"[图片: \1]", text)
    text = re.sub(r"\[\^([^|\]]+)\]", r"[附件: \1]", text)
    text = re.sub(r"\s+_\([^)]*\)_?", "", text)  # 删除 _(300 kB)_ 残留
    text = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", r"\1", text)  # 一般链接转纯文本
    return text.strip()


def content_text(item: dict) -> str:
    """从 activityStream 元素中提取回复纯文本（rawComment / comment 字段）。"""
    raw = item.get("rawComment")
    if raw:
        return mask_sensitive(clean_wiki(str(raw)))
    html = item.get("comment")
    if html:
        return mask_sensitive(clean_wiki(html_to_text(str(html))))
    return ""


# ---------- 解析单个工单 ----------

def parse_ticket(ticket_id: int) -> dict:
    raw_path = RAW_DIR / f"MIUIX1565-{ticket_id}.html"
    if not raw_path.exists():
        print(f"[跳过] {raw_path.name} 不存在")
        return None
    soup = BeautifulSoup(raw_path.read_text(encoding="utf-8"), "lxml")
    payload_div = soup.find(id="jsonPayload")
    if not payload_div:
        print(f"[失败] MIUIX1565-{ticket_id}: 未找到 jsonPayload")
        return None
    decoded = html_mod.unescape(payload_div.get_text())

    # 主题 / 时间 / 状态（主题也需脱敏：客户名可能出现在标题里）
    summary = mask_sensitive(extract_value(decoded, "summary") or f"MIUIX1565-{ticket_id}")
    friendly_date = extract_value(decoded, "friendlyDate", "未知时间")
    status = extract_value(decoded, "status", "")

    # 描述：优先找 label=Description 的 customfield，否则取第一个 value.html
    description = ""
    cf_match = re.search(r'"label"\s*:\s*"Description"\s*,\s*"value"\s*:\s*\{', decoded)
    if cf_match:
        m = re.search(r'"html"\s*:\s*"', decoded[cf_match.start():])
        if m:
            description = extract_value(decoded[cf_match.start():], "html", "")
    if not description:
        description = extract_value(decoded, "html", "")

    # 回复流
    activity = extract_value(decoded, "activityStream", [])
    comments = []
    for item in activity if isinstance(activity, list) else []:
        if not isinstance(item, dict):
            continue
        itype = item.get("type", "")
        if not itype.endswith("-comment"):  # worker-comment / requester-comment / customer-comment ...
            continue
        author_raw = item.get("author", "")
        if AUTHOR_SKIP.search(author_raw):
            continue  # 系统自动通知（sysadmin 等），忽略
        body = content_text(item)
        if not body or AUTO_REPLY_PATTERN.search(body):
            continue  # 自动提醒内容，忽略
        comments.append({
            "date": item.get("friendlyDate", ""),
            "author": mask_author(author_raw,
                                 "支持工程师" if itype.startswith("worker") else "客户"),
            "body": body,
        })
    comments.reverse()  # 原厂数据最新在前，转为正序（最旧在前，阅读习惯）

    return {
        "id": f"{TICKET_PREFIX}-{ticket_id}",
        "title": summary,
        "date": friendly_date,
        "status": status,
        "source": f"https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-{ticket_id}",
        "description": mask_sensitive(clean_wiki(html_to_text(description))),
        "comments": comments,
    }


def render_markdown(t: dict) -> str:
    """工单 dict → Markdown 文本。"""
    lines = [
        "---",
        f"id: {t['id']}",
        f"title: {t['title']}",
        f"date: {t['date']}",
        f"status: {t['status']}",
        f"source: {t['source']}",
        "---",
        "",
        f"# {t['id']} {t['title']}",
        "",
        f"> 📅 {t['date']}　🔗 [原始工单链接]({t['source']})",
        "",
        "## 问题描述",
        "",
        t["description"] or "（无描述）",
        "",
        "---",
        "",
    ]
    if t["comments"]:
        lines += ["## 回复记录", ""]
        for i, c in enumerate(t["comments"]):
            cls = "odd" if i % 2 == 0 else "even"  # 灰白交替
            lines += [
                f'<div class="reply {cls}" markdown="1">',
                "",
                f"### {c['date']} — {c['author'] or c['role']}",
                "",
                c["body"],
                "",
                "</div>",
                "",
            ]
    return "\n".join(lines)


def main():
    global NAME_MAP, TERM_MAP
    NAME_MAP = {}
    TERM_MAP = {}
    load_names()
    ids = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else None
    if ids is None:
        ids = sorted(int(p.stem.split("-")[-1]) for p in RAW_DIR.glob("MIUIX1565-*.html"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for tid in ids:
        t = parse_ticket(tid)
        if not t:
            continue
        out = OUT_DIR / f"{t['id']}.md"
        out.write_text(render_markdown(t), encoding="utf-8")
        print(f"[成功] {t['id']} → {out.name}（{len(t['comments'])} 条回复）")


if __name__ == "__main__":
    main()
