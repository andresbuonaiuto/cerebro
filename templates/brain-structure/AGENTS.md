# AGENTS.md — {{BRAIN_NAME}}

Operating manual for any AI agent maintaining this brain. This file is
self-contained: it does not depend on the cerebro repo being present.

> Replace `{{BRAIN_NAME}}` and `{{PURPOSE}}` when creating the brain, then delete
> this quote block.

## Purpose

{{PURPOSE}}

This brain exists to be **cited** when validating ideas and making decisions.
Answers must trace back to real sources, never be invented.

## What this is

A persistent, interlinked markdown wiki built from curated sources. It is NOT
RAG: knowledge is compiled once into the wiki and kept current, not re-derived
per question. The human curates sources and asks questions; you (the agent) do
all the reading, summarizing, cross-referencing, and filing.

## Structure

```
sources/            # original documents. IMMUTABLE. Never edit.
  converted/        # markdown conversions (read THESE, not raw PDFs)
  assets/           # images extracted from sources
wiki/
  source-notes/     # one page per ingested source
  concepts/         # one page per concept, framework, or idea
  entities/         # authors, companies, people, tools
  synthesis/        # cross-source pages, the evolving thesis
  answers/          # valuable queries filed back as pages
index.md            # catalog of every wiki page, by category
log.md              # chronological, append-only activity record
```

## Page conventions

Every wiki page starts with frontmatter:

```yaml
---
type: source | concept | entity | synthesis | answer
sources: [source-slug-1]
updated: YYYY-MM-DD
confidence: high | medium | low
tags: [tag1, tag2]
---
```

- `confidence`: high if several sources agree, medium if one source asserts it,
  low if sources contradict or it is your extrapolation.
- File names: kebab-case, ASCII, no accents.
- Internal links use `[[page-name]]`. Link generously.
- Every factual claim traces to a source (chapter/page where available). Mark
  your own inferences: `(inference, not stated in the sources)`.
- No em dashes (—); use commas or parentheses.

## Ingest a source

1. **Convert first**: PDF/docx/epub to `sources/converted/[slug].md`, read the
   markdown. (`python convert.py sources/x.pdf -o sources/converted/x.md` if the
   converter is available; otherwise read the original, at higher token cost.)
2. Read the whole source; for a book, read in ~20-page blocks with interim notes.
3. Discuss the 3 to 5 key takeaways with the human before writing.
4. Write `wiki/source-notes/[slug].md`: thesis, main arguments, citable
   data/figures with origin, limitations.
5. Create or update the concept and entity pages it touches; update synthesis.
6. Handle contradictions (see below), never overwrite silently.
7. Update `index.md`; append to `log.md`:
   `## [YYYY-MM-DD] ingest | Source Title` + pages touched.

## Answer a query / validate an idea

1. Read `index.md`, then the relevant pages. Do not read the whole wiki.
2. **If the brain has no coverage, say so.** Never invent and attribute to the
   brain. This is the most important rule.
3. Cite wiki pages with `[[links]]` and the original source where available.
4. State confidence; surface contradictions.
5. For idea validation use: **Supports** / **Contradicts or qualifies** /
   **Not covered** / **Verdict**.
6. Offer to file valuable new synthesis into `wiki/answers/`.

## Handle contradictions

When a new source contradicts the wiki: do not overwrite. Add a
`## Contradiction` section on the affected page with both positions and their
sources, lower `confidence` to low, and note it in the log.

## Lint (on request)

Check for: unmarked contradictions, stale claims, orphan pages, concepts without
a page, broken `[[links]]`, `index.md` mismatches, and data gaps to fill. Record
findings in `log.md`.
