# Changelog: Agent Orchestration Manager

All notable changes to this skill are documented here.

## [Unreleased]

## [0.1.0] - 2026-07-21

### Added
- Initial version of agent-orchestration-manager.
- Core instructions for acting as the manager of a multi-agent workflow: route by kind of work
  (reason/code/verify), delegate-vs-inline judgment, decompose into bounded independent tasks,
  specify-don't-hope task specs with environment provisioning, verify every worker's output
  yourself (never trust the report), stay-the-manager (no silent hand-edits), own the mainline
  and consolidation, and report truthfully. Positioned as the umbrella over codex-driven-coding,
  worktree-parallel-agents, and chatgpt-ui-reasoning.
- Examples covering delegate-vs-inline judgment, verifying instead of trusting a report, and
  staying the manager rather than doing the worker's job.
- Test prompts for coordination, delegation judgment, independent verification, role separation,
  parallel decomposition, mainline ownership, and progress-vs-liveness.
