# Test Prompts: Subject Outlier Review

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "I think one subject is dragging down performance. Find the outlier."

Expected behavior: The agent performs a subject-level comparison, ranks subjects, and identifies the weakest candidate with supporting evidence.

---

## Test Prompt 2

> "Should we drop a subject from the final result?"

Expected behavior: The agent evaluates whether exclusion is justified, not justified, or still unproven, and avoids silent removal.

---

## Test Prompt 3

> "Show me each subject's performance and tell me which one is the problem."

Expected behavior: The agent produces a subject-by-subject table and explains the weakest and strongest cases.

---

## Test Prompt 4

> "Compare full-cohort versus filtered-cohort subject behavior before we decide to exclude anyone."

Expected behavior: The agent insists on an explicit exclusion workflow and distinguishes hard subjects from invalid ones.

---

## Test Prompt 5

> "This run feels like it has a bad subject in it. Review whether exclusion is actually defensible."

Expected behavior: The agent uses concrete run artifacts, checks support and imbalance, and states what evidence would justify or block exclusion.
