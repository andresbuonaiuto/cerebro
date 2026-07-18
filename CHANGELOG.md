# Changelog

All notable changes to this project are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added

- Phase 0 scaffolding: STATUS.md, 8 ADRs, AGENTS.md/CLAUDE.md, MIT license.
- Quality gates (`scripts/check.sh`): markdownlint, internal-link check,
  python compile, blueprint-copy sync. GitHub Actions CI running the same gates.
- `scripts/build-skill.sh` to package the Claude skill (activates in phase 2).
- `.gitattributes` forcing LF on scripts so CI stays green on Linux.
