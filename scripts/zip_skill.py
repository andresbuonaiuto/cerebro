#!/usr/bin/env python3
"""Zip the skill/ folder into dist/cerebro-skill.zip, cross-platform.

The zip contents are rooted at the skill folder (SKILL.md at the top level),
which is what Claude expects when installing a skill.
"""
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO / "skill"
OUT = REPO / "dist" / "cerebro-skill.zip"
SKIP = {".DS_Store"}

def main():
    if not (SKILL_DIR / "SKILL.md").exists():
        print("skill/SKILL.md not found")
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        OUT.unlink()
    files = sorted(
        p for p in SKILL_DIR.rglob("*")
        if p.is_file() and p.name not in SKIP
    )
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(SKILL_DIR).as_posix())
    print(f"Built {OUT.relative_to(REPO).as_posix()}:")
    for p in files:
        print(f"  {p.relative_to(SKILL_DIR).as_posix()}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
