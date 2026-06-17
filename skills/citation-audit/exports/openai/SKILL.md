---
name: citation-audit
description: Decompose cited statements into atomic claims, cross-check whether each cited paper actually supports the claim, extract the exact supporting text from the abstract or full paper, and emit a structured JSON citation audit.
---

# Citation Relevance Audit

## Overview

Verify that every citation in a manuscript actually supports the statement it backs. For each cited
statement you decompose it into atomic claims, locate the exact supporting text in the cited source
(abstract or full paper), judge relevance, and record everything in a structured JSON audit. The goal
is to eliminate mismatched or hallucinated citations and to leave an auditable evidence trail.

## Core principles

1. **Evidence comes only from the cited source** — Supporting text must be quoted from the cited
   paper's abstract or full text. Never paraphrase from memory or invent a quote. If no source text is
   available, mark the citation unverifiable rather than guessing.
2. **Atomise before judging** — Split each cited statement into atomic claims (see `atomise-claims`) so
   relevance is judged per claim, not per bundled sentence.
3. **Relevance is explicit** — Each citation gets a verdict: `Relevant`, `Partially relevant`, or
   `Not relevant`, with notes explaining which claim each source supports.
4. **Unsupported citations do not survive** — Do not keep citations that do not support the statement.
   Replace, reassign, or flag them; never leave a known-irrelevant citation in place.
5. **Faithful quoting** — `actual_text` is the verbatim supporting sentence(s) from the source, not a
   summary.

## Step-by-step process

1. **Collect the statements** and their citation keys from the manuscript (e.g. parse `\citep{...}`
   / `\citet{...}`). Keep each statement's source location.
2. **Atomise** each cited statement into atomic claims.
3. **For each citation key, retrieve the source text** — prefer the abstract; consult the full paper
   when the abstract is insufficient. Locate the sentence(s) that bear on the claim.
4. **Extract the exact supporting text** (`actual_text`) for each `citing_key`.
5. **Assess relevance** per citation and overall for the statement: does the source fully support,
   partially support, or fail to support the claim?
6. **Write the JSON audit** (structure below), one entry per synthesized statement.
7. **Act on the findings** — for `Not relevant` citations, remove/replace/flag them in the manuscript;
   for `Partially relevant`, note which sub-claim is supported and what is missing.

## Required JSON structure

Emit a JSON array; each entry documents one synthesized manuscript statement:

```json
[
  {
    "synthesized_statement": "Blinking is a physiological process that involves the closure and reopening of the eyelids \\citep{nystrm2024what}.",
    "sources": [
      {
        "citing_key": "nystrm2024what",
        "actual_text": "Blink is related to closure and reopening of the eyelids."
      }
    ],
    "relevance_assessment": "Relevant",
    "notes": "The cited text directly supports the statement."
  },
  {
    "synthesized_statement": "Blinking can be influenced by both physiological and cognitive factors \\citep{nystrm2024what,nystrm2030paper}.",
    "sources": [
      { "citing_key": "nystrm2024what", "actual_text": "Blinking is associated with eyelid closure and reopening." },
      { "citing_key": "nystrm2030paper", "actual_text": "Blinking may vary according to cognitive and physiological conditions." }
    ],
    "relevance_assessment": "Partially relevant",
    "notes": "The first citation supports the physiological definition, while the second better supports the cognitive-factor claim."
  }
]
```

Each entry MUST include: the synthesized manuscript statement, the citing key(s), the exact supporting
text from each cited source, a relevance assessment, and notes explaining full/partial/no support.

## Rules

- Always quote `actual_text` verbatim from the cited source; never fabricate or paraphrase it.
- Always assign one of `Relevant` / `Partially relevant` / `Not relevant` per statement, with notes.
- Never keep a citation that is not relevant to the statement — replace or flag it.
- If the source text cannot be obtained, set the verdict accordingly and note "source unavailable";
  do not invent supporting text.
- Preserve the exact citation keys as written in the manuscript.

## Common mistakes to avoid

- **Fabricating `actual_text`** that sounds plausible but is not in the paper — this is the failure the
  skill exists to prevent.
- **Judging a multi-claim sentence as a whole** when one citation supports only part of it (use
  `Partially relevant` and atomise).
- **Accepting topical-but-non-supporting citations** (same domain, wrong claim) as relevant.
- **Leaving flagged citations in the manuscript** without removal, replacement, or an explicit flag.

## Additional guidance

Store the audit as a JSON file (e.g. `citation_audit.json`) plus, optionally, per-section files. This
skill composes with `atomise-claims` (statement decomposition) and with a knowledge library when the
sources live in a CSV/SQLite store (see `literature-review-writing`). When the full paper is large,
search it for the claim's keywords to find the supporting passage rather than reading end to end.

### Sourcing `actual_text` from a reference library

When abstracts/full text are not separate files, they usually live in the reference manager export. A Zotero
CSV export, for example, carries the abstract in an **"Abstract Note"** column keyed by the bibtex **"Key"** —
read `actual_text` from there and cross-check keys against the bib catalogue so you never cite a key that does
not exist. If a key has no stored abstract, set `actual_text` to `""` and flag it (mark the claim unverifiable)
rather than inventing supporting text.

**Encoding gotcha:** these CSV/JSON files are UTF-8 and routinely contain curly quotes, en-dashes, and other
non-ASCII characters. Always open them with an explicit `encoding="utf-8"` (do not rely on the platform default
such as Windows cp1252, which raises `UnicodeDecodeError` mid-file). Write the audit JSON with `ensure_ascii=False`
+ UTF-8 so quoted text round-trips faithfully.
