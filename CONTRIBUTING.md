# Contributing Guide

Thank you for contributing to **agent-skillbook**! This guide explains the rules and workflows for adding or modifying skills.

---

## Table of Contents

- [How to create a new skill](#how-to-create-a-new-skill)
- [How to edit an existing skill](#how-to-edit-an-existing-skill)
- [Golden rule: canonical files first](#golden-rule-canonical-files-first)
- [Adding examples](#adding-examples)
- [Adding test prompts for bugs](#adding-test-prompts-for-bugs)
- [Updating CHANGELOG.md](#updating-changelogmd)
- [How to run validation](#how-to-run-validation)
- [How to run tests](#how-to-run-tests)
- [Code style](#code-style)

---

## How to create a new skill

If a repeated user preference or correction does not fit cleanly into an existing skill, create a new skill for it instead of relying on conversational memory.

1. **Pick a slug.** Use lowercase kebab-case (e.g. `my-new-skill`). The slug must be unique.

2. **Create the skill directory:**
   ```
   skills/my-new-skill/
   ```

3. **Copy the canonical template:**
   ```bash
   cp -r templates/canonical-skill/* skills/my-new-skill/
   ```

4. **Fill in `skill.yaml`** with real values. Every field is required:
   - `slug` — must match the folder name
   - `title` — human-readable name
   - `summary` — one clear sentence (this becomes the routing trigger)
   - `when_to_use` — list of situations
   - `when_not_to_use` — list of situations
   - `tags` — list of relevant keywords
   - `invocation` — auto/explicit flags
   - `platform_overrides` — per-platform config

5. **Write `INSTRUCTIONS.md`.** This is the core content of the skill. Be detailed. Aim for at least 200 words. Write as if you are giving instructions to an AI agent.

6. **Write `EXAMPLES.md`.** Include at least two before/after examples showing the skill applied in practice.

7. **Write `TESTS.md`.** Include at least five test prompts — natural language phrases that should trigger this skill when typed into an AI agent.

8. **Write `CHANGELOG.md`.** Start with an `## [Unreleased]` section, then add `## [0.1.0] - YYYY-MM-DD` and a note about the initial version.

9. **Add `resources/notes.md`** with any reference links, research notes, or extra context.

10. **Generate exports:**
    ```bash
    python -m agent_skillbook.cli render
    ```
    This creates `exports/openai/SKILL.md`, `exports/claude/SKILL.md`, and `exports/gemini/GEM_INSTRUCTIONS.md`.

11. **Run validation:**
    ```bash
    python -m agent_skillbook.cli validate
    ```
    All checks must pass.

12. **Run tests:**
    ```bash
    pytest tests/ -v
    ```

13. **Update the root `CHANGELOG.md`** to document your new skill.

14. **Open a pull request.**

---

## How to edit an existing skill

If the same preference or correction has appeared multiple times, prefer updating the relevant skill so future agents inherit it automatically.

1. **Always edit the canonical files first.** The canonical files are:
   - `skills/<slug>/skill.yaml`
   - `skills/<slug>/INSTRUCTIONS.md`
   - `skills/<slug>/EXAMPLES.md`
   - `skills/<slug>/TESTS.md`
   - `skills/<slug>/CHANGELOG.md`
   - `skills/<slug>/resources/notes.md`

2. **After editing canonical files, regenerate exports:**
   ```bash
   python tools/render_openai_skill.py skills/<slug>
   python tools/render_claude_skill.py skills/<slug>
   python tools/render_gemini_gem.py skills/<slug>
   ```
   Or all at once:
   ```bash
   python -m agent_skillbook.cli render
   ```

3. **Validate and test** before committing.

4. **Update `CHANGELOG.md`** in the skill directory under `## [Unreleased]`, and update the root `CHANGELOG.md` under `## [Unreleased]` as well.

5. **Version metadata uses `VERSION` as the canonical source.**
   - for normal agent-authored updates, bump at least the patch version:
     ```bash
     python -m agent_skillbook.cli bump-version patch
     ```
   - to sync existing metadata from `VERSION` without changing the semantic version:
     ```bash
     python -m agent_skillbook.cli sync-version
     ```
   - do not edit `pyproject.toml`, `src/agent_skillbook/__init__.py`, and the README version line independently

---

## Golden rule: canonical files first

> **Never edit the generated exports directly.**

The files under `exports/` are auto-generated. If you edit them manually, your changes will be overwritten the next time someone runs the renderer.

If you absolutely must make a temporary edit to an export (for example, to test something quickly in the Gemini UI), always:
- Add a comment in your commit message explaining why
- Go back and make the real change in the canonical files immediately after

---

## Adding examples

Every new behavior added to a skill should have a corresponding before/after example in `EXAMPLES.md`. Examples help both humans understand the skill and AI agents learn from concrete demonstrations.

Format:
```markdown
## Example N: Short Title

### Before (without this skill)

[bad or naive approach]

### After (with this skill applied)

[correct approach]

### Why it's better

[brief explanation]
```

---

## Adding test prompts for bugs

If you find a bug where a skill triggers incorrectly or fails to trigger:
1. Write a test prompt that reproduces the issue — add it to `TESTS.md`
2. Fix the canonical files to address it
3. Note the fix in `CHANGELOG.md`

This ensures the bug cannot regress silently.

---

## Updating CHANGELOG.md

Every pull request that changes a skill **must** update both:
- The skill's own `CHANGELOG.md` (under `skills/<slug>/`)
- The root `CHANGELOG.md`

For normal in-progress work, add entries under `## [Unreleased]`.
When you cut a release, move the unreleased notes into a dated semantic version section and keep `VERSION`, `pyproject.toml`, `src/agent_skillbook/__init__.py`, and `README.md` synchronized.

Follow the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format:
```markdown
## [Unreleased]

### Changed
- Clarified routing examples for a new edge case

## [0.2.0] - YYYY-MM-DD

### Changed
- Updated instructions to clarify X
```

---

## How to run validation

```bash
# Validate all skills
python -m agent_skillbook.cli validate

# Or run the validation script directly
python tools/validate_skills.py
```

Validation checks:
- Folder name is lowercase kebab-case
- `skill.yaml` exists and has all required fields
- `INSTRUCTIONS.md`, `EXAMPLES.md`, `TESTS.md`, `CHANGELOG.md` exist
- Each skill `CHANGELOG.md` has an `## [Unreleased]` section and at least one semantic-version release heading
- All exports exist and are not empty
- `VERSION`, `pyproject.toml`, `src/agent_skillbook/__init__.py`, and `README.md` agree on the current package version

---

## How to run tests

```bash
# Install the package in editable mode first
pip install -e ".[dev]"

# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_validation.py -v
```

---

## Code style

- Python: follow PEP 8 conventions
- Use type hints on all function signatures
- Keep functions small and focused (see the `good-function-design` skill!)
- Write docstrings for all public functions and modules
- YAML: use 2-space indentation
- Markdown: use ATX-style headings (`##` not underline style)
- Keep lines under 100 characters where possible
