# BLUEPRINT: how to build and maintain a brain

This is the normative specification any LLM follows to build and maintain a
**brain**: a persistent, interlinked markdown knowledge base, browsed in
Obsidian, built from curated sources (books, PDFs, articles) and designed to be
cited when validating ideas and making decisions.

This document is authoritative. Follow it literally. "MUST" is mandatory,
"SHOULD" is a strong default, "MAY" is optional.

It implements the LLM Wiki pattern by Andrej Karpathy
(<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>).

---

## 1. Core principle

A brain is NOT RAG. The point is not to retrieve raw chunks at query time. The
LLM builds and maintains a persistent, interlinked wiki that gets richer with
every source ingested and every question answered. Knowledge is compiled once
and kept current, not re-derived on every query.

Division of labor:

- **The human** curates sources, directs the analysis, asks the questions.
- **The LLM** reads, summarizes, cross-references, flags contradictions, files,
  and maintains. All wiki writing is the LLM's job. The human rarely, if ever,
  writes wiki pages.

The wiki is a compounding artifact. Cross-references are already there.
Contradictions are already flagged. The synthesis already reflects everything
read so far.

## 2. Anatomy of a brain

```
[brain-name]/
├── AGENTS.md            # this brain's schema (from templates/AGENTS.md, filled in)
├── CLAUDE.md            # one-line pointer to AGENTS.md
├── index.md             # catalog of every wiki page, by category
├── log.md               # chronological, append-only activity record
├── sources/             # original documents. IMMUTABLE. Never edited.
│   ├── converted/       # markdown conversions of the originals (read THESE)
│   └── assets/          # images extracted from sources
└── wiki/                # everything the LLM writes and owns
    ├── source-notes/    # one page per ingested source
    ├── concepts/        # one page per concept, framework, or idea
    ├── entities/        # authors, companies, people, tools
    ├── synthesis/       # cross-source pages, the evolving thesis
    └── answers/         # valuable queries filed back as pages
```

Rules:

- `sources/` is the source of truth and is IMMUTABLE. The LLM reads from it and
  never modifies it.
- The LLM owns `wiki/` entirely: it creates, updates, and cross-references pages.
- File names MUST be kebab-case, ASCII, no accents: `competitive-advantage.md`.

## 3. Page conventions

Every wiki page MUST start with YAML frontmatter:

```yaml
---
type: source | concept | entity | synthesis | answer
sources: [source-slug-1, source-slug-2]
updated: 2026-07-17
confidence: high | medium | low
tags: [business, strategy]
---
```

- `type` MUST match the folder the page lives in.
- `sources` lists the source slugs backing the page (the file names in
  `wiki/source-notes/` without extension). Empty only for pure `synthesis`.
- `confidence`:
  - **high** if several independent sources agree.
  - **medium** if a single source asserts it.
  - **low** if sources contradict each other, or it is the LLM's extrapolation.
- `updated` MUST be an absolute date (`YYYY-MM-DD`), never relative.

Linking:

- Internal links MUST use Obsidian wiki syntax: `[[page-name]]`.
- Link generously. Every entity, concept, and source mentioned on a page SHOULD
  link to its own page (create the page if it does not exist yet).

Writing:

- One page, one topic. Prefer short, linked pages over long monolithic ones.
- Every important factual claim MUST be traceable to a source, with chapter or
  page number where available. LLM inferences MUST be marked inline:
  `(inference, not stated in the sources)`.
- No em dashes (—); use commas or parentheses.

## 4. Operations

Four operations. Detect which one the user is asking for and follow its steps.

### 4.1 CREATE

Set up a new brain.

1. Ask the user for: the brain **name**, its **purpose** in one sentence (what
   decisions it will support), and the **kind of sources** expected.
2. Copy `templates/brain-structure/` to `[brain-name]/`. The skeleton already
   includes `AGENTS.md`, `CLAUDE.md`, `index.md`, `log.md`, and the empty folder
   tree, so copying it yields a complete brain.
3. In the new `AGENTS.md`, fill in `{{BRAIN_NAME}}` and `{{PURPOSE}}` and delete
   the instruction quote block. `CLAUDE.md` already points to `AGENTS.md` (Claude
   Code reads `CLAUDE.md`; other agents read `AGENTS.md`).
4. Write the first `log.md` entry: `## [YYYY-MM-DD] create | [brain-name]`.
5. Register the brain in the root `brains.md` catalog (name, purpose, date,
   source count 0). Create `brains.md` if it does not exist.
