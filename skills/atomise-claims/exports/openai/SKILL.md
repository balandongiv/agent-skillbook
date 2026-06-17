---
name: atomise-claims
description: Decompose any sentence, paragraph, or section into atomic, independently checkable factual claims so each can be verified, cited, or revised on its own.
---

# Atomise Claims into Atomic Statements

## Overview

Break text into **atomic claims**: the smallest standalone statements that are each independently
true-or-false and independently checkable. Atomisation is the prerequisite for citation auditing,
fact-checking, proof extraction, and overclaim detection — you cannot verify a sentence that bundles
five claims behind one citation.

## Core principles

1. **One claim, one fact** — Each atomic statement asserts a single verifiable proposition. If a
   sentence uses "and", "while", "because", or lists, it almost certainly contains multiple claims.
2. **Self-contained** — Resolve pronouns and references so each atomic claim stands alone without the
   surrounding sentence ("it", "this method", "they" must be replaced by the referent).
3. **Faithful, not inflated** — Do not add, strengthen, or weaken meaning. Preserve hedges ("may",
   "suggests") and quantities exactly as written; atomisation is decomposition, not interpretation.
4. **Carry the provenance** — Keep each atomic claim linked to its source location (paragraph/sentence)
   and to any citation keys attached to the original sentence.
5. **Separate fact from framing** — Distinguish empirical claims (checkable against data/sources) from
   rhetorical or motivational framing, which may need a different verification path or none.

## Step-by-step process

1. **Segment** the input into sentences, keeping the source location for each.
2. **Split** each sentence at logical connectives and enumerations into candidate atomic claims.
3. **Decontextualise** each candidate: replace pronouns/anaphora with their referents so it reads alone.
4. **Classify** each claim as one of: empirical/factual, numeric/quantitative, citation-backed, or
   framing/opinion. Attach any citation keys that applied to the original sentence.
5. **Emit** a structured list: claim id, source location, atomic text, type, attached citation key(s).
6. **Hand off** to the appropriate verifier (citation audit, results-number check, proof extraction).

## Rules

- Always split conjunctions and lists into separate atomic claims unless they are a single indivisible fact.
- Always resolve references so each claim is self-contained.
- Never change numbers, units, hedges, or scope when atomising.
- Never merge two distinct claims to make verification easier.
- Always preserve the mapping from atomic claim back to its original sentence and citation keys.

## Common mistakes to avoid

- **Over-splitting** a single fact into fragments that are no longer meaningful on their own.
- **Under-splitting** a compound sentence so one citation appears to cover claims it does not support.
- **Silently strengthening** a hedged claim ("may bias" becoming "biases") during decomposition.
- **Dropping the citation linkage**, which makes the downstream audit impossible.

## Additional guidance

Output is most useful as a list of objects, e.g.
`{id, source, atomic_text, type, citation_keys[]}`. For a manuscript, run atomisation per paragraph
and keep a per-paragraph file plus an aggregate summary. This skill pairs directly with
`citation-audit` (assigns evidence + relevance to each citation-backed atomic claim) and with proof
extraction (assigns supporting text + a supported/weak/unsupported verdict to each claim).
