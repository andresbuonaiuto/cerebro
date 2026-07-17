#!/usr/bin/env bash
# Package the Claude skill into dist/cerebro-skill.zip.
# The zip must be self-contained: SKILL.md + an in-sync copy of BLUEPRINT.md.
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
rm -f dist/cerebro-skill.zip
( cd skill && zip -r -q ../dist/cerebro-skill.zip . -x '*.DS_Store' )
echo "Built dist/cerebro-skill.zip:"
unzip -l dist/cerebro-skill.zip
