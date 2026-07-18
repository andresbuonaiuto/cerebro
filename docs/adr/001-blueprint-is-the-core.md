# ADR 001: The blueprint is the core, the skill is a wrapper

- **Status:** accepted
- **Date:** 2026-07-17

## Context

The project can be centered on the Claude Skill (vendor-specific) or on a
vendor-neutral document. The value we want to distribute is the *method*, not a
particular tool integration.

## Options considered

- **Skill-first**: everything lives in the Claude Skill. Easiest for Claude
  users, but locks the pattern to one vendor and one format.
- **Blueprint-first**: a normative markdown document (`BLUEPRINT.md`) is the
  product; the skill, `AGENTS.md`, and Custom GPT prompt are thin wrappers that
  point any agent to it.

## Decision

Blueprint-first. `BLUEPRINT.md` is the authoritative spec. Every distribution
surface (Claude Skill, `AGENTS.md`, Custom GPT prompt) references or embeds it.

## Consequences

- The pattern survives any single vendor's format changes.
- One source of truth to maintain; wrappers stay minimal.
- Each brain carries a copy of the blueprint (as `AGENTS.md`), so it is
  self-contained and portable across agents.
