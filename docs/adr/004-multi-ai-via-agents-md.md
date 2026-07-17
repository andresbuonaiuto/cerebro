# ADR 004 — Multi-AI support via AGENTS.md and a Custom GPT prompt

- **Status:** accepted
- **Date:** 2026-07-17

## Context

The pattern should not be Claude-only. Other agents (Codex, Cursor, Gemini CLI)
read an `AGENTS.md` convention; ChatGPT users work through Custom GPTs or
Projects rather than installable skills.

## Options considered

- **Claude-only** — simplest, but abandons a large audience.
- **AGENTS.md + Custom GPT prompt** — cover CLI agents via the de-facto
  `AGENTS.md` standard, and ChatGPT via a pasteable Custom GPT instruction set.

## Decision

Each brain carries a copy of the blueprint as `AGENTS.md`. Ship a
`templates/custom-gpt-prompt.md` for ChatGPT users.

## Consequences

- One method, three delivery surfaces.
- ChatGPT web (no filesystem) is limited to *querying* a pasted/uploaded brain,
  not *maintaining* it. Accepted; maintenance needs a real filesystem agent.
