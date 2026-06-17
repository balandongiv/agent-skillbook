# Test Prompts: Citation Relevance Audit

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Audit the citations in my introduction and tell me which ones don't actually support the sentence.

Expected behavior: Atomise each cited statement, retrieve source text per key, assess relevance, and
produce the JSON audit flagging non-supporting citations.

---

## Test Prompt 2

> For each citation, extract the exact supporting text from the abstract or paper and save a JSON audit.

Expected behavior: Quote `actual_text` verbatim per citing key and write the array-of-objects JSON in
the required structure.

---

## Test Prompt 3

> Check whether these two papers really back this multi-part claim.

Expected behavior: Split the claim into atomic parts, map each citation to the part it supports, and
return `Relevant` / `Partially relevant` / `Not relevant` with notes.

---

## Test Prompt 4

> Remove or flag any citations that are off-topic for the statement they're attached to.

Expected behavior: Mark non-supporting citations `Not relevant`, recommend removal/replacement, and do
not leave them silently in place.

---

## Test Prompt 5

> Produce a citation audit JSON for the discussion section using only the cited papers' text.

Expected behavior: Build the JSON audit grounded strictly in source text; mark any citation whose
source text is unavailable as unverifiable rather than inventing a quote.
