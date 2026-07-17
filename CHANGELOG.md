# Changelog

All notable changes to this project are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added

- Phase 3: `tools/convert.py`, a markitdown wrapper that converts PDF/docx/epub
  sources to markdown so a brain reads the leaner markdown instead of raw PDFs.
  Clear install hint and non-zero exit when markitdown is missing.
  `tools/requirements.txt` pins the dependency.
- Phase 2: portable `skill/SKILL.md` (English, no hardcoded paths) that drives
  the four operations in natural language, deferring to the bundled blueprint.
- `scripts/build-skill.sh` + `scripts/zip_skill.py` package the skill into
  `dist/cerebro-skill.zip` (cross-platform, uses Python's zipfile so no `zip`
  binary is needed on Windows).
- Phase 1: `BLUEPRINT.md`, the normative spec for building and maintaining a
  brain (core principle, page conventions with confidence levels, the four
  operations, contradiction handling, source conversion, scale rules).
- `templates/brain-structure/`, a complete copyable brain skeleton (AGENTS.md
  schema, CLAUDE.md pointer, index.md, log.md, and the folder tree).
- Phase 0 scaffolding: STATUS.md, 8 ADRs, AGENTS.md/CLAUDE.md, MIT license.
- Quality gates (`scripts/check.sh`): markdownlint, internal-link check,
  python compile, blueprint-copy sync. GitHub Actions CI running the same gates.
- `scripts/build-skill.sh` to package the Claude skill (activates in phase 2).
- `.gitattributes` forcing LF on scripts so CI stays green on Linux.
