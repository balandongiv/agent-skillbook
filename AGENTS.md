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

## Validation rule

Before finishing:

- run `python -m agent_skillbook.cli validate`
- run `pytest tests/ -v`

Do not finish with version metadata, changelogs, or exports out of sync.
