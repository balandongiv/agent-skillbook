# Agent Instructions for `agent_skillbook`

These instructions apply to any change inside `agent_skillbook/`.

## Versioning rule

`VERSION` is the canonical source of the repository version.

Never update these files independently by hand:

- `pyproject.toml`
- `src/agent_skillbook/__init__.py`
- `README.md`

Instead:

1. bump or set `VERSION`
2. run `python -m agent_skillbook.cli sync-version`

Or use:

- `python -m agent_skillbook.cli bump-version patch`
- `python -m agent_skillbook.cli bump-version minor`
- `python -m agent_skillbook.cli bump-version major`

Default rule for agent-authored changes:

- if you change anything under `agent_skillbook/`, bump at least the patch version unless the user explicitly asks not to bump it or explicitly requests a different semver level

## Changelog rule

For every change:

- update the relevant skill `CHANGELOG.md` under `## [Unreleased]` when a skill changed
- update the root `CHANGELOG.md` under `## [Unreleased]`

If you are cutting a new released version:

- move the relevant unreleased notes into a dated release section
- keep a fresh `## [Unreleased]` section at the top

## Skill update rule

If any canonical skill files changed:

- regenerate exports with `python -m agent_skillbook.cli render`

## Recurring preference capture rule

If a user repeats the same workflow preference, correction, validation standard, naming convention, or debugging style across multiple turns, do not rely on conversational memory alone.

Instead:

1. update an existing skill if the preference clearly belongs there
2. create a new skill if the preference is distinct and likely reusable across projects
3. update the relevant skill `CHANGELOG.md` and the root `CHANGELOG.md`
4. bump and sync the repository version metadata
5. regenerate exports and run validation before finishing

Examples of preferences that should be codified:

- IntelliJ-first debugging expectations
- real-data-first smoke and promotion rules
- implementation-aligned planning and naming contracts
- experiment runbook and observability discipline

## Validation rule

Before finishing:

- run `python -m agent_skillbook.cli validate`
- run `pytest tests/ -v`

Do not finish with version metadata, changelogs, or exports out of sync.
