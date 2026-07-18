#!/usr/bin/env bash
# Quality gates for the cerebro repo. Run before every commit.
# Steps grow with the repo: skill/ and tools/ checks activate once those exist.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
fail=0

echo "== 1/4 markdownlint =="
if command -v npx >/dev/null 2>&1; then
  npx --yes markdownlint-cli2 >/dev/null 2>&1 && echo "  markdownlint OK" || { echo "  markdownlint FAILED"; npx --yes markdownlint-cli2; fail=1; }
else
  echo "  SKIP (npx not available)"
fi

echo "== 2/4 internal links =="
python scripts/check_links.py || fail=1

echo "== 3/4 python tooling compiles =="
if [ -d tools ]; then
  python -m compileall -q tools/ && echo "  compile OK" || fail=1
else
  echo "  SKIP (tools/ not present yet)"
fi

echo "== 4/4 blueprint copies in sync =="
if [ -f BLUEPRINT.md ] && [ -f skill/BLUEPRINT.md ]; then
  if diff -q BLUEPRINT.md skill/BLUEPRINT.md >/dev/null; then
    echo "  in sync OK"
  else
    echo "  BLUEPRINT.md and skill/BLUEPRINT.md differ"; fail=1
  fi
else
  echo "  SKIP (blueprint copies not present yet)"
fi

echo
if [ "$fail" -eq 0 ]; then echo "ALL GATES PASSED"; else echo "GATES FAILED"; fi
exit "$fail"
