# export_tiddlers.py
from bs4 import BeautifulSoup
import re
from pathlib import Path

html_file = Path("data/example mgsd.htm")   # ← CHANGE to your exact filename
out_dir = Path("data/tiddlers")
out_dir.mkdir(exist_ok=True)

html = html_file.read_text(encoding="utf-8", errors="ignore")

soup = BeautifulSoup(html, "html.parser")

# Classic TiddlyWiki storeArea (most common for mGSD)
store = soup.find("div", id="storeArea")
if not store:
    # Fallback for newer classic or JSON style
    store = soup.find("script", class_="tiddlywiki-tiddler-store")

print("Store area found:", bool(store))

tiddlers = []
if store and store.name == "div":
    tiddlers = store.find_all("div", title=True)   # each tiddler is a <div title="...">
elif store and store.name == "script":
    import json
    data = json.loads(store.string or "[]")
    tiddlers = data if isinstance(data, list) else []

print(f"Found {len(tiddlers)} tiddlers")

for t in tiddlers:
    if isinstance(t, dict):                    # JSON style
        title = t.get("title", "untitled")
        text = t.get("text", "")
        tags = t.get("tags", "")
    else:                                      # Classic <div> style
        title = t.get("title", "untitled")
        text_tag = t.find("pre")
        text = text_tag.get_text() if text_tag else ""
        tags = t.get("tags", "")

    if not title or title.startswith("$:/"):
        continue  # skip system tiddlers

    safe_title = re.sub(r'[\\/:*?"<>|]', "_", title)

    md = f"""---
title: {title}
tags: {tags}
created: {t.get("created", "")}
modified: {t.get("modified", "")}
---

{text}
"""
    (out_dir / f"{safe_title}.md").write_text(md, encoding="utf-8")

print("✅ Export done → data/tiddlers/")