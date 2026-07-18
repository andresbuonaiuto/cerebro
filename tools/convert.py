#!/usr/bin/env python3
"""Convert a source document (PDF, docx, pptx, xlsx, epub, html) to markdown.

Reading raw PDFs costs 5-10x the tokens of reading clean markdown, so a brain
converts each source once and reads the markdown. This is a thin wrapper around
markitdown (https://github.com/microsoft/markitdown).

Usage:
    python tools/convert.py sources/book.pdf
    python tools/convert.py sources/book.pdf -o sources/converted/book.md

If -o is omitted, the output goes next to the input with a .md extension.
For scanned or layout-heavy PDFs where markitdown output is poor, use docling
(https://github.com/DS4SD/docling) instead.
"""
import argparse
import sys
from pathlib import Path

INSTALL_HINT = (
    "markitdown is not installed.\n"
    "Install it with:  pip install 'markitdown[all]'\n"
    "Docs: https://github.com/microsoft/markitdown"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("input", help="Path to the source document")
    parser.add_argument("-o", "--output", help="Output .md path (default: input with .md)")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.is_file():
        print(f"Input not found: {src}", file=sys.stderr)
        return 2

    try:
        from markitdown import MarkItDown
    except ImportError:
        print(INSTALL_HINT, file=sys.stderr)
        return 1

    out = Path(args.output) if args.output else src.with_suffix(".md")
    out.parent.mkdir(parents=True, exist_ok=True)

    try:
        result = MarkItDown().convert(str(src))
    except Exception as exc:  # markitdown raises various errors per format
        print(f"Conversion failed: {exc}", file=sys.stderr)
        return 3

    out.write_text(result.text_content, encoding="utf-8")
    chars = len(result.text_content)
    print(f"Wrote {out}  ({chars:,} chars, ~{chars // 4:,} tokens)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
