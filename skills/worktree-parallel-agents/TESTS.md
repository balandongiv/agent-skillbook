# Test Prompts: Parallel Agents in Git Worktrees

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Set up four coding agents to work in parallel on this repo without stepping on each other."

Expected behavior: The agent creates one git worktree per workstream on its own branch, keeps them isolated, and plans consolidation as a separate step.

---

## Test Prompt 2

> "The agent in the new worktree is producing garbage numbers on almost no data."

Expected behavior: The agent recognizes the missing git-ignored runtime config, copies it into the worktree, confirms real inputs resolve, and requires stop-on-missing instead of fabricated data.

---

## Test Prompt 3

> "Merge all eight algorithm branches into main."

Expected behavior: The agent verifies whether the shared harness is byte-identical, then assembles each branch's unique files with `git checkout <branch> -- ...` rather than raw-merging when the shared files match.

---

## Test Prompt 4

> "Can the workers just push their branches to main when they're done?"

Expected behavior: The agent keeps workers off the mainline, has them commit only on their own branches, and reserves consolidation as a manager-owned step.

---

## Test Prompt 5

> "We're done — clean up the repo."

Expected behavior: The agent pushes the mainline, removes the worktrees, deletes the merged branches, and prunes so the repo ends as a single clean mainline.

---

## Test Prompt 6

> "Each algorithm should still be runnable and testable on its own after we combine them."

Expected behavior: The agent ensures every workstream ships a thin runner and its own unit test so it stays independently selectable and verifiable after consolidation.
