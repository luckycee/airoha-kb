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
    for p in sorted(TICKETS_DIR.glob("ABT-*.md")):
        t = read_frontmatter(p)
        if t["id"]:
            tickets.append(t)

    # 列表页（表格，按工单号排序）
    lines = ["# 工单列表", "",
             f"共 {len(tickets)} 条工单（MIUIX1565-15 ~ MIUIX1565-{tickets[-1]['id'].split('-')[-1] if tickets else '?'}）。",
             "",
             "| 工单号 | 主题 | 日期 | 状态 |",
             "|---|---|---|---|"]
    for t in tickets:
        title = t["title"].replace("|", "｜")
        lines.append(f"| [{t['id']}]({t['id']}.md) | {title} | {t['date']} | {t['status']} |")
    LIST_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 首页统计信息
    index = INDEX_FILE.read_text(encoding="utf-8")
    index = re.sub(r"- \*\*工单数量\*\*：[^\n]*", f"- **工单数量**：{len(tickets)} 条", index)
    INDEX_FILE.write_text(index, encoding="utf-8")
    print(f"[成功] 列表页已更新：{len(tickets)} 条工单")


if __name__ == "__main__":
    build()
