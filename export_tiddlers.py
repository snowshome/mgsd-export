# src/export_tiddlers.py
import re
import json
from pathlib import Path

html_file = Path("data/your-wiki.html")      # ← put your .html here
out_dir = Path("data/tiddlers")
out_dir.mkdir(exist_ok=True)

html = html_file.read_text(encoding="utf-8")

# Classic TiddlyWiki extractor
match = re.search(r"var tiddlers = (\[.*?\]);", html, re.DOTALL) or \
        re.search(r"store = (\{.*?\});", html, re.DOTALL)

data = json.loads(match.group(1))
tiddlers = data if isinstance(data, list) else data.get("tiddlers", [])

print(f"Found {len(tiddlers)} tiddlers")

for t in tiddlers:
    title = t.get("title", "untitled").replace("/", "_").replace("\\", "_")
    if not title:
        continue
    
    md = f"""---
title: {title}
tags: {t.get("tags", "")}
type: {t.get("type", "text/vnd.tiddlywiki")}
created: {t.get("created", "")}
modified: {t.get("modified", "")}
fields: {json.dumps(t.get("fields", {}), ensure_ascii=False)}
---

{t.get("text", "")}
"""
    (out_dir / f"{title}.md").write_text(md, encoding="utf-8")

print("✅ Export complete → data/tiddlers/")