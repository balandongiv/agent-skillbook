# Test Prompts: Implementation-Aligned Planning

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "This planning document is outdated. Rewrite it so it matches the code."

Expected behavior: The agent inspects the implementation, treats code as the source of truth for concrete behavior, and rewrites the doc into a clear stage contract and execution map.

---

## Test Prompt 2

> "The plan is half baked. Turn it into something I can use to navigate the repository."

Expected behavior: The agent restructures the doc into contracts, module maps, execution flow, checks, failure modes, pseudocode, and debug navigation.

---

## Test Prompt 3

> "If the implementation changed, update the flowchart and folder docs too."

Expected behavior: The agent synchronizes the stage doc with related shared planning docs instead of editing only one file.

---

## Test Prompt 4

> "There is a conflict between the old plan and the actual code. Which one should we trust?"

Expected behavior: The agent uses code and config as the source of truth for concrete implemented behavior, preserves intent separately, and documents the resolution explicitly.

---

## Test Prompt 5

> "Make this stage plan explain exactly what files are read and written, and where to debug first."

Expected behavior: The agent adds a precise folder contract, execution flow, and debugging path rather than leaving the plan at a high level.

---

## Test Prompt 6

> "Rewrite this planning doc so it explains the column naming rules, the Excel source of truth, the normalized parquet cache, and which tutorial script I should debug."

Expected behavior: The agent documents naming contracts, source-versus-cache relationships, and the human-facing debug entrypoint alongside the execution flow.
