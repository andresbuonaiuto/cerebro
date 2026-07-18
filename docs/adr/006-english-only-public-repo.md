# ADR 006 — English for all public content, commits included

- **Status:** accepted
- **Date:** 2026-07-17

## Context

The maintainer's default is Spanish (including commit messages). This repo is a
public, portfolio-facing, international project.

## Options considered

- **Spanish** — matches the maintainer's default and the private skill.
- **English** — matches the target audience of a public GitHub tool.

## Decision

Everything public is in English: README, `BLUEPRINT.md`, `STATUS.md`, ADRs,
and commit messages. This is a deliberate exception to the global Spanish-commit
rule. The private daily-use skill stays in Spanish; improvements are ported
between the two.

## Consequences

- Wider reach and credibility for an international audience.
- Two language surfaces to keep in sync (private ES skill ↔ public EN repo);
  a sync rule lives in the repo's `AGENTS.md`.
