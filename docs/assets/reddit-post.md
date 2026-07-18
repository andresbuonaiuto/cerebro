<!-- Suggested subreddits: r/ClaudeAI, r/ObsidianMD, r/LocalLLaMA -->

**Title:** I turned Andrej Karpathy's "LLM Wiki" idea into an installable kit (Claude skill + blueprint, open source)

Karpathy posted a gist a while back describing a pattern he calls "LLM Wiki": instead of RAG (upload docs, retrieve chunks, answer, forget), you have the LLM build and maintain a persistent Markdown wiki from your sources. Read a book once, get a wiki page. Read the next one, the LLM cross-references it, updates concept pages, flags contradictions. Nothing gets re-derived from scratch each time.

It's a great idea but it was just a gist, a description to paste into your own agent. I wanted to actually use it for something specific (validating business decisions against a library of books I trust), so I built it out into something installable:

- **`BLUEPRINT.md`** — a normative spec any LLM follows: how to structure a brain, ingest a source, answer a query, lint for contradictions. The important rule: if the brain has no coverage on something, it says so instead of inventing an answer.
- **A Claude skill** (zip, install via Settings → Capabilities → Skills) that drives the whole thing in plain language.
- **`AGENTS.md` templates** for Codex/Cursor/Gemini CLI, plus a Custom GPT prompt for ChatGPT (query-only there, since it has no filesystem).
- **A PDF→Markdown converter** (thin `markitdown` wrapper) so you're not burning tokens reading raw PDFs.
- **A full worked example brain** in the repo, built from two public-domain books, so you can see the pattern (including a documented contradiction between the sources) without installing anything.

It's just Markdown files you browse in Obsidian. No vector DB, no embeddings, index.md is the whole search mechanism until you have ~100+ sources.

MIT licensed: <https://github.com/andresbuonaiuto/cerebro>

Full credit to Karpathy for the original pattern (linked in the README), this is my attempt at turning the idea into something you can actually pick up and use. Feedback welcome, especially on the blueprint itself.
