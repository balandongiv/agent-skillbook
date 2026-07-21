# Changelog: Codex-Driven Coding with Tiered Intelligence

All notable changes to this skill are documented here.

## [Unreleased]

## [0.1.0] - 2026-07-21

### Added
- Initial version of codex-driven-coding.
- Core instructions for delegating code changes to an autonomous coding agent at a
  task-matched intelligence tier, with a separate planning/verifying manager: bounded written
  handoffs, tier selection by difficulty, escalate-don't-blind-retry, environment provisioning
  with stop-on-missing (no fabricated data), scoped run commands, and diff review with kept
  provenance.
- Examples covering bounded vs vague delegation, tier matching with escalation, and
  provisioning the environment so the worker cannot fabricate data.
- Test prompts for handoff writing, tier selection, escalation, provisioning, scoped runs,
  manager-owned consolidation, and separation of duties.
