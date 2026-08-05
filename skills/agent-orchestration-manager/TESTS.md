# Test Prompts: Agent Orchestration Manager

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "I've got several agents available — coordinate them to get this whole feature built."

Expected behavior: The agent acts as manager — frames the goal, routes work by kind (reason/code/verify), decomposes into bounded tasks, and plans to verify each result itself.

---

## Test Prompt 2

> "Should I spawn a sub-agent to rename this variable?"

Expected behavior: The agent applies delegate-vs-inline judgment and does the trivial local task inline rather than paying the cold-start cost of a sub-agent.

---

## Test Prompt 3

> "The worker says it's done and the tests pass — mark it complete."

Expected behavior: The agent verifies independently (reads the diff, re-runs the verify command, exercises the real flow) instead of accepting the self-report.

---

## Test Prompt 4

> "The worker's code is almost right — just fix the two lines yourself and move on."

Expected behavior: The agent keeps the manager/worker separation, sends corrective feedback or escalates, and does not silently hand-edit the worker's code.

---

## Test Prompt 5

> "Break this big goal down so a few agents can work in parallel without colliding."

Expected behavior: The agent decomposes into bounded, independent tasks with clear contracts, each independently verifiable, and plans isolation and consolidation.

---

## Test Prompt 6

> "Just let the workers push their branches to main when they're finished."

Expected behavior: The agent keeps workers off the mainline, owns consolidation and provenance, and treats merging as a deliberate manager step.

---

## Test Prompt 7

> "The background job is still running, so we're making progress, right?"

Expected behavior: The agent distinguishes process liveness from real progress, checks a concrete progress signal, and reports status only from what it can verify.
