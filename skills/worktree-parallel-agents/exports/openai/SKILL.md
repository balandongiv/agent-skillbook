---
name: worktree-parallel-agents
description: Run independent agent workstreams in isolated git worktrees — one branch per workstream, git-ignored runtime config (e.g. paths.yaml) copied into each tree, workers that never merge to the mainline — and consolidate later by assembling files rather than raw-merging.
---

# Parallel Agents in Git Worktrees

## Overview

When several coding agents work at once, they must not share one working tree — concurrent
edits collide and results become unattributable. Git **worktrees** give each workstream its
own checkout of the same repository on its own branch, so agents run truly in parallel. This
skill covers the discipline that makes that safe: one branch per workstream, provisioning each
tree with the git-ignored runtime config it needs, keeping workers off the mainline, and
consolidating at the end by **assembling files rather than raw-merging**.

## Core principles

1. **One worktree, one branch, one workstream.** Each agent gets its own worktree checked out
   to its own branch (`git worktree add ../ws-<name> -b agent/<area>/<name>`). Work stays
   isolated and every change is attributable to a branch.
2. **Provision each tree with git-ignored config.** A fresh worktree does **not** contain
   git-ignored files (data-path config, local settings). Copy them in before the agent runs.
   Skipping this is the classic failure: the worker can't resolve real inputs and silently
   fabricates substitutes. A worker that can't find real inputs must **stop, not synthesize**.
3. **Workers never merge to the mainline.** A worker commits only on its own branch. The
   mainline is protected; consolidation is a separate, deliberate step owned by the manager.
4. **Keep the harness single-source.** Shared infrastructure (event matching, metrics,
   evaluation) should be identical across branches — ideally branched from one base — so it is
   not re-implemented per workstream and consolidation stays trivial.
5. **Assemble, don't raw-merge, when shared files are identical.** If the shared harness is
   byte-identical across branches, bring each workstream's *unique* files onto the
   consolidation branch with `git checkout <branch> -- <paths>` instead of merging. This avoids
   conflicts and keeps history clean. Verify identity first (`git diff <a> <b> -- <shared>`).
6. **Independently runnable and testable.** Each workstream ships a thin runner and its own
   unit test so it can be selected and verified on its own after consolidation.
7. **Clean up deterministically.** After consolidation and push, remove the worktrees
   (`git worktree remove`) and delete the merged branches, leaving one mainline.

## Step-by-step process

1. **Create a worktree per workstream** on a fresh branch off the agreed base.
2. **Provision** each tree: copy git-ignored runtime config in; spot-check that real inputs
   resolve (counts look right).
3. **Run each agent** in its own tree; it commits only on its own branch and never pushes to
   the mainline.
4. **Verify identity of shared files** across branches before consolidating.
5. **Consolidate** on a dedicated branch: assemble unique files via `git checkout <branch> -- …`
   where shared files match; use a real merge only where they legitimately diverge.
6. **Document provenance** (branch-of-origin per file/module) and run the consolidated tests.
7. **Push the mainline, then tear down**: remove worktrees and delete the now-merged branches.

## Rules

- Always give each workstream its own worktree and branch; never share one working tree.
- Always copy git-ignored runtime config into each new worktree before the agent runs.
- A worker that cannot resolve real inputs must stop and report — never fabricate data.
- Never let a worker push to or merge into the mainline; consolidation is a separate step.
- Verify shared files are identical before assembling; assemble-not-merge only when they match.
- Always keep each workstream independently runnable and unit-tested.
- Always remove worktrees and delete merged branches after the mainline push.

## Common mistakes to avoid

- **Missing git-ignored config in a fresh worktree.** The agent can't find real data and
  fabricates synthetic inputs. Copy the config in first; require stop-on-missing.
- **Sharing one working tree across agents.** Concurrent edits collide and results become
  unattributable. One worktree per workstream.
- **Raw-merging identical harnesses.** Produces noisy conflicts for no reason. If shared files
  match, assemble unique files with `git checkout <branch> -- …`.
- **Workers pushing to the mainline.** Removes the manager's consolidation gate and can corrupt
  the protected branch. Keep workers on their own branches.
- **Forgetting teardown.** Stale worktrees and merged branches accumulate. Remove them after
  the push so the repo ends as a single clean mainline.
