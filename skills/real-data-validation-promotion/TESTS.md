# Test Prompts: Real-Data Validation Promotion

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Synthetic data is not acceptable here. Validate this stage on the actual dataset first, then scale up."

Expected behavior: The agent chooses the smallest representative real-data smoke scope first, defines pass criteria, and only then promotes to broader runs.

---

## Test Prompt 2

> "Run a one-session real-data smoke test before the full sweep and tell me what artifacts prove it passed."

Expected behavior: The agent uses a smallest-real-scope workflow and validates real artifacts, counts, and summaries instead of only process exit.

---

## Test Prompt 3

> "This package is installed editable from a local repo. If the smoke test fails there, fix it at the source and rerun."

Expected behavior: The agent treats the editable dependency as part of the validated system, patches it there if needed, and reruns the smoke scope before promotion.

---

## Test Prompt 4

> "Create a readable validation report and keep the heavy plot gallery separate."

Expected behavior: The agent separates summary EDA from bulky plot outputs and uses the summary artifact as the primary validation surface.

---

## Test Prompt 5

> "Tell me what still blocks confidence after the real-data smoke passes."

Expected behavior: The agent reports residual risks honestly instead of overstating readiness.
