#!/usr/bin/env python3
"""Build the interactive dictionary page from internal/page.template.html and the entries.

Usage:
    python3 internal/build_page.py   # writes internal/dictionary_page.html
"""

import json
from pathlib import Path
from urllib.parse import unquote

import generate_readme as g

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "page.template.html"
OUTPUT = HERE / "dictionary_page.html"

sections = []
for heading, terms in g.parse_curriculum(g.CURRICULUM.read_text()):
    number, title = heading.split(" — ", 1)
    entries = []
    for term in terms:
        desc, origin, body = g.split_entry(
            term, (g.DICT_DIR / f"{term}.md").read_text()
        )
        targets = [
            g.heading_slug(unquote(target)) for _, target in g.LINK_RE.findall(body)
        ]
        body = g.rewrite_links(body)
        main, _, usage = body.partition("_Usage:_")
        entries.append(
            {
                "term": term,
                "slug": g.heading_slug(term),
                "desc": desc,
                "origin": origin,
                "body": main.strip(),
                "usage": usage.strip(),
                "links": targets,
            }
        )
    sections.append({"number": number, "title": title, "entries": entries})

payload = json.dumps(sections).replace("</", "<\\/")
html = TEMPLATE.read_text().replace("__DATA__", payload)
OUTPUT.write_text(html)
count = sum(len(s["entries"]) for s in sections)
print(f"wrote {OUTPUT.name}: {count} entries in {len(sections)} sections")
