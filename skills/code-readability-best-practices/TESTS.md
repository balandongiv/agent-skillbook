# Test Prompts: Code Readability Best Practices

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Please reorganize this file so the main function appears first and the helpers read top-down."

Expected behavior: The agent identifies the headline function, moves it near the top, and arranges helpers below it in call-flow order without changing behavior.

---

## Test Prompt 2

> "Review this module for readability and tell me whether the function order makes sense."

Expected behavior: The agent evaluates top-down structure, grouping by concern, helper proximity, and scanability, then explains concrete structural improvements.

---

## Test Prompt 3

> "Can you refactor these comments? They feel vague and noisy."

Expected behavior: The agent rewrites or removes vague comments, keeps only non-obvious context, and turns uncertainty into precise TODOs when needed.

---

## Test Prompt 4

> "This code works, but it is hard to follow because helpers are scattered everywhere."

Expected behavior: The agent preserves behavior while regrouping related helpers, separating layers naturally, and explaining the new organization in terms of readability.

---

## Test Prompt 5

> "Should this comment stay, or is it just repeating the code?"

Expected behavior: The agent checks whether the comment adds constraints, rationale, or caveats. If it only restates obvious code, the agent recommends deleting it.

---

## Test Prompt 6

> "Please clean up these HTML-style comments so they read well in code review and in the terminal."

Expected behavior: The agent converts markup-heavy comments into plain text, keeps the same intent, and removes decorative formatting that adds clutter.

