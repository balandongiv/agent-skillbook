# agent-skillbook

**Reusable custom skills for agents, with templates and guides.**

Status: Active | Version: 0.2.2 | License: MIT | Python: >=3.9

---

## What is this?

**agent-skillbook** is a repository of reusable skills for AI agents (ChatGPT/OpenAI Codex, Claude Code, Gemini Gems). Each skill is a set of structured instructions that teaches an agent how to handle a specific type of task — for example, how to write a good Python function, how to write a clear README, or how to craft precise routing descriptions.

Skills are stored in a **canonical format** that is platform-independent. From each skill, the repository generates platform-specific exports for OpenAI, Claude, and Gemini. You edit the canonical files, run one command, and all exports update automatically.

This repository is designed to be cloned, extended, and customized. Add your own skills, modify existing ones, and use the validation and rendering tools to keep everything consistent.

When a workflow preference keeps recurring, the preferred maintenance path is to capture it in an existing skill or add a new skill instead of relying on conversational memory alone.

---

## Why does it exist?

AI agents are only as good as the instructions they are given. But writing good agent instructions is surprisingly hard — they need to be specific enough to trigger accurately, detailed enough to produce consistent results, and maintainable enough to update over time.

This repository provides:
- A proven format for structuring agent skills
- Starter skills you can use or learn from
- Tools for validating and exporting skills to multiple platforms
- Documentation on what makes skills work well

---

## Who is it for?

- Developers who use AI agents (OpenAI, Claude, Gemini) in their daily workflow
- Teams that want a shared library of agent skills they can reuse and maintain
- Anyone who wants to learn how to write better instructions for AI agents
- Contributors who want to add skills to the public library

---

## Repository structure

```
agent-skillbook/
├── skills/                          ← Canonical skill files (source of truth)
│   ├── good-function-design/
│   │   ├── skill.yaml               ← Metadata, routing config, platform settings
│   │   ├── INSTRUCTIONS.md          ← What the agent should do
│   │   ├── EXAMPLES.md              ← Before/after examples
│   │   ├── TESTS.md                 ← Test prompts to verify the skill
│   │   ├── CHANGELOG.md             ← History of changes
│   │   ├── resources/               ← Extra notes and references
│   │   └── exports/                 ← Auto-generated platform exports
│   │       ├── openai/
│   │       │   ├── SKILL.md
│   │       │   └── agents/
│   │       │       └── openai.yaml
│   │       ├── claude/
│   │       │   └── SKILL.md
│   │       └── gemini/
│   │           ├── GEM_INSTRUCTIONS.md
│   │           └── SETUP.md
│   ├── code-readability-best-practices/
│   ├── good-description-writing/
│   ├── python-class-and-filename/
│   └── repo-readme-writing/
├── docs/                            ← Guides and documentation
│   ├── beginner-guide.md
│   ├── what-is-a-skill.md
│   ├── skill-writing-guide.md
│   ├── description-writing-guide.md
│   ├── update-workflow.md
│   └── platforms/
│       ├── openai-codex.md
│       ├── claude-code.md
│       └── gemini-gems.md
├── templates/                       ← Blank templates for new skills
├── tools/                           ← Python scripts for validation and rendering
├── src/agent_skillbook/             ← Python package with CLI
├── tests/                           ← Automated tests
├── VERSION                          ← Canonical repository version source
├── AGENTS.md                        ← Agent-facing update rules for versioning, changelogs, and validation
├── pyproject.toml
└── CONTRIBUTING.md
```

---

## How the canonical format works

Each skill is a folder under `skills/` with five required files:

| File | Purpose |
|---|---|
| `skill.yaml` | Slug, title, summary (routing trigger), tags, platform config |
| `INSTRUCTIONS.md` | Detailed instructions the agent follows |
| `EXAMPLES.md` | Before/after examples showing the skill in action |
| `TESTS.md` | Test prompts to verify the skill triggers correctly |
| `CHANGELOG.md` | History of all changes to this skill |

The `exports/` folder inside each skill is **auto-generated**. Never edit it directly. Always edit the canonical files and regenerate.

---

## How OpenAI, Claude, and Gemini differ

### OpenAI Codex

OpenAI Codex reads the `description` field from `exports/openai/SKILL.md` and uses it to automatically match the skill to relevant user messages. No manual invocation is needed — the agent routes to the skill automatically when the user's message semantically matches the description.

The `exports/openai/agents/openai.yaml` file provides the agent definition for use with the OpenAI Assistants API or custom GPTs.

See [docs/platforms/openai-codex.md](docs/platforms/openai-codex.md) for details.

### Claude Code

Claude Code uses `exports/claude/SKILL.md` similarly — it reads the `description` field and auto-routes based on semantic matching. Claude's export format includes additional fields (`disable-model-invocation`, `user-invocable`, `allowed-tools`) that are specific to Claude's behavior.

Users can also invoke skills explicitly by name when `user-invocable: true` is set.

See [docs/platforms/claude-code.md](docs/platforms/claude-code.md) for details.

### Gemini Gems

