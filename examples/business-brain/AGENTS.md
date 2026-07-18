# AGENTS.md: business-brain

Operating manual for any AI agent maintaining this brain. This file is
self-contained: it does not depend on the cerebro repo being present.

## Purpose

Validate business and money decisions against classic, public-domain texts on
wealth-building and enterprise. A worked example of the cerebro pattern, small
enough to read end to end.

This brain exists to be **cited** when validating ideas and making decisions.
Answers must trace back to real sources, never be invented.

## What this is

A persistent, interlinked markdown wiki built from curated sources. It is NOT
RAG: knowledge is compiled once into the wiki and kept current, not re-derived
per question. The human curates sources and asks questions; you (the agent) do
all the reading, summarizing, cross-referencing, and filing.

## Structure

```
sources/            # provenance of the originals. IMMUTABLE.
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

Every wiki page starts with frontmatter: `type`, `sources`, `updated`,
`confidence` (high if several sources agree, medium if one asserts it, low if
sources contradict or it is your extrapolation), `tags`. File names are
kebab-case ASCII. Internal links use `[[page-name]]`. Every factual claim traces
to a source with chapter where available. Mark inferences:
`(inference, not stated in the sources)`. No em dashes.

## Operations

Follow the cerebro blueprint: ingest a source (convert, read, discuss, write a
source note, update concepts/entities/synthesis, handle contradictions, update
index and log); answer a query or validate an idea (read index then pages, say
"no coverage" when absent, cite pages and sources, use Supports / Contradicts or
qualifies / Not covered / Verdict); lint on request. When a new source
contradicts the wiki, do not overwrite: add a `## Contradiction` section, lower
confidence, note it in the log.
