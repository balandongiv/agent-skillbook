# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- No unreleased changes yet.

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
