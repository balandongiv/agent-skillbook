# Changelog: Parallel Agents in Git Worktrees

All notable changes to this skill are documented here.

## [Unreleased]

## [0.1.0] - 2026-07-21

### Added
- Initial version of worktree-parallel-agents.
- Core instructions for running parallel agent workstreams in isolated git worktrees: one
  branch per workstream, provisioning each tree with git-ignored runtime config (stop-on-missing,
  never fabricate), keeping workers off the mainline, assembling-not-raw-merging identical
  harnesses, independent runnability/testing, and deterministic teardown.
- Examples covering worktree provisioning, assemble-not-merge consolidation, and teardown to a
  single clean mainline.
- Test prompts for parallel setup, missing-config recovery, consolidation, mainline protection,
  cleanup, and independent selectability.