**Gemini Gems require manual setup through the Gemini web UI.** There is no API for creating Gems programmatically. This repository provides:
- `exports/gemini/GEM_INSTRUCTIONS.md` — the text to paste into the Gem UI
- `exports/gemini/SETUP.md` — a step-by-step guide for creating the Gem

Because Gemini Gems are manually selected (not auto-routed), you choose the Gem before starting a conversation.

See [docs/platforms/gemini-gems.md](docs/platforms/gemini-gems.md) for details.

---

## Installation

You need Python 3.9 or higher.

```bash
# Clone the repository
git clone https://github.com/balandongiv/agent-skillbook.git
cd agent-skillbook

# Install in editable mode (includes dev dependencies)
pip install -e ".[dev]"
```

Verify the installation:

```bash
agent-skillbook list
```

---

## CLI commands

### List all skills

```bash
agent-skillbook list
# or
python -m agent_skillbook.cli list
```

Output:
```
Found 10 skill(s):

  code-readability-best-practices
    Title:   Code Readability Best Practices
    Summary: Review and refactor code for top-down readability by reorganizing functions...
    Tags:    readability, refactoring, code-review, comments, maintainability

  experiment-runbook-discipline
    Title:   Experiment Runbook Discipline
    Summary: Plan, launch, monitor, and document long-running experiments...
    Tags:    experimentation, validation, runbook, monitoring, logging, reproducibility

  good-function-design
    Title:   Good Function Design
    Summary: Write small, readable, testable Python functions with clear names...
    Tags:    python, functions, readability, testing

  hyperparameter-search-strategy
    Title:   Hyperparameter Search Strategy
    Summary: Choose efficient hyperparameter search strategies for finding optimal parameter sets...
    Tags:    hyperparameter-search, optimization, tuning, experimentation, bayesian-optimization, random-search

  good-description-writing
    ...
```

### Validate all skills

```bash
agent-skillbook validate
# or
python -m agent_skillbook.cli validate
```

Checks that all skills have required files, valid YAML fields, and up-to-date exports.

### Regenerate all exports

```bash
agent-skillbook render
# or
python -m agent_skillbook.cli render
```

Runs all three renderers (OpenAI, Claude, Gemini) for all skills.

### Show a specific skill

```bash
agent-skillbook show good-function-design
```

---

## How to create a new skill

1. **Create a new folder** under `skills/` using a lowercase kebab-case name:
   ```bash
   mkdir -p skills/my-new-skill/resources
   ```

2. **Copy the template:**
   ```bash
   cp -r templates/canonical-skill/* skills/my-new-skill/
   ```

3. **Fill in `skill.yaml`** with your skill's metadata. The `summary` field is the routing trigger — write it carefully. See the [description writing guide](docs/description-writing-guide.md).

4. **Write `INSTRUCTIONS.md`** with detailed, actionable instructions (aim for 200+ words).

5. **Write `EXAMPLES.md`** with at least two before/after examples.

6. **Write `TESTS.md`** with at least five test prompts.

7. **Generate exports:**
   ```bash
   agent-skillbook render
   ```

8. **Validate:**
   ```bash
   agent-skillbook validate
   ```

9. **Run tests:**
   ```bash
   pytest tests/ -v
   ```

10. **Update changelogs and versioning metadata:**
    - Add an entry to the skill's `CHANGELOG.md` under `## [Unreleased]`
    - Add an entry to the root `CHANGELOG.md` under `## [Unreleased]`
    - Bump or synchronize the repository version with:
      ```bash
      python -m agent_skillbook.cli bump-version patch
      # or
      python -m agent_skillbook.cli sync-version
      ```

11. **Commit all files** — canonical files and generated exports together.

### Versioning helpers

```bash
agent-skillbook sync-version
# or
python -m agent_skillbook.cli sync-version
```

Synchronizes `pyproject.toml`, `src/agent_skillbook/__init__.py`, and the README status line from the canonical `VERSION` file.

### Bump the repository version

```bash
agent-skillbook bump-version patch
# or
python -m agent_skillbook.cli bump-version patch
```

Available bump levels are `patch`, `minor`, and `major`.

---

## How to update a skill

1. Edit the canonical file (never edit exports directly)
2. If the change comes from a repeated user preference or correction, decide whether it belongs in the existing skill or should become a new reusable skill
3. Regenerate: `agent-skillbook render`
4. Validate: `agent-skillbook validate`
5. Test: `pytest tests/ -v`
6. Update `CHANGELOG.md` in the skill directory
7. Bump or sync the repository version with the CLI helpers
8. Commit

### Versioning policy

Treat versioning in two layers:

- **Every change:** record it under the relevant `## [Unreleased]` section in the skill changelog and the root `CHANGELOG.md`
- **Every release:** keep `VERSION`, `pyproject.toml`, `src/agent_skillbook/__init__.py`, and the README status line synchronized

`VERSION` is the canonical source. Use:

```bash
python -m agent_skillbook.cli bump-version patch
# or
python -m agent_skillbook.cli sync-version
```

`agent_skillbook/AGENTS.md` tells agents to bump at least the patch version for any `agent_skillbook/` change unless the user explicitly requests a different semver level or no version bump.

