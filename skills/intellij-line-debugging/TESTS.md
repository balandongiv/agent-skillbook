# Test Prompts: IntelliJ Line Debugging

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "I want to debug this pipeline line by line in IntelliJ IDEA from the file load until the merge."

Expected behavior: The agent narrows the scope, prefers a serial real-input path, and gives an explicit breakpoint order.

---

## Test Prompt 2

> "This script uses parallel workers and caching. Can you refactor it so I can right-click Debug in IntelliJ?"

Expected behavior: The agent proposes or creates a thin serial debug helper that preserves the production call order and avoids cache short-circuits.

---

## Test Prompt 3

> "Show me exactly where to Step Into the library code in PyCharm."

Expected behavior: The agent points to precise library call boundaries and mentions debugger settings that may skip library scripts.

---

## Test Prompt 4

> "I only want one subject and one parameter set so I can inspect every variable."

Expected behavior: The agent freezes scope aggressively, sets `jobs=1`, and recommends a smallest-real-input workflow.

---

## Test Prompt 5

> "Should we add a debug helper or just use the current entrypoint?"

Expected behavior: The agent chooses the simplest of direct entrypoint, direct instructions, or thin helper, and avoids unnecessary refactoring.

---

## Test Prompt 6

> "This package is installed editable from a local repo. Show me exactly where to Step Into it from IntelliJ and give me a debug script I can find easily."

Expected behavior: The agent identifies the editable dependency boundary, points to the local repo path, and prefers a reusable helper in `tutorials/` or an equally obvious IDE-facing location.
