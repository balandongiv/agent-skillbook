# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- No unreleased changes yet.

## [0.1.5] - 2026-03-31

### Added
- New canonical skills: `handoff`, `handoff-resume`, `subject-outlier-review`, and `manuscript-results-curation`
- Canonical guidance for operational handoff creation, handoff-driven resume workflows, subject-level outlier review, and direct manuscript result curation

### Changed
- Migrated the repository-local workflow skills from `.codex/skills/` into canonical `agent_skillbook/skills/` entries
- Regenerated skill exports so OpenAI-facing metadata is emitted from the canonical skillbook schema, including `exports/openai/SKILL.md` and `exports/openai/agents/openai.yaml`

## [0.1.4] - 2026-03-19

### Added
- New starter skill: `real-data-validation-promotion`
- Agent rule in `AGENTS.md` requiring repeated user preferences and corrections to be captured in existing or new skills instead of relying on conversational memory

### Changed
- Expanded `intellij-line-debugging` to cover tutorial-style debug helper placement and stepping into editable local dependencies
- Expanded `implementation-aligned-planning` to require naming contracts, source-versus-cache documentation, and human-facing debug entrypoints
- Expanded `experiment-runbook-discipline` to emphasize smallest-real-data smoke validation, staged promotion, and editable dependency revalidation
- Updated skillbook README and contributing docs to reflect recurring-preference capture as part of normal skill maintenance

## [0.1.3] - 2026-03-18

### Added
- New starter skill: `intellij-line-debugging`
- New starter skill: `implementation-aligned-planning`
- New starter skill: `experiment-runbook-discipline`
- New starter skill: `hyperparameter-search-strategy`
- Canonical root `VERSION` file for repository version management
- `agent_skillbook/AGENTS.md` with agent-facing rules for changelog and version updates
- CLI command: `python -m agent_skillbook.cli sync-version`
- CLI command: `python -m agent_skillbook.cli bump-version [patch|minor|major]`
- Beginner and contributor docs for the canonical `VERSION` workflow and agent-facing auto-bump rules
- Regression coverage for canonical `VERSION` synchronization and version bump helpers

### Changed
- Canonical guidance for planning, monitoring, and documenting long-running experiments with fresh prefixes, live status artifacts, and post-run metric checks
- Canonical guidance for choosing efficient hyperparameter search methods and avoiding unjustified brute-force grid search
- Fixed `python -m agent_skillbook.cli render` so it renders every canonical skill when no explicit target is provided.
- Repository version validation now treats `VERSION` as the canonical source and requires `pyproject.toml`, `src/agent_skillbook/__init__.py`, and `README.md` to match it
- Contributor and workflow docs now instruct agents to bump or sync version metadata through the CLI helpers rather than editing version strings independently

### Fixed
- CLI render workflow regression when invoking `python -m agent_skillbook.cli render` from the repo-local package path

## [0.1.2] - 2026-03-17

### Added
- New starter skill: `code-readability-best-practices`
- New starter skill: `python-class-and-filename`
- Canonical guidance for top-down function organization, helper grouping, and comment cleanup without changing behavior
- Canonical guidance for choosing when to use a Python class, matching it to a responsibility-based module filename, and avoiding vague module names
- Validation now checks synchronized repository version metadata and requires `## [Unreleased]` sections in skill changelogs
- Contributor and agent workflow docs now spell out when to update unreleased changelog entries versus when to bump release versions

## [0.1.0] - 2024-01-01

### Added
- Initial repository structure with canonical skill format
- Three starter skills: `good-function-design`, `good-description-writing`, `repo-readme-writing`
- Python package `agent_skillbook` with registry, models, validators, and CLI
- Export templates for OpenAI Codex, Claude Code, and Gemini Gems
- Beginner documentation in `docs/`
- Contribution guidelines
- GitHub Actions workflow for validation and testing
