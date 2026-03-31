# Test Prompts: Handoff

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Create a handoff note for this repo so another agent can continue later."

Expected behavior: The agent writes a markdown file under `handoff/` with the required sections and an explicit pending-work table.

---

## Test Prompt 2

> "Document what has been done, what was stopped, and what is still pending."

Expected behavior: The agent separates completed work from stopped work and records pending tasks in `Task | Done? | Evidence / Next step` format.

---

## Test Prompt 3

> "Make me a transfer summary with the exact logs and commands the next session will need."

Expected behavior: The agent writes an operational handoff with exact file paths, log paths, and suggested next commands.

---

## Test Prompt 4

> "Write a resume markdown for this interrupted experiment run."

Expected behavior: The agent inspects the current repository and process state, then produces a handoff that makes the interrupted run easy to resume.

---

## Test Prompt 5

> "Create a handoff note and say whether any background terminals are still running."

Expected behavior: The agent checks relevant process state and records whether long-running commands are active, finished, or manually stopped.
