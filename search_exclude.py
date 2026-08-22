"""自定义 MkDocs 插件：构建后从搜索索引中移除指定页面。

用法（mkdocs.yml）：
    plugins:
      - search
      - search_exclude:
          pages:
            - tickets/list   # 从搜索索引中排除的页面（URL location 路径）

MkDocs 的插件名约定：模块 search_exclude 中查找类 SearchExcludePlugin。
通过 `python -m mkdocs build` 运行时，项目根目录在 sys.path 中，可直接加载。
"""
import json
from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class SearchExcludePlugin(BasePlugin):
    config_scheme = (
        ("pages", config_options.Type(list, default=[])),
    )

    def on_post_build(self, config, **kwargs):
        pages = self.config.get("pages") or []
        if not pages:
            return
        idx_path = Path(config["site_dir"]) / "search" / "search_index.json"
        if not idx_path.exists():
            return
        data = json.loads(idx_path.read_text(encoding="utf-8"))
        removed = 0
        docs = []
        for d in data.get("docs", []):
            loc = d.get("location", "")
            if any(loc == p or loc.startswith(p + "/") for p in pages):
                removed += 1
                continue
            docs.append(d)
        if removed:
            data["docs"] = docs
            idx_path.write_text(
                json.dumps(data, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )
            print(f"[search_exclude] 从搜索索引移除 {removed} 条（{pages}）")
