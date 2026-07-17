#!/usr/bin/env bash
# Package the Claude skill into dist/cerebro-skill.zip.
# The zip must be self-contained: SKILL.md + an in-sync copy of BLUEPRINT.md.
# Uses Python's zipfile (already a project dependency) so it works on any OS.
set -euo pipefail
cd "$(dirname "$0")/.." || exit 2

if [ ! -f skill/SKILL.md ]; then
  echo "skill/SKILL.md not found (phase 2 not done yet)"; exit 1
fi

# Ensure the skill ships the current blueprint.
if [ -f BLUEPRINT.md ]; then
  cp BLUEPRINT.md skill/BLUEPRINT.md
fi

mkdir -p dist
python scripts/zip_skill.py
