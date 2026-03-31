# OpenAI Codex Platform Guide

This guide explains how to use skills from this repository with OpenAI Codex and OpenAI custom agents.

---

## How OpenAI Codex auto-matches skills

OpenAI Codex uses the `description` field in a skill's YAML frontmatter to decide when to apply the skill. When you load a skill as a custom instruction or agent configuration, Codex performs a semantic match between the user's message and the skill description.

**This is automatic** — you do not need to tell the agent "use the good-function-design skill." If the user asks "help me refactor this Python function," Codex will recognize that this matches the description of the `good-function-design` skill and apply it.

This is why writing a good description is critical. See [description-writing-guide.md](../description-writing-guide.md) for details.

---

## The SKILL.md export structure

Each skill generates `exports/openai/SKILL.md` with this structure:

```markdown
---
name: good-function-design
description: Write small, readable, testable Python functions with clear names and explicit inputs and outputs. Use when writing or refactoring Python functions.
---

## Good Function Design

[Full instructions from INSTRUCTIONS.md]
```

The **YAML frontmatter** at the top provides metadata for OpenAI:
- `name` — unique identifier for this skill
- `description` — the routing trigger (semantic match target)

The **body** contains the full instructions the agent will follow when this skill is active.

---

## The agents/openai.yaml structure

Each skill also generates `exports/openai/agents/openai.yaml`:

```yaml
name: good-function-design
description: Write small, readable, testable Python functions with clear names and explicit inputs and outputs. Use when writing or refactoring Python functions.
instructions_file: ../SKILL.md
```

This file is used when configuring an OpenAI custom agent (in the OpenAI platform or API). It tells the agent:
- The name of this capability
- What the description is (for routing)
- Where the full instructions are stored

---

## How to install and use a skill with OpenAI

### Option 1: Copy to your project

Copy the `exports/openai/` directory to your OpenAI agent project. Reference `SKILL.md` in your agent configuration.

### Option 2: Use as a custom instruction

1. Open ChatGPT or the OpenAI API playground
2. In the system prompt or custom instructions section, paste the content of `exports/openai/SKILL.md`
3. The agent will now apply the skill when relevant

### Option 3: Use with the OpenAI Assistants API

When creating an assistant via the API, include the content of `exports/openai/SKILL.md` as part of the assistant's instructions. The description in the frontmatter helps you organize and document your agent's capabilities.

---

## Regenerating the OpenAI export

If you update the canonical skill files, regenerate the export:

```bash
python tools/render_openai_skill.py skills/good-function-design
```

Or for all skills:

```bash
python -m agent_skillbook.cli render
```
