"""从已抓取的工单中自动收集人名 → sensitive_names.txt（可手工编辑补充）。

格式：主名=别名1,别名2（同组视为同一人，脱敏时共用同一编号 [人名N]）
收集规则：
  - 回复作者：中文名（括号内）、英文全名 + 英文名首词 → 归为同一组
  - Jira 提及 [~name]：@ 前的名字部分 → 独立组
  - 系统账号（sysadmin/bot 等）不收集
"""
import html as html_mod
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse import extract_value, NAMES_FILE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"

SYSTEM_AUTHORS = ("sysadmin", "bot", "notification", "support-team", "admin")
AUTHOR_SKIP = re.compile(r"|".join(SYSTEM_AUTHORS), re.IGNORECASE)
ZH_NAME = re.compile(r"[一-鿿]{2,4}")


def group_from_author(author: str) -> tuple:
    """从 author 字符串提取名字组（主名, 别名列表）。"""
    zh = ZH_NAME.findall(author)
    en = author.split("(")[0].strip()
    words = en.split()
    en_full = en if len(words) >= 2 and all(w[0].isupper() for w in words) else ""
    en_first = words[0] if en_full else ""
    group = []
    if zh:
        group.extend(zh)
    if en_full:
        group.append(en_full)
    if en_first:
        group.append(en_first)
    group = list(dict.fromkeys(group))  # 去重保序
    if not group:
        return None
    return group[0], group[1:]


def collect_from_ticket(path: Path, groups: dict):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    div = soup.find(id="jsonPayload")
    if not div:
        return
    decoded = html_mod.unescape(div.get_text())
    activity = extract_value(decoded, "activityStream", [])
    for item in activity if isinstance(activity, list) else []:
        if not isinstance(item, dict):
            continue
        author = item.get("author", "")
        if not author or AUTHOR_SKIP.search(author):
            continue
        g = group_from_author(author)
        if not g:
            continue
        main, aliases = g
        if main not in groups:
            groups[main] = aliases
        else:
            for a in aliases:
                if a not in groups[main]:
                    groups[main].append(a)
    # Jira 提及 [~name]
    for m in re.finditer(r"\[~([^\]]+)\]", decoded):
        name = m.group(1).split("@")[0].strip()
        if name and not AUTHOR_SKIP.search(name):
            groups.setdefault(name, [])


def normalize(groups: dict) -> dict:
    """合并有关联的组：同名名字出现在多个组时，并为一组。"""
    adj = {}
    for main, aliases in groups.items():
        mem = [main] + aliases
        for m in mem:
            adj.setdefault(m.lower(), set()).update(x.lower() for x in mem)
    visited, result = set(), {}
    for main in groups:
        if main.lower() in visited:
            continue
        queue, comp = [main.lower()], set()
        while queue:
            cur = queue.pop()
            if cur in visited:
                continue
            visited.add(cur)
            comp.add(cur)
            queue.extend(adj.get(cur, set()) - visited)
        orig = [k for k in groups if k.lower() in comp]
        new_main = orig[0]
        names = set()
        for k in orig:
            names.add(k)
            names.update(groups[k])
        result[new_main] = sorted((n for n in names if n != new_main),
                                  key=lambda n: (len(n), n), reverse=True)
    return result


def main():
    groups = {}
    other_lines = []  # 非人名行（@客户/@项目 等），原样保留
    # 读取已有词库（合并，保留手工别名）
    if NAMES_FILE.exists():
        for line in NAMES_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                other_lines.append(line)
            elif line.startswith("@"):
                other_lines.append(line)
            elif "=" in line:
                main, _, aliases = line.partition("=")
                groups[main.strip()] = [a.strip() for a in aliases.split(",") if a.strip()]
            else:
                groups.setdefault(line, [])
    for p in sorted(RAW_DIR.glob("MIUIX1565-*.html")):
        collect_from_ticket(p, groups)
    groups = normalize(groups)
    # 写回
    with NAMES_FILE.open("w", encoding="utf-8") as f:
        f.write("# 敏感词库：\n")
        f.write("#   人名：主名=别名1,别名2（同组视为同一人，替换为 [人名N]）\n")
        f.write("#   客户名：@客户 某某公司（替换为 [客户A]）\n")
        f.write("#   项目/代号：@项目 XXX（替换为 [项目A]）\n")
        f.write("# 可手工补充任意条目。\n")
        for line in other_lines:
            if not line.startswith("# 敏感词库") and line != "# 人名词库：主名=别名1,别名2（同组视为同一人）。可手工补充。":
                f.write(line + "\n")
        for main in sorted(groups, key=str.lower):
            aliases = groups[main]
            f.write(f"{main}=" + ",".join(aliases) + "\n")
    print(f"[成功] 词库已更新：{len(groups)} 个人名组 → {NAMES_FILE.name}")
    for main in sorted(groups, key=str.lower):
        print(f"  - {main}  (别名: {', '.join(groups[main]) if groups[main] else '无'})")


if __name__ == "__main__":
    main()
