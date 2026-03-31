# Beginner Guide to agent-skillbook

Welcome! This guide explains what this repository is, how it works, and how to get started in your first 30 minutes.

---

## What is a skill?

A **skill** is a set of instructions you give to an AI agent (like ChatGPT, Claude, or Gemini) so it knows how to handle a specific type of task.

Think of it like this: if you hire a contractor, you might hand them a checklist of your standards — "always use these materials, always check these things". A skill is that checklist, but for an AI agent.

For example, a skill called `good-function-design` tells an AI agent: "When the user asks you to write or review a Python function, apply these rules: keep it small, use descriptive names, one responsibility per function…"

---

## How this repository is structured

```
agent-skillbook/
├── skills/                  ← The actual skills (source of truth)
│   ├── good-function-design/
│   │   ├── skill.yaml       ← Metadata and routing config
│   │   ├── INSTRUCTIONS.md  ← What the agent should do
│   │   ├── EXAMPLES.md      ← Before/after examples
│   │   ├── TESTS.md         ← Test prompts to verify the skill
│   │   ├── CHANGELOG.md     ← History of changes to this skill
│   │   ├── resources/       ← Extra notes and references
│   │   └── exports/         ← Auto-generated files for each platform
│   │       ├── openai/
│   │       ├── claude/
│   │       └── gemini/
│   └── ...
├── docs/                    ← Guides like this one
├── templates/               ← Blank templates for creating new skills
├── tools/                   ← Python scripts for validation and rendering
├── src/agent_skillbook/     ← Python package with CLI
├── VERSION                  ← Canonical repository version source
├── AGENTS.md                ← Agent-facing workflow rules for versioning and changelogs
└── tests/                   ← Automated tests
```

Each skill lives in its own folder under `skills/`. Every skill has the same structure — a predictable format that makes skills easy to read, validate, and export to different AI platforms.

---

## First 30 minutes: setup guide

### Step 1: Clone the repository

```bash
git clone https://github.com/balandongiv/agent-skillbook.git
cd agent-skillbook
```

### Step 2: Install the Python package

You need Python 3.9 or higher. Check your version:

```bash
python --version
```

Install the package in editable mode (so changes you make are reflected immediately):

```bash
pip install -e ".[dev]"
```

This installs:
- The `agent-skillbook` command-line tool
- `PyYAML` for reading skill files
- `pytest` for running tests

### Step 3: List all skills

```bash
agent-skillbook list
```

Or, if the command is not in your PATH:

```bash
python -m agent_skillbook.cli list
```

You should see output like:

```
Found 9 skill(s):

  code-readability-best-practices
    Title:   Code Readability Best Practices
    Summary: Review and refactor code for top-down readability...

  experiment-runbook-discipline
    Title:   Experiment Runbook Discipline
    Summary: Plan, launch, monitor, and document long-running experiments...

  good-function-design
    Title:   Good Function Design
    Summary: Write small, readable, testable Python functions...

  hyperparameter-search-strategy
    Title:   Hyperparameter Search Strategy
    Summary: Choose efficient hyperparameter search strategies...

  ...
```

### Step 4: Validate all skills

```bash
agent-skillbook validate
```

All skills should pass validation. You should see:

```
  OK  code-readability-best-practices
  OK  experiment-runbook-discipline
  OK  good-function-design
  OK  hyperparameter-search-strategy
  ...

All skills valid. Version metadata is consistent.
```

The validator checks both the skill files and the repository version metadata. `VERSION` is the canonical source, and the package metadata in `pyproject.toml`, `src/agent_skillbook/__init__.py`, and the README status line must match it.

### Step 5: Explore a skill

Open any skill directory and read through it:

```bash
cat skills/good-function-design/skill.yaml
cat skills/good-function-design/INSTRUCTIONS.md
```

### Step 6: Run the tests

```bash
pytest tests/ -v
```

All tests should pass.

### Step 7: Learn the versioning workflow

If you change anything under `agent_skillbook/`, do not manually edit version strings in multiple places. Use the CLI helpers:

```bash
python -m agent_skillbook.cli bump-version patch
# or
python -m agent_skillbook.cli sync-version
```

The agent-facing default rule for this repository lives in `AGENTS.md`: normal `agent_skillbook/` edits should bump at least the patch version unless a user explicitly asks for a different behavior.

---

## What to do next

- Read [what-is-a-skill.md](what-is-a-skill.md) to understand the canonical format in detail
- Read [skill-writing-guide.md](skill-writing-guide.md) to learn how to write good skills
- Read the [CONTRIBUTING.md](../CONTRIBUTING.md) guide to create your own skill
