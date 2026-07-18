# ADR 008: No npm/npx CLI in v1

- **Status:** accepted
- **Date:** 2026-07-17

## Context

A `npx cerebro init` CLI could scaffold a brain automatically. It also adds a
package to publish, version, and maintain.

## Options considered

- **Ship a CLI in v1**: nicer UX, but more surface area and maintenance before
  the pattern has any traction.
- **No CLI in v1**: the skill and `templates/brain-structure/` cover scaffolding;
  revisit a CLI only if the repo gains users.

## Decision

No CLI in v1. Brain creation happens through the Claude Skill or by copying
`templates/brain-structure/`. A CLI is a candidate for v2.

## Consequences

- Less to build and maintain now.
- Non-Claude users scaffold manually (copy a template folder). Acceptable for v1.
