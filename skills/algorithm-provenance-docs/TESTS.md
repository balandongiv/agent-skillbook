# Test Prompts: Algorithm Provenance Documentation

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Document this algorithm so another agent can pick it up later without reading the commit history."

Expected behavior: The agent writes a `docs/algorithms/<name>.md` with the fixed sections including provenance, method, falsifiers, exploratory results, and how to select/run/test it.

---

## Test Prompt 2

> "We just consolidated eight methods — give each one a consistent write-up."

Expected behavior: The agent uses the same fixed section order for every report so they are comparable, and adds each to the catalogue/README.

---

## Test Prompt 3

> "Where did this method come from and what was it supposed to prove?"

Expected behavior: The agent records the source paper (and where it is listed), the source repo, the origin, and the hypothesis, grounding claims in a real reference rather than inventing one.

---

## Test Prompt 4

> "Just put the F1 number in the doc."

Expected behavior: The agent attaches the split, n, baseline comparison, and an exploratory caveat to the number, and adds the pre-registered falsifiers rather than only the passing result.

---

## Test Prompt 5

> "The doc copies the event-matching code. Is that right?"

Expected behavior: The agent links the shared single-source harness instead of duplicating it, to prevent drift.

---

## Test Prompt 6

> "Make sure the docs and the code actually agree."

Expected behavior: The agent cross-checks the doc's selector name, module path, runner, and modalities against the registry and fixes mismatches.

---

## Test Prompt 7

> "Can a new agent run this from the doc alone?"

Expected behavior: The agent applies the future-agent test — selector, module path, runner, and test command are present — and fills any gap that would force reading the git history.
