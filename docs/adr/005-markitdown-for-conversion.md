# ADR 005: Use markitdown for PDF→markdown conversion

- **Status:** accepted
- **Date:** 2026-07-17

## Context

Reading raw PDFs costs 5-10x the tokens of reading clean markdown, and many
agents read PDFs poorly. Sources should be converted once, then read as markdown.

## Options considered

- **markitdown** (Microsoft): simple CLI, maintained, covers PDF/docx/pptx/xlsx/
  html/epub. Weak on scanned PDFs.
- **docling** (IBM): stronger layout/table/OCR handling, heavier dependency.
- **pandoc**: universal, but poor at PDF specifically.

## Decision

markitdown as the default, wrapped by `tools/convert.py`. Document docling as the
fallback for scanned or layout-heavy PDFs.

## Consequences

- One-command conversion for the common case.
- Requires Python. Scanned PDFs may need docling; documented in the blueprint.
- Conversion is optional: the blueprint still works reading a PDF directly, just
  at higher token cost.
