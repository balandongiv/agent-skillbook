# Test Prompts: Knowledge-Library-Grounded Literature Review Writing

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Write a related-work section using only the papers in this CSV library.

Expected behavior: Load the CSV, select relevant keys, write themed paragraphs citing only existing
keys, and flag any coverage gaps without inventing papers.

---

## Test Prompt 2

> Expand my literature review using the SQLite knowledge base — don't add anything not in it.

Expected behavior: Query the SQLite store, add only library-backed keys that fill real thematic gaps,
and avoid fabricated citations.

---

## Test Prompt 3

> Group these references into themes and write flowing prose, not a citation list.

Expected behavior: Cluster the library candidates into method/problem themes and synthesise each into a
coherent paragraph.

---

## Test Prompt 4

> Make sure every citation here actually exists in our library and supports the sentence.

Expected behavior: Restrict citations to library keys and hand off to citation verification; flag any
key not present.

---

## Test Prompt 5

> The review feels thin — add more relevant work, but no padding.

Expected behavior: Add only genuinely relevant, library-backed papers and explicitly avoid weakly
related filler.
