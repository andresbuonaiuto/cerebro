#!/usr/bin/env python3
"""Check that relative markdown links in the repo resolve to existing files.

Skips external links (http, https, mailto), pure anchors (#...), and Obsidian
[[wikilinks]] (those belong to brains, not this repo). Exits non-zero if any
relative link points to a missing file.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "dist", ".venv", "venv", "node_modules", "__pycache__"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

def iter_md():
    for p in REPO.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(REPO).parts):
            continue
        yield p

def main():
    broken = []
    for md in iter_md():
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0].strip()
            if not path_part:
                continue
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                broken.append(f"{md.relative_to(REPO)} -> {target}")
    if broken:
        print("Broken internal links found:")
        for b in broken:
            print(f"  {b}")
        return 1
    print(f"Link check OK ({sum(1 for _ in iter_md())} markdown files scanned).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