The validator checks that `VERSION`, `pyproject.toml`, `src/agent_skillbook/__init__.py`, and the README status line stay synchronized, and that each skill changelog includes an `## [Unreleased]` section. This makes agents and contributors aware of versioning expectations before a change is committed.

Full workflow details: [docs/update-workflow.md](docs/update-workflow.md)

---

## Writing good descriptions

The `summary` field in `skill.yaml` is the **routing trigger** for OpenAI and Claude. It determines whether the agent activates a skill for a given user message.

**Bad description:**
> "Helps with Python functions."

**Good description:**
> "Write small, readable, testable Python functions with clear names and explicit inputs and outputs."

Rules:
- Start with a verb (Write, Review, Refactor, Generate…)
- Name the specific output (a Python function, a README, a skill description)
- Include context about when it applies
- Avoid filler words: handles, manages, deals with, helps with

Full guide: [docs/description-writing-guide.md](docs/description-writing-guide.md)

---

## Starter skills

This repository includes ten starter skills to demonstrate the format and provide immediate value:

### `code-readability-best-practices`
Teaches agents how to review or refactor code so it reads top-down and stays easy to scan. Covers: headline-first function ordering, grouping helpers by concern, keeping related functions close together, rewriting vague comments, removing stale comment history, and replacing markup-heavy comments with plain text.

### `experiment-runbook-discipline`
Teaches agents how to plan, launch, monitor, and document long-running experiments or validation sweeps. Covers: creating markdown investigation notes before a run, choosing fresh experiment prefixes, keeping rolling logs and live status artifacts, verifying real progress, checking final summary outputs, and rerunning validated scopes after logic changes.

### `good-function-design`
Teaches agents how to write Python functions that are small, readable, and testable. Covers: single responsibility, descriptive naming, explicit parameters, pure functions, docstrings, and common antipatterns (god functions, mutable defaults).

### `good-description-writing`
Teaches agents how to write routing-optimized descriptions for skills, tools, and functions. Critical for AI agent systems where the description is the primary routing signal. Covers the description formula, bad vs good examples, and testing descriptions.

### `hyperparameter-search-strategy`
Teaches agents how to choose efficient search methods for tuning detector, model, or experiment parameters. Covers: random search as the default large-space baseline, when Bayesian optimization is worth it, when to use successive halving or Hyperband, when evolutionary methods fit irregular spaces, when population-based training is appropriate, and when exhaustive enumeration is still justified.

### `implementation-aligned-planning`
Teaches agents how to turn ambiguous, stale, or half-baked planning documents into implementation-aligned engineering documents. Covers: using code and config as the source of truth for concrete behavior, rewriting stages into explicit contracts and execution flows, synchronizing flowcharts and folder docs, and keeping unresolved ambiguity visible instead of hand-waving it away.

### `intellij-line-debugging`
Teaches agents how to prepare line-by-line IntelliJ IDEA or PyCharm debugging workflows for real code paths. Covers: shrinking scope to one real unit of work, removing hidden cache skips, using serial debug helpers when needed, setting exact breakpoint order, and stepping into library boundaries intentionally.

### `python-class-and-filename`
Teaches agents how to create focused Python classes and choose matching `snake_case.py` filenames. Covers: one main class per file, responsibility-based module naming, converting `PascalCase` class names into readable filenames, avoiding vague modules like `utils.py`, and deciding when a stateless module should stay function-oriented instead of class-based.

### `repo-readme-writing`
Teaches agents how to write beginner-friendly GitHub README files. Covers required sections, writing for a newcomer audience, quick start sections, working code examples, and avoiding jargon.

### `real-data-validation-promotion`
Teaches agents how to validate pipelines on the smallest real dataset scope first and only then promote to broader sweeps. Covers: real-data smoke validation, stable smoke-to-full code paths, editable local dependency handling, summary-artifact versus plot-gallery separation, and honest residual-risk reporting.

---

## Documentation

| Guide | Description |
|---|---|
| [docs/beginner-guide.md](docs/beginner-guide.md) | First 30 minutes: setup and orientation |
| [docs/what-is-a-skill.md](docs/what-is-a-skill.md) | Canonical vs exported skills, skill.yaml format explained |
| [docs/skill-writing-guide.md](docs/skill-writing-guide.md) | How to design and write good skills |
| [docs/description-writing-guide.md](docs/description-writing-guide.md) | How to write descriptions that route accurately |
| [docs/update-workflow.md](docs/update-workflow.md) | How to safely update a skill |
| [docs/platforms/openai-codex.md](docs/platforms/openai-codex.md) | OpenAI Codex integration guide |
| [docs/platforms/claude-code.md](docs/platforms/claude-code.md) | Claude Code integration guide |
| [docs/platforms/gemini-gems.md](docs/platforms/gemini-gems.md) | Gemini Gems manual setup guide |

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

Quick summary:
- Always edit canonical files first, then regenerate exports
- Add examples for every new behavior
- Add test prompts for every bug found
- Update `CHANGELOG.md` with every change
- Run `agent-skillbook validate` and `pytest tests/ -v` before submitting

---

## License

MIT License. See [LICENSE](LICENSE).

Copyright (c) 2024 balandongiv.
