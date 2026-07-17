# ADR 003 — Distribute the Claude integration as an Agent Skill

- **Status:** accepted
- **Date:** 2026-07-17

## Context

Claude supports installable Skills (a `SKILL.md` with YAML frontmatter plus
supporting files, zipped) that work across Claude Desktop, Claude Code, and
claude.ai. We need a distribution format for the Claude integration.

## Options considered

- **Agent Skill** — official, installable via the UI, one artifact for all
  Claude surfaces.
- **Plain prompt / slash command** — no install story, harder to share.
- **MCP server** — powerful but heavy: requires running a server, overkill for a
  markdown-driven workflow.

## Decision

Ship an Agent Skill packaged as `dist/cerebro-skill.zip` via a build script. The
zip is self-contained (includes `BLUEPRINT.md`).

## Consequences

- One-click install for Claude users.
- Tied to Anthropic's skill format; if it changes, only the wrapper is updated
  (the blueprint is unaffected, per ADR 001).
