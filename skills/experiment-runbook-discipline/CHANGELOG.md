# Changelog: Experiment Runbook Discipline

All notable changes to this skill are documented here.

## [Unreleased]

### Added
- "Compute placement and concurrency (multi-agent / sandboxed runners)" section: sandboxed code-agents often
  cannot spawn OS process pools (silent GIL-bound stall) so heavy parallel sweeps must run orchestrator-side
  while the sub-agent authors code + does subprocess-only work; detect stalls via progress-file timestamp/delta
  not percent; never overlap browser/UI automation with full-core compute; one distinct live-status file per
  runner; smoke-test one real unit before the full sweep; verify the actual interpreter/environment used.

## [0.1.1] - 2026-03-19

### Changed
- Expanded the skill to require smallest-real-data smoke validation before broader promotion when the user asks for true pipeline readiness
- Added explicit guidance for tracking editable local dependencies as part of run logic and rerunning smoke scopes after dependency fixes
- Added examples and trigger prompts for real-data promotion and editable dependency revalidation

## [0.1.0] - 2026-03-18

### Added
- Initial version of experiment-runbook-discipline
- Core instructions for planning, launching, monitoring, and validating long-running experiments
- Examples covering observable runs, clean reruns after logic changes, and smoke-to-full promotion
- Test prompts for runbook and experiment-execution verification