6. MAY run `git init` in the brain folder for version history.

### 4.2 INGEST

Add a new source to the brain. A single source may touch 5 to 15 wiki pages.

1. **Convert first.** If the source is a PDF, docx, or epub, convert it to
   markdown once into `sources/converted/[slug].md` (see section 6) and read the
   markdown, not the original. This saves 5 to 10x the tokens of reading a raw
   PDF. Keep the original in `sources/` as backup.
2. **Read the whole source.** For a long source (a book), read in blocks of
   roughly 20 pages or by chapter, taking interim notes before synthesizing.
3. **Discuss** the 3 to 5 key takeaways with the user before writing, so they
   can steer the emphasis. In explicit batch ingestion, skip this step only if
   the user asked to.
4. **Write the source note** at `wiki/source-notes/[slug].md`: central thesis,
   main arguments, citable data and figures (with chapter or page of origin),
   and the source's limitations.
5. **Update the cross-wiki.** Create or update the concept and entity pages the
   source touches. Strengthen or challenge existing synthesis pages.
6. **Handle contradictions** (section 5). Never overwrite a prior claim in
   silence.
7. **Update `index.md`** with new or changed pages.
8. **Append to `log.md`**: `## [YYYY-MM-DD] ingest | Source Title` followed by
   the list of pages touched.
9. **Update `brains.md`** (source count).

### 4.3 QUERY

Answer a question, validate an idea, or sharpen a decision against the brain.

1. Read `index.md` to locate relevant pages, then read those pages. Do not read
   the whole wiki.
2. **If the brain does not cover the topic, say so explicitly**: "the brain has
   no coverage on X." NEVER invent content and attribute it to the brain. This
   is the single most important rule for decision support.
3. Answer citing wiki pages with `[[links]]` and, where available, the original
   source with chapter or page.
4. State the confidence level and surface contradictions. An idea validated
   against conflicting sources MUST mention the conflict.
5. For **idea validation**, use this structure:
   - **Supports** the idea (with citations).
   - **Contradicts or qualifies** the idea (with citations).
   - **Not covered** by the brain.
   - **Verdict.**
6. **File valuable answers back.** If the answer produced new synthesis (a
   comparison, an analysis, a connection not written before), offer to save it
   to `wiki/answers/`. If the user accepts, file it, link it from related pages,
   and register it in `index.md` and `log.md`.

### 4.4 LINT

Health-check the brain, on request or periodically.

1. Contradictions between pages not yet marked as such.
2. Stale claims superseded by more recent sources.
3. Orphan pages with no inbound links (Obsidian graph view helps).
4. Concepts mentioned on 3 or more pages that lack their own page.
5. Broken `[[links]]` to non-existent pages: create them or fix the link.
6. Mismatches between `index.md` and the actual files.
7. Data gaps a web search or a new source could fill: propose them to the user,
   do not act on your own.
8. Record the result in `log.md`: `## [YYYY-MM-DD] lint | summary of findings`.

## 5. Handling contradictions

When a new source contradicts something already in the wiki:

- Do NOT overwrite the older claim silently.
- On the affected page, add a `## Contradiction` section stating both positions
  with the source behind each side.
- Lower the page's `confidence` to `low`.
- Note it in the `log.md` ingest entry.

The value of a brain for decisions comes partly from surfacing where good
sources disagree, not from hiding it.

## 6. Source conversion

Reading raw PDFs is expensive and error-prone. Convert once, read the markdown.

- Default: `python tools/convert.py sources/original.pdf -o sources/converted/original.md`
  (a thin wrapper around markitdown).
- For scanned or layout-heavy PDFs where markitdown output is poor, use docling
  as a fallback.
- Conversion is a token optimization, not a hard requirement. The blueprint
  still works if an agent reads a PDF directly; it just costs more.

## 7. Scale and tooling

- Up to roughly 100 sources and a few hundred pages, `index.md` is enough as the
  search mechanism. Do NOT add RAG or embeddings before you need them.
- Beyond that, consider a local markdown search engine such as qmd
  (<https://github.com/tobi/qmd>). Install third-party tools only with the
  user's approval.
- Obsidian is the viewer: graph view shows hubs and orphans; Dataview queries
  the frontmatter; Marp turns pages into slides. All optional.
- A brain is just a git repo of markdown, so you get history and diffs for free.
