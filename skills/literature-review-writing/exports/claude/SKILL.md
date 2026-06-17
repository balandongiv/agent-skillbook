---
name: literature-review-writing
description: Write or expand a literature review / related-work section using only a provided knowledge library (CSV or SQLite), citing only keys that exist in that library, with no invented papers, facts, or citation keys.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Knowledge-Library-Grounded Literature Review Writing

## Overview

Write or expand a literature-review / related-work section using **only** a provided knowledge library —
a CSV or SQLite store of papers (keys, titles, abstracts, metadata). Every citation must be a key that
exists in the library, and every claim about prior work must be traceable to that library. This is the
anti-hallucination contract: no invented papers, no invented citation keys, no facts the library does
not support.

## Core principles

1. **The library is the only source of truth** — Cite only keys present in the CSV/SQLite. If a needed
   paper is not in the library, flag the gap; do not invent a key or fabricate the paper.
2. **No fabricated content** — Claims about a paper must match its title/abstract/metadata in the
   library. Do not assert findings the library cannot support.
3. **Themes, not lists** — Organise prior work into coherent thematic paragraphs (e.g. by method
   family, problem, or dataset), not a flat citation dump.
4. **Every citation supports its sentence** — Place each key where the library content actually backs
   the claim; pair with the `citation-audit` skill to verify.
5. **No padding** — Add only genuinely relevant papers. Do not inflate the section with weakly related
   citations to look comprehensive.

## Step-by-step process

1. **Load the library** (CSV or SQLite). Identify the columns/fields: citation key, title, abstract,
   year, venue, tags. Confirm which keys already exist.
2. **Scope the review** from the manuscript's topic and the section's purpose; list the themes to cover.
3. **Select candidates** by querying the library (keyword/tag/title match against each theme). Record,
   for each candidate, the key + the library text that justifies inclusion.
4. **Cluster** candidates into themed paragraphs; decide narrative order (foundational -> method
   families -> closest prior work -> contrast with the present work).
5. **Draft** each paragraph as flowing prose, citing only library keys, each citation placed where the
   library content supports the sentence.
6. **Flag gaps** where a theme needs a paper not in the library, as an explicit note for the user to
   add to the library — never fill the gap with an invented citation.
7. **Verify** with the citation-audit skill: confirm each key exists and supports its sentence.

## Rules

- Always restrict citations to keys that exist in the provided CSV/SQLite library.
- Always ground each prior-work claim in the library's title/abstract/metadata.
- Never invent a paper, author, finding, or citation key; never cite from memory.
- Never pad with weakly related citations; prefer fewer, well-supported ones.
- Always surface missing-coverage gaps as explicit flags rather than fabricating.

## Common mistakes to avoid

- **Citing a plausible-looking key** that is not actually in the library.
- **Stating a finding** that the library's abstract does not contain.
- **Citation-list paragraphs** with no synthesis or contrast.
- **Padding** the section with on-topic-but-non-supporting papers to seem thorough.

## Additional guidance

For a CSV library, read the header and match on key/title/tag columns; for SQLite, query the studies
table (e.g. `SELECT key, title, abstract FROM studies WHERE ...`). Keep an inclusion log mapping each
cited key to the library row that justified it, which doubles as the input to `citation-audit`. When the
user asks to "expand" an existing review, first list currently-cited keys, then add only new
library-backed keys that fill real thematic gaps. This skill composes with `citation-audit` (verify
relevance) and `atomise-claims` (check each prior-work claim).
