# Test Prompts: Atomise Claims into Atomic Statements

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Break this paragraph into atomic claims so I can fact-check each one.

Expected behavior: Segment into sentences, split compound sentences/lists into single-fact claims,
resolve references, and emit a structured list with source location and types.

---

## Test Prompt 2

> Decompose each sentence in the introduction into atomic statements and keep the citation keys attached.

Expected behavior: Produce per-sentence atomic claims, each carrying the citation keys from the
original sentence, ready for a citation audit.

---

## Test Prompt 3

> Atomise this claim without changing its meaning or the hedging.

Expected behavior: Decompose while preserving hedges, numbers, and scope exactly; do not strengthen or
weaken any claim.

---

## Test Prompt 4

> Which of these are factual claims versus just framing?

Expected behavior: Classify each atomic claim as empirical/numeric/citation-backed vs framing/opinion
and flag overclaims.

---

## Test Prompt 5

> Prepare the discussion section for proof extraction by listing the atomic claims.

Expected behavior: Output a per-paragraph list of self-contained atomic claims with ids and source
locations suitable for assigning evidence and verdicts.
