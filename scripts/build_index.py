"""根据 docs/tickets/*.md 生成工单列表页 docs/tickets/list.md 与首页统计。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKETS_DIR = ROOT / "docs" / "tickets"
LIST_FILE = TICKETS_DIR / "list.md"
INDEX_FILE = ROOT / "docs" / "index.md"


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip()
    # 标题：front matter title 或正文 # 标题
    title = meta.get("title", "")
    return {"id": meta.get("id", path.stem), "title": title,
            "date": meta.get("date", ""), "status": meta.get("status", ""),
            "source": meta.get("source", "")}


def build():
    tickets = []
    # 按工单号数字倒序（最新在前；避免字符串排序出现 100→15→200 的乱序）
    files = sorted(TICKETS_DIR.glob("ABT-*.md"),
                   key=lambda p: int(p.stem.split("-")[-1]), reverse=True)
    for p in files:
        t = read_frontmatter(p)
        if t["id"]:
            tickets.append(t)

    # 列表页（表格，按工单号排序）
    first = tickets[0]["id"] if tickets else "?"
    last = tickets[-1]["id"] if tickets else "?"
    lines = ["# 工单列表", "",
             f"共 {len(tickets)} 条工单（{first} ~ {last}）。",
             "",
             "| 工单号 | 主题 | 日期 | 状态 |",
             "|---|---|---|---|"]
    for t in tickets:
        # 链接文本内：竖线替换为全角；方括号用 Markdown 转义（占位符 [客户A] 等不会被误解为嵌套链接）
        title = t["title"].replace("|", "｜").replace("[", "\\[").replace("]", "\\]")
        link = f"{t['id']}.md"  # MkDocs 构建时自动转换为正确 URL
        lines.append(f"| [{t['id']}]({link}) | [{title}]({link}) | {t['date']} | {t['status']} |")
    LIST_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 首页统计信息
    index = INDEX_FILE.read_text(encoding="utf-8")
    index = re.sub(r"- \*\*工单数量\*\*：[^\n]*", f"- **工单数量**：{len(tickets)} 条", index)
    INDEX_FILE.write_text(index, encoding="utf-8")
    print(f"[成功] 列表页已更新：{len(tickets)} 条工单")


if __name__ == "__main__":
    build()
