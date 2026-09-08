#!/usr/bin/env python3
"""Generate README.md from internal/Curriculum.md, dictionary/*.md, and internal/README.template.md.

Usage:
    python3 internal/generate_readme.py          # validate and write README.md
    python3 internal/generate_readme.py --check  # validate only
"""

import re
import sys
from typing import NoReturn
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CURRICULUM = HERE / "Curriculum.md"
TEMPLATE = HERE / "README.template.md"
DICT_DIR = ROOT / "dictionary"
OUTPUT = ROOT / "README.md"
TOC_MARKER = "<!-- TOC -->"
CURRICULUM_MARKER = "<!-- CURRICULUM -->"

SECTION_RE = re.compile(r"^## Section \d+ — .+$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(\./([^)]+)\.md\)")
MAX_DESCRIPTION = 140
MIN_WORDS = 200


def fail(msg) -> NoReturn:
    print(msg, file=sys.stderr)
    sys.exit(1)


def heading_slug(heading):
    return re.sub(r"[^\w -]", "", heading.lower(), flags=re.UNICODE).replace(" ", "-")


def parse_curriculum(text):
    sections = []
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if not line:
            continue
        if line.startswith("## "):
            if not SECTION_RE.match(line):
                fail(
                    f'Curriculum.md:{line_no}: heading must match "## Section N — Title": {line}'
                )
            sections.append((line[3:], []))
            continue
        if line.startswith("- "):
            if not sections:
                fail(f"Curriculum.md:{line_no}: bullet before any section heading")
            term = line[2:]
            if term != term.strip() or re.search(r"[*_`\[]", term):
                fail(
                    f"Curriculum.md:{line_no}: term must be plain trimmed text: {term}"
                )
            sections[-1][1].append(term)
            continue
        fail(
            f"Curriculum.md:{line_no}: only section headings and term bullets are allowed: {line}"
        )
    return sections


def split_entry(term, text):
    if not text.startswith("---\n"):
        fail(f"{term}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{term}: unterminated frontmatter")
    frontmatter = text[4:end]
    body = text[end + 5 :].lstrip("\n")
    match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        fail(f"{term}: frontmatter lacks a description")
    description = match.group(1).strip().strip('"')
    origin_match = re.search(r"^origin:\s*(\S+)$", frontmatter, re.MULTILINE)
    if not origin_match:
        fail(f"{term}: frontmatter lacks an origin (coined or borrowed)")
    origin = origin_match.group(1)
    if origin not in ("coined", "borrowed", "project"):
        fail(f"{term}: origin must be coined, borrowed, or project, not {origin!r}")
    return description, origin, body


def validate_entry(term, description, origin, body, known_terms):
    if origin == "borrowed" and "](http" not in body:
        fail(f"{term}: borrowed terms must attribute their source with a link")
    if len(description) > MAX_DESCRIPTION:
        fail(
            f"{term}: description is {len(description)} characters; limit is {MAX_DESCRIPTION}"
        )
    words = len(body.split())
    if words < MIN_WORDS:
        fail(f"{term}: body is {words} words; minimum is {MIN_WORDS}")
    if "_Usage:_" not in body:
        fail(f"{term}: missing _Usage:_ dialogue")
    seen = set()
    for _, target in LINK_RE.findall(body):
        target = unquote(target)
        if target not in known_terms:
            fail(f"{term}: links to unknown entry {target!r}")
        if target == term:
            fail(f"{term}: links to itself")
        if target in seen:
            fail(
                f"{term}: links {target!r} more than once; link the first occurrence only"
            )
        seen.add(target)


def rewrite_links(body):
    return LINK_RE.sub(
        lambda m: f"[{m.group(1)}](#{heading_slug(unquote(m.group(2)))})", body
    )


def main():
    check_only = "--check" in sys.argv
    template = TEMPLATE.read_text()
    for marker in (TOC_MARKER, CURRICULUM_MARKER):
        if marker not in template:
            fail(f"Template missing {marker}")

    sections = parse_curriculum(CURRICULUM.read_text())
    on_disk = {p.stem for p in DICT_DIR.glob("*.md")}
    seen = set()
    origins = {"coined": [], "project": [], "borrowed": []}
    parts = []
    for heading, terms in sections:
        parts += [f"## {heading}", ""]
        for term in terms:
            if term in seen:
                fail(f'Curriculum.md: duplicate term "{term}"')
            seen.add(term)
            path = DICT_DIR / f"{term}.md"
            if not path.exists():
                fail(f'Curriculum.md references "{term}" but {path} does not exist')
            description, origin, body = split_entry(term, path.read_text())
            validate_entry(term, description, origin, body, on_disk)
            origins[origin].append(term)
            parts += [f"### {term}", "", rewrite_links(body).rstrip(), ""]

    orphans = sorted(on_disk - seen)
    if orphans:
        fail(f"dictionary/ entries not in Curriculum.md: {', '.join(orphans)}")

    if check_only:
        print(f"ok: {len(seen)} entries in {len(sections)} sections")
        return

    toc = "\n\n".join(
        "\n".join(
            ["<details>", f"<summary>{heading}</summary>", ""]
            + [f"- [{t}](#{heading_slug(t)})" for t in terms]
            + ["", "</details>"]
        )
        for heading, terms in sections
    )
    origin_labels = {
        "coined": "Coined here",
        "project": "Project terms — named tools of ours",
        "borrowed": "Borrowed — attributed in the entry",
    }
    toc += "\n\n" + "\n\n".join(
        "\n".join(
            [
                "<details>",
                f"<summary>{origin_labels[origin]} ({len(terms)})</summary>",
                "",
            ]
            + [f"- [{t}](#{heading_slug(t)})" for t in sorted(terms)]
            + ["", "</details>"]
        )
        for origin, terms in origins.items()
        if terms
    )
    banner = (
        "<!--\n"
        "  GENERATED FILE — DO NOT EDIT.\n"
        "  Source: dictionary/*.md, internal/Curriculum.md, internal/README.template.md\n"
        "  Regenerate: make generate\n"
        "-->\n\n"
    )
    block = "\n".join(parts).rstrip() + "\n"
    OUTPUT.write_text(
        banner + template.replace(TOC_MARKER, toc).replace(CURRICULUM_MARKER, block)
    )
    print(f"wrote README.md: {len(seen)} entries in {len(sections)} sections")


if __name__ == "__main__":
    main()
