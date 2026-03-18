# Test Prompts: Experiment Runbook Discipline

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Run a fresh full validation sweep on this dataset and tell me which files I can watch live."

Expected behavior: The agent creates a runbook-oriented plan with a fresh experiment prefix, a markdown note, rolling log and status artifacts, and explicit live-watch paths.

---

## Test Prompt 2

> "Start this long batch experiment in the background and make sure it is actually progressing."

Expected behavior: The agent emphasizes background execution plus real progress verification, not only process liveness, and describes rolling logs and live status files.

---

## Test Prompt 3

> "I changed the scoring logic. Please rerun the validated subjects safely."

Expected behavior: The agent increments the experiment prefix, avoids mixing old and new outputs, reruns previously validated scopes, and updates the markdown trail.

---

## Test Prompt 4

> "Set up a smoke run first, then scale to the full experiment if the pipeline is clean."

Expected behavior: The agent recommends a staged workflow with smoke scope, fresh prefixes, observability artifacts, and promotion only after successful verification.

---

## Test Prompt 5

> "Document this investigation, monitor the run, and summarize the final metrics when it finishes."

Expected behavior: The agent creates a markdown investigation note before execution, monitors the run through durable artifacts, and reports the final metrics from summary outputs.
