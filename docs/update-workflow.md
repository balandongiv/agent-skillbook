# Agent Update Workflow

This document describes how an AI agent should safely update a skill. Follow these steps every time you modify a skill — whether you are a human contributor or an AI agent making automated updates.

Repository-specific defaults for `agent_skillbook/` also live in `AGENTS.md`. Agents should follow both this workflow and those local instructions.

---

## Why follow a workflow?

Skills have two representations: canonical files (the source) and exported files (generated for each platform). If you update one without the other, the skill becomes inconsistent. The workflow ensures everything stays in sync.

---

## Step-by-step update workflow

### Step 1: Identify the canonical file to change

Determine which canonical file needs updating:

- **Changing what the skill does** → edit `INSTRUCTIONS.md`
- **Adding or changing examples** → edit `EXAMPLES.md`
- **Changing metadata, routing, or config** → edit `skill.yaml`
- **Adding test prompts** → edit `TESTS.md`

Never start by editing exported files.

### Step 2: Edit the canonical file

Make your change in the appropriate canonical file. Keep changes focused — one concern per commit.

If changing `skill.yaml`:
- Verify the `summary` field still accurately describes the skill (see [description-writing-guide.md](description-writing-guide.md))
- Check that `when_to_use` and `when_not_to_use` are still accurate

If changing `INSTRUCTIONS.md`:
- Verify the instructions are still consistent with the examples in `EXAMPLES.md`
- Add a test prompt to `TESTS.md` if the change addresses a new case

### Step 3: Run validation

```bash
python -m agent_skillbook.cli validate
```

Validation will catch:
- Missing required files
- Missing required YAML fields
- Folder name not matching slug
- Missing or empty exports (will flag after you regenerate)

Fix any validation errors before proceeding.

### Step 4: Regenerate exports

Run the renderer for all platforms:

```bash
python -m agent_skillbook.cli render
```

Or render a specific skill only:

```bash
python tools/render_openai_skill.py skills/<slug>
python tools/render_claude_skill.py skills/<slug>
python tools/render_gemini_gem.py skills/<slug>
```

This will update:
- `exports/openai/SKILL.md`
- `exports/openai/agents/openai.yaml`
- `exports/claude/SKILL.md`
- `exports/gemini/GEM_INSTRUCTIONS.md`
- `exports/gemini/SETUP.md`

### Step 5: Run validation again

```bash
python -m agent_skillbook.cli validate
```

After regenerating, all exports should exist and be non-empty. Validation should now pass completely.

### Step 6: Run tests

```bash
pytest tests/ -v
```

All tests must pass. If a test fails:
- Investigate whether the test expectation is wrong or the skill content is wrong
- Fix the root cause, not just the test assertion

### Step 7: Update versioning metadata

For every change, update the skill's `CHANGELOG.md` under `## [Unreleased]`:

```markdown
## [Unreleased]

### Changed
- Clarified rule about side effects in helper functions

## [0.2.0] - YYYY-MM-DD

### Changed
- Updated INSTRUCTIONS.md to clarify rule about side effects
```

Also update the root `CHANGELOG.md` under `## [Unreleased]`.

`VERSION` is the canonical source of the repository version.

For normal agent-authored changes, bump the patch version:

```bash
python -m agent_skillbook.cli bump-version patch
```

If you already set `VERSION` manually and just need to synchronize the other files:

```bash
python -m agent_skillbook.cli sync-version
```

If the change is part of a release, keep the package version synchronized in all four places together:

- `VERSION`
- `pyproject.toml`
- `src/agent_skillbook/__init__.py`
- the status line in `README.md`

### Step 8: Run validation one more time

```bash
python -m agent_skillbook.cli validate
```

The validator now checks both skill changelog structure and repository version consistency against `VERSION`. Do not commit until it passes.

### Step 9: Commit

Commit all changed files together:

```bash
git add skills/<slug>/
git commit -m "skill(<slug>): update instructions for side effects clarity

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Include all canonical files and generated exports in the same commit. This makes it easy to see what changed and why.

---

## Quick reference

```
Edit canonical file
       ↓
agent-skillbook validate
       ↓
agent-skillbook render
       ↓
agent-skillbook validate (again)
       ↓
pytest tests/
       ↓
Update [Unreleased] changelog entries
       ↓
Sync release version files if needed
       ↓
agent-skillbook validate
       ↓
git commit
```

---

## What if the Gemini export changed?

If `GEM_INSTRUCTIONS.md` changed, you (or the user) will need to manually update the Gem in the Gemini UI. The export file contains the text to paste. See [docs/platforms/gemini-gems.md](platforms/gemini-gems.md) for instructions.
