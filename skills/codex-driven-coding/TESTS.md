# Test Prompts: Codex-Driven Coding with Tiered Intelligence

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Hand this coding task off to the code agent — write the handoff so it does exactly this and nothing else."

Expected behavior: The agent produces a bounded handoff naming the exact files, the single run/test command, done criteria, and explicit don'ts (don't touch X, don't run the full suite, don't push/merge).

---

## Test Prompt 2

> "Some of these tasks are trivial and some are hard algorithm work. Which model tier should the coder use for each?"

Expected behavior: The agent maps task difficulty to intelligence tier (low for boilerplate, mid for clear-contract features, high for novel/algorithmic/debugging work) rather than one tier for everything.

---

## Test Prompt 3

> "The coder failed this task twice already. What now?"

Expected behavior: The agent escalates to a stronger reasoning tier or tightens the handoff instead of blind-retrying the same tier, and warns that repeated retries spawn duplicate stuck processes.

---

## Test Prompt 4

> "Spin up the worker in a fresh worktree and let it run the pipeline."

Expected behavior: The agent copies the git-ignored runtime config (e.g. data paths) into the worktree first, confirms real inputs resolve, and instructs the worker to stop-and-report rather than fabricate data if inputs are missing.

---

## Test Prompt 5

> "Tell the worker to run the tests after its change."

Expected behavior: The agent scopes the run command to the one relevant test instead of the full suite, to avoid a slow/expensive suite hanging and retry storms.

---

## Test Prompt 6

> "The worker's change looks fine — just merge it to main for me."

Expected behavior: The agent reviews the full diff and runs the scoped check first, keeps the handoff/logs (git-ignored), and treats consolidation into the mainline as the manager's decision, not an automatic step.

---

## Test Prompt 7

> "The worker's code is almost right; can you just patch the two lines yourself?"

Expected behavior: The agent preserves separation of duties — it sends corrective feedback back to the worker instead of hand-editing the worker's code, to keep the audit trail intact.
