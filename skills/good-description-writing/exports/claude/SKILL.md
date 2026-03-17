---
name: good-description-writing
description: Write precise, specific descriptions for agent skills, tools, and functions so that AI agents can route to them accurately.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Good Description Writing

This skill guides you through writing descriptions that work as routing triggers for AI agents. The description is not documentation — it is a signal. It tells the agent: "activate me when this situation arises." Apply these principles when writing or editing any `description`, `summary`, or `when_to_use` field in a skill, tool, or agent definition.

---

## Why descriptions are different from documentation

When you write a README or a user guide, your audience is a human who reads carefully. You can afford to be broad, narrative, and exploratory.

When you write a description for an AI agent skill or tool, your audience is the routing mechanism of an AI system. It performs semantic matching — it compares the user's message to your description and asks: "does this description match what the user needs right now?"

This means:
- **Vague descriptions match too many things** (false positives)
- **Narrow descriptions match too few things** (false negatives)
- **Filler words add noise without signal**

A good description is precise, action-oriented, and specific enough to be distinguishable from other descriptions in the same system.

---

## The description formula

Use this template:

> **[Verb phrase describing the action] + [specific object or output] + [context: for whom / in what situation]**

Examples:

| Weak | Strong |
|---|---|
| "Helps with code" | "Write Python functions with single responsibility and explicit parameters" |
| "Handles descriptions" | "Write routing descriptions for AI agent skills so they trigger accurately" |
| "Manages README files" | "Write structured README files for GitHub repositories aimed at beginners" |

---

## Core rules

### Rule 1: Start with a verb

The description should begin with an action verb that names what the skill produces or does:
- Write, Generate, Refactor, Analyze, Review, Convert, Extract, Validate…

Avoid starting with nouns or vague openers like "This skill…" or "A tool that…"

### Rule 2: Name the specific output or artifact

Be concrete about what is produced:
- "a Python function" — not "code"
- "a skill description" — not "text"
- "a GitHub README" — not "documentation"

### Rule 3: Include context about when it applies

Add a clause that describes the situation that triggers this skill:
- "…when writing or refactoring Python functions"
- "…when a skill is not triggering correctly"
- "…when creating or updating a GitHub repository"

### Rule 4: Avoid filler verbs

These words add no information and hurt routing accuracy:
- handles, manages, deals with, works with, helps with, processes, supports, assists

Replace them with specific action verbs that describe what actually happens.

### Rule 5: Keep it to one or two sentences

The routing system reads quickly. A description longer than two sentences becomes hard to match precisely. Put additional detail in `when_to_use` and `when_not_to_use`, not in the description.

### Rule 6: Make it distinguishable

If you have two skills and their descriptions could be confused, one of them needs to be more specific. Test: could you tell from the description alone which skill to use for a given request?

---

## Bad vs good description examples

### Example: Tool description for a database query function

**Bad:** "Handles database operations."
**Problem:** What operations? Read? Write? Which database? This matches everything.

**Good:** "Execute a read-only SQL SELECT query and return the results as a list of dictionaries."
**Why:** Specific operation (SELECT), specific output type (list of dicts), explicit constraint (read-only).

---

### Example: Agent skill description

**Bad:** "Helps with writing."
**Problem:** Every writing task matches this. The skill will trigger constantly for unrelated tasks.

**Good:** "Write precise routing descriptions for AI agent skills and tools so they trigger on the correct user requests."
**Why:** Specific domain (routing descriptions), specific audience (AI agent skills), specific purpose (trigger on correct requests).

---

### Example: Summary field in skill.yaml

**Bad:** "Assists with Python development tasks."
**Problem:** Too broad. Any Python task would match.

**Good:** "Write small, readable, testable Python functions with clear names and explicit inputs and outputs."
**Why:** Names the output (Python functions), names the qualities (small, readable, testable, clear names, explicit I/O), nothing extraneous.

---

## After writing a description

1. Test it with the test prompts in `TESTS.md`. Do they trigger the skill?
2. Check for filler words. Remove any you find.
3. Check: is it distinguishable from descriptions of similar skills?
4. Read it aloud. Does it sound like it names exactly what the skill does?

If you change the description in `skill.yaml`, regenerate all exports immediately:
```bash
python -m agent_skillbook.cli render
```
