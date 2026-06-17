# Test Prompts: Strategy C Experiment Log

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> I'm about to try a new parameter setting for Strategy C — log it properly.

Expected behavior: Create a structured `## Strategy: ...` entry under
`development_strategy/strategy_C/obs/` with Date/Proposal/Rationale/Status and the required subsections.

---

## Test Prompt 2

> Record this Strategy C validation run with its metrics and sources.

Expected behavior: Add Performance & Metrics (Before/After/Change with sources) and an Outcome verdict.

---

## Test Prompt 3

> This Strategy C experiment failed — note it as a dead end.

Expected behavior: Log Status: Abandoned with Outcome, "no implementation benefit", and Learnings.

---

## Test Prompt 4

> Explain why this Strategy C approach is a better implementation than Strategy A and B.

Expected behavior: Fill the Implementation Benefits section comparing modularity/debuggability/contract,
or state explicitly that no benefit was demonstrated.

---

## Test Prompt 5

> Make sure this Strategy C spinoff gets a traceable history entry.

Expected behavior: Append a complete, template-consistent log entry so future agents see the history.
