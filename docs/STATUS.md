# STATUS — cerebro

> **READ THIS FIRST AT THE START OF EVERY SESSION.**
> This file is the single source of truth for project progress.
> Master plan: [`../../PLAN-CEREBRO.md`](../../PLAN-CEREBRO.md) (kept outside the repo, in `X:\Claude DeepSeek\`).
> Last updated: 2026-07-17

## Phases

| # | Phase | Status | Verified |
|---|---|---|---|
| 0 | Scaffolding | 🟢 local done, awaiting GitHub push | 2026-07-17 |
| 1 | BLUEPRINT.md + structure templates | ⬜ | — |
| 2 | Installable Claude Skill | ⬜ | — |
| 3 | PDF→markdown tooling | ⬜ | — |
| 4 | Multi-AI templates + example brain | ⬜ | — |
| 5 | README + launch (v1.0) | ⬜ | — |

## Phase 0 checklist

- [x] `git log` shows the initial commit (`git remote -v` still pending: manual GitHub step)
- [x] `bash scripts/check.sh` passes locally (verified 2026-07-17)
- [ ] First-push CI action is green on GitHub (blocked: needs the manual push below)
- [x] `X:\Claude DeepSeek\cerebros\cerebros.md` exists and the personal skill points there
- [x] `docs/STATUS.md` and ≥6 ADRs exist (8 ADRs)

**Blocker:** `gh` CLI is not installed on this machine. Creating the GitHub repo and the first push are a manual step for Andres (commands in "Pending, non-code" below).

## Dev environment

- OS: Windows 10, bash via Git Bash / Bash tool.
- Repo root: `X:\Claude DeepSeek\cerebro` (public).
- Personal brains (private, not in this repo): `X:\Claude DeepSeek\cerebros`.
- Personal Claude Skill (Spanish, daily use): `C:\Users\pand\.claude\skills\cerebro`.
- Quality gates: `bash scripts/check.sh` (markdownlint via npx, internal-link check, python compile, skill zip build).
- Requires: Node (for `npx markdownlint-cli2`), Python 3 (for tooling), `zip`.

## Pending, non-code (Andres)

- Install `gh` (`winget install GitHub.cli`) OR create the repo manually at github.com/new named `cerebro`, public.
- Then, from `X:\Claude DeepSeek\cerebro`:

  ```bash
  git remote add origin https://github.com/<user>/cerebro.git
  git push -u origin main
  ```

- Confirm the CI action turns green after the push.

## Known issues / notes

- `.claude/settings.local.json` is gitignored (machine-specific permissions).
- All public content and commit messages are in **English** (ADR 006), a deliberate exception to the global Spanish-commit rule.
