---
name: cerebro
description: Create and maintain "brains": persistent, interlinked markdown knowledge bases that an LLM builds from your sources (books, PDFs, articles) and keeps current, so you can cite them to validate ideas and make decisions. Use when the user says /cerebro, "create a brain", "ingest this book/PDF into the brain", "query the brain about X", "validate this idea against the brain", or "lint the brain".
---

# cerebro

Build and maintain knowledge "brains" following `BLUEPRINT.md` (bundled next to
this file). The blueprint is the source of truth: read it in full before running
any operation and follow it literally.

## Brains root

Brains live under a single root folder you choose (for example
`~/brains` or `D:\brains`). A registry file `brains.md` at that root lists every
brain with its purpose and status.

- If the user names the root or is working inside it, use it.
- Otherwise ask once for the root folder, then create `brains.md` there if it
  does not exist.
- Each brain is a subfolder: `[root]/[brain-name]/`.

## Operations

Detect which operation the user wants and follow the matching section of
`BLUEPRINT.md`:

| The user says | Operation |
|---|---|
| "create a brain for/about X" | **CREATE** (blueprint 4.1) |
| "ingest / add / process this book / PDF / article" | **INGEST** (4.2) |
| "query the brain", "validate this idea", "what does the brain say about X" | **QUERY** (4.3) |
| "lint", "health-check the brain" | **LINT** (4.4) |

## Rules for this skill (on top of the blueprint)

1. On CREATE: ask for the brain name, its one-sentence purpose, and the kind of
   sources before generating anything.
2. On QUERY: if the user does not name the brain and there is more than one in
   `brains.md`, ask which one.
3. Never modify anything inside a brain's `sources/`: it is immutable.
4. After any operation, update the brain's `log.md` and, if its overall state
   changed, its entry in `brains.md`.
5. If the brain has no coverage for a query, say so. Never invent content and
   attribute it to the brain.
