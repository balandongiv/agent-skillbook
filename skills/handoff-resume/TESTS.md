# Test Prompts: Handoff Resume

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Read the handoff file and continue from there."

Expected behavior: The agent reads the handoff before acting, uses its pending tasks as the checklist, and updates the handoff as tasks complete.

---

## Test Prompt 2

> "Resume the work from `handoff/20260331_subject_performance_handoff.md`."

Expected behavior: The agent reads the named handoff, verifies process state if needed, and executes the listed unfinished tasks.

---

## Test Prompt 3

> "Continue from the last handoff and tick completed tasks yes."

Expected behavior: The agent treats the handoff as the source of truth and only changes `Done?` to `Yes` when concrete evidence exists.

---

## Test Prompt 4

> "Pick up the pending work from the handoff without rereading the whole chat."

Expected behavior: The agent prioritizes the handoff artifact over chat reconstruction and uses it to drive the resumed work.

---

## Test Prompt 5

> "Use the handoff as the checklist and update it as you finish each item."

Expected behavior: The agent keeps the handoff synchronized with actual progress and preserves the historical record while adding new evidence.
