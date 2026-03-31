# Description Writing Guide

This is one of the most important documents in the repository. Read it carefully before writing or editing any skill description.

---

## Why the description field is critical

The `summary` field in `skill.yaml` — and the `description` in exported `SKILL.md` files — is the **primary routing trigger** for OpenAI Codex and Claude Code.

When a user sends a message to an AI agent, the agent compares the message to the descriptions of all loaded skills. If the message semantically matches a skill's description, the agent loads that skill's instructions and applies them.

**This means: if your description is vague, your skill will not trigger when it should — or it will trigger when it shouldn't.**

---

## How OpenAI Codex uses descriptions

OpenAI Codex uses the `description` field in the YAML frontmatter of `SKILL.md` to decide which skill to apply. It does a semantic match between the user's input and the skill description.

A description that is too broad will match everything. A description that is too narrow will miss legitimate use cases. You need to find the right level of specificity.

---

## How Claude Code uses descriptions

Claude Code operates similarly. It reads the `description` field from the `SKILL.md` frontmatter and uses it to decide whether to invoke the skill for a given conversation. The description acts as a pre-filter: "does this conversation call for this skill?"

Claude also exposes the skill to users via `user-invocable: true`, so users can invoke the skill by name. But the description still governs automatic matching.

---

## Bad description examples

Here are descriptions that will cause problems, with explanations of why.

### Too vague

> "Helps with code."

**Problem:** This matches almost any programming task. Every code-related conversation will trigger this skill, even if it is irrelevant.

### Too narrow

> "Writes Python functions named `process_data` that take a string argument."

**Problem:** This is so specific it will almost never match. Real user messages won't contain those exact words.

### Uses filler words

> "Handles, manages, and deals with Python function writing."

**Problem:** Words like "handles", "manages", "deals with", and "helps with" are routing poison. They are filler. They do not convey what the skill does. The router cannot distinguish "handles Python functions" from "handles SQL queries."

### States the tool, not the task

> "Uses Python to do programming tasks."

**Problem:** This describes the tool (Python) rather than the workflow. The agent already knows it is writing Python code. The description should describe *what kind of help* this skill provides.

### No context about when to use

> "Write Python functions."

**Problem:** Almost every Python task involves writing a function. This description lacks the context that would help the router distinguish this skill from others.

---

## Good description examples

### Specific and contextual

> "Write small, readable, testable Python functions with clear names and explicit inputs and outputs. Use when writing or refactoring Python functions."

**Why it works:**
- Describes the *outcome* (small, readable, testable)
- Describes the *context* (when writing or refactoring)
- Uses concrete adjectives that distinguish this skill from a generic "write code" skill

### Includes the trigger context

> "Write precise, specific descriptions for agent skills, tools, and functions so that AI agents can route to them accurately. Use when writing or editing a skill description or tool description."

**Why it works:**
- Names the specific artifact being produced (descriptions for agent skills)
- Names the purpose (accurate routing)
- Names the trigger context (when writing or editing a skill description)

### Clear audience and output

> "Write clear, structured, beginner-friendly README files for GitHub repositories that explain purpose, setup, and usage."

**Why it works:**
- Describes the output (README files)
- Describes the audience (beginner-friendly)
- Describes the content (purpose, setup, usage)
- Specifies the platform (GitHub repositories)

---

## The description formula

A reliable formula for writing skill descriptions:

> **[Action verb] + [specific output] + [for whom / on what] + [so that / in order to]**

Examples applying the formula:

| Action | Output | For/On What | Purpose |
|---|---|---|---|
| Write | small, testable functions | in Python | so code is easy to maintain |
| Write | precise routing descriptions | for agent skills and tools | so AI agents match them accurately |
| Write | structured README files | for GitHub repositories | so beginners can get started quickly |

---

## Checklist before finalizing a description

- [ ] Does it say what the skill *produces* or *achieves*?
- [ ] Does it say *when* the skill is relevant?
- [ ] Is it free of filler words (handles, manages, deals with, helps)?
- [ ] Is it specific enough to distinguish this skill from similar skills?
- [ ] Is it short enough to be read in one sentence?
- [ ] Would a test prompt naturally match this description?

---

## When to update a description

Update the description when:
- A test prompt that should trigger the skill is not triggering it
- The skill is triggering for tasks where it is not relevant
- The scope of the skill has changed

After updating the description in `skill.yaml`, regenerate all exports:
```bash
python -m agent_skillbook.cli render
```
