# Log

Chronological, append-only record of what happened and when. Newest entries at
the bottom.

Each entry starts with a consistent prefix so the log is greppable:

```bash
grep "^## \[" log.md | tail -5    # the last 5 entries
```

Format: `## [YYYY-MM-DD] <op> | <title>`, where `<op>` is one of
`create`, `ingest`, `query`, `lint`.

<!-- entries below -->
