# AGENTS.md — cerebro (repo)

Instructions for any AI agent working on **this repository** (the public kit).
Not to be confused with the `AGENTS.md` that ships *inside* each brain (that one
is a copy of `BLUEPRINT.md`).

## Read first, every session

1. [`docs/STATUS.md`](docs/STATUS.md) — the source of truth for progress. Never
   start work without reading it.
2. The master plan lives outside the repo: `X:\Claude DeepSeek\PLAN-CEREBRO.md`.

## What this repo is

An installable kit implementing the LLM Wiki pattern. The core deliverable is
`BLUEPRINT.md` (landing in phase 1); everything else (skill, templates, tooling)
wraps it. See [`docs/adr/`](docs/adr/) for the decisions behind the structure.

## Commands

- Quality gates (run before every commit): `bash scripts/check.sh`
- Build the Claude skill zip: `bash scripts/build-skill.sh` → `dist/cerebro-skill.zip`
- Convert a source: `python tools/convert.py <file.pdf> [-o out.md]`

## Project rules

- **English everywhere in public content, commit messages included** (ADR 006).
  No em dashes (—); use commas or parentheses.
- `skill/BLUEPRINT.md` is a copy of the root `BLUEPRINT.md`. If you edit one,
  sync the other (`scripts/check.sh` verifies they match).
- Never commit private data or source PDFs. Only public-domain sources under
  `examples/` are allowed. The private brains live in `X:\Claude DeepSeek\cerebros`.
- **Sync rule:** the private Spanish skill at `C:\Users\pand\.claude\skills\cerebro`
  is the daily driver. When an improvement is proven there, port it here (and
  vice-versa) in the same phase close.

## Closing rule (definition of done)

A phase/task is not done until, in the same close: the phase checkboxes in
`PLAN-CEREBRO.md` are green, `docs/STATUS.md` and `CHANGELOG.md` are updated, the
vault file `04-proyectos/cerebro.md` is updated, and the commit is pushed with CI
green.

## Model rule

- Normative writing (phases 1 and 4: the blueprint, the example brain) → use the
  most capable model available.
- Scaffolding, templates, scripts (phases 0, 2, 3, 5) → Sonnet or fast Opus is
  enough. Validate with `scripts/check.sh`, never with trust in the model.
