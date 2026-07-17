# ADR 002 — No RAG: a markdown index is the search mechanism

- **Status:** accepted
- **Date:** 2026-07-17

## Context

Most "chat with your documents" systems use embeddings + vector retrieval (RAG).
The LLM Wiki pattern deliberately does not: it maintains a persistent, curated
wiki instead of re-retrieving raw chunks per query.

## Options considered

- **Embeddings/RAG** — scales to large corpora, but adds infrastructure, hides
  reasoning behind opaque retrieval, and re-derives knowledge on every query.
- **Markdown index (`index.md`) + hand-maintained wiki** — the LLM reads the
  index to find pages, then reads those pages. No vector DB.

## Decision

Markdown index. The LLM navigates via `index.md` and `[[wiki links]]`. Search
infrastructure is only considered past ~100 sources (see ADR on scale in the
blueprint), and even then via a local tool (qmd), not a hosted vector store.

## Consequences

- Zero infra, fully offline, git-friendly, human-inspectable.
- Knowledge compounds instead of being re-retrieved each time.
- Does not scale to thousands of sources without an added search tool; that is
  an accepted limit for a personal-scale knowledge base.
