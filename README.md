# cerebro

Build **persistent knowledge bases** ("brains") that an LLM writes and maintains for you, as plain markdown you browse in [Obsidian](https://obsidian.md/).

A brain is a curated collection of sources (books, PDFs, articles) that the LLM reads once, distills into an interlinked wiki, and keeps current. You then **cite the brain** to validate ideas, sharpen decisions, and improve your processes, with answers traced back to real sources instead of re-derived from scratch on every question.

> **Status: work in progress.** This README is a stub. Full quickstart, screenshots, and installation land in v1.0. See [`PLAN-CEREBRO.md`](../PLAN-CEREBRO.md) and [`docs/STATUS.md`](docs/STATUS.md) for progress.

## What this is

- **`BLUEPRINT.md`** — the normative pattern any LLM follows to create, ingest, query, and lint a brain. This is the core of the project.
- **A Claude Skill** — install it in Claude (Desktop, Code, or claude.ai) to drive the whole workflow in natural language.
- **Multi-AI templates** — an `AGENTS.md` (for Codex, Cursor, Gemini CLI) and a Custom GPT prompt, so the pattern is not locked to one vendor.
- **PDF→markdown tooling** — convert sources once and read the markdown, saving 5-10x the tokens of reading raw PDFs.

## Credit

This project is an installable, opinionated implementation of the **LLM Wiki** pattern described by **Andrej Karpathy** ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). That gist communicates the idea; this repo turns it into a ready-to-use kit and adds:

- A normative, step-by-step blueprint (not just an abstract description).
- An installable Claude Skill and multi-AI templates.
- Per-page confidence levels and explicit contradiction handling.
- Anti-hallucination rules for querying ("no coverage" instead of inventing).
- An idea-validation output format (supports / contradicts / not covered / verdict).
- PDF→markdown conversion wired into the ingest step.

## License

[MIT](LICENSE) © 2026 Andres Buonaiuto
