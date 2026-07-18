# STATUS: cerebro

> **READ THIS FIRST AT THE START OF EVERY SESSION.**
> This file is the single source of truth for project progress.
> Master plan: `PLAN-CEREBRO.md`, kept outside the repo (not published) in the maintainer's local `X:\Claude DeepSeek\`.
> Last updated: 2026-07-17

## Phases

| # | Phase | Status | Verified |
|---|---|---|---|
| 0 | Scaffolding | 🟢 done, published | 2026-07-17 |
| 1 | BLUEPRINT.md + structure templates | 🟢 done | 2026-07-17 |
| 2 | Installable Claude Skill | 🟢 local done, 2 manual tests pending | 2026-07-17 |
| 3 | PDF→markdown tooling | 🟢 done | 2026-07-17 |
| 4 | Multi-AI templates + example brain | 🟢 local done, 1 manual test pending | 2026-07-17 |
| 5 | README + launch (v1.0) | 🟢 done, published | 2026-07-18 |

## Phase 0 checklist

- [x] `git log` shows the initial commit; `git remote -v` points to
      github.com/andresbuonaiuto/cerebro
- [x] `bash scripts/check.sh` passes locally (verified 2026-07-17)
- [x] CI is green on GitHub (verified 2026-07-18, run 29656087174)
- [x] `X:\Claude DeepSeek\cerebros\cerebros.md` exists and the personal skill points there
- [x] `docs/STATUS.md` and ≥6 ADRs exist (8 ADRs)

Published 2026-07-18: repo at github.com/andresbuonaiuto/cerebro, `gh` CLI
installed and authenticated, CI green, v1.0.0 released.

## Phase 1 checklist (done 2026-07-17)

- [x] `BLUEPRINT.md` covers CREATE/INGEST/QUERY/LINT with numbered steps, the
      anti-hallucination "no coverage" rule, and the idea-validation format
- [x] `templates/brain-structure/` replicates the structure declared in the
      blueprint exactly (verified by listing)
- [x] `bash scripts/check.sh` green (lint + links)

## Phase 2 checklist (local done 2026-07-17)

- [x] `bash scripts/build-skill.sh` builds `dist/cerebro-skill.zip` containing
      `SKILL.md` + `BLUEPRINT.md` (verified)
- [x] CREATE mechanics verified: copying `templates/brain-structure/` yields a
      complete brain matching the blueprint structure
- [ ] **Manual (Andres):** upload `dist/cerebro-skill.zip` in claude.ai →
      Settings → Capabilities → Skills without errors
- [ ] **Manual (Andres):** in a clean Claude Code session, `/cerebro` creates a
      test brain and the structure matches the blueprint

To rebuild the zip for the upload test: `bash scripts/build-skill.sh`
(output at `dist/cerebro-skill.zip`, gitignored).

## Phase 3 checklist (done 2026-07-17)

- [x] `tools/convert.py` produces readable markdown (verified with markitdown in
      an isolated venv; both a real PDF conversion and the output were checked)
- [x] With markitdown not installed, `convert.py` prints the install hint and
      exits non-zero (verified)
- [>] Headline PDF-vs-md token figures deferred to phase 4: this machine had no
      representative book-sized PDF, so the comparison is done on a real
      public-domain book when the example brain is built.

## Phase 4 checklist (local done 2026-07-17)

- [x] `templates/custom-gpt-prompt.md` for ChatGPT Custom GPTs / Projects
- [x] `examples/business-brain/` has 2 public-domain sources (Wattles 1910,
      Barnum 1880), 10 wiki pages, coherent `index.md` and `log.md`, a
      `## Contradiction` demo, and an idea-validation answer page
- [x] All example `[[wikilinks]]` resolve (verified); example sources are public
      domain (pre-1929, US)
- [x] Token savings handled by `convert.py`'s token readout; README framing in
      phase 5 (no fabricated multiplier)
- [ ] **Manual (Andres):** paste `templates/custom-gpt-prompt.md` into a ChatGPT
      Custom GPT with the example brain uploaded, confirm it cites pages and says
      "no coverage" when out of scope

## Phase 5 checklist

- [x] Polished README: hero image slot, tagline, badges, mermaid flow,
      quickstart (3 options), the four operations, the example brain, source
      conversion, and the Karpathy credit with what this kit adds
- [x] `docs/assets/cover.png` added (cover image supplied by Andres)
- [ ] **Manual (Andres):** run the quickstart cold in under 15 min, following
      only the README
- [x] Pushed to github.com/andresbuonaiuto/cerebro, CI green
- [x] v1.0.0 released: github.com/andresbuonaiuto/cerebro/releases/tag/v1.0.0
- [ ] **Manual (Andres):** publish the launch article (ES + EN)

## Marketing (2026-07-18)

- [x] Project card + case-study page added to andresbuonaiuto.com, ES and EN,
      matching the tokenbreak editorial pattern: `proyectos/cerebro.astro` +
      `en/projects/cerebro.astro`, both `index.astro` files, cover converted to
      `public/images/proyectos/cerebro.webp`. Verified with `npm run build`
      (both pages compile, sitemap regenerates) and a visual check in-browser.
- [x] Draft posts for LinkedIn and Reddit at `docs/assets/linkedin-post.md` and
      `docs/assets/reddit-post.md`.
- [ ] **Manual (Andres):** deploy the personal site (Cloudflare Worker
      `peaceful-pegasi`) and publish the posts.

## Dev environment

- OS: Windows 10, bash via Git Bash / Bash tool.
- Repo root: `X:\Claude DeepSeek\cerebro` (public).
- Personal brains (private, not in this repo): `X:\Claude DeepSeek\cerebros`.
- Personal Claude Skill (Spanish, daily use): `C:\Users\pand\.claude\skills\cerebro`.
- Quality gates: `bash scripts/check.sh` (markdownlint via npx, internal-link check, python compile, skill zip build).
- Requires: Node (for `npx markdownlint-cli2`), Python 3 (for tooling), `zip`.

## Pending, non-code (Andres)

- Install `gh` (`winget install GitHub.cli`) OR create the repo manually at github.com/new named `cerebro`, public.
- Drop the cover image at `docs/assets/cover.png` (wide banner, ~1280x640).
- Then, from `X:\Claude DeepSeek\cerebro`:

  ```bash
  git remote add origin https://github.com/andresbuonaiuto/cerebro.git
  git push -u origin main
  ```

- Confirm the CI action turns green after the push.
- Cut a v1.0.0 release and write the launch article (ES + EN) on
  andresbuonaiuto.com, updating both sitemaps.

## Known issues / notes

- `.claude/settings.local.json` is gitignored (machine-specific permissions).
- All public content and commit messages are in **English** (ADR 006), a deliberate exception to the global Spanish-commit rule.
