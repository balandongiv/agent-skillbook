# Claude Code Platform Guide

This guide explains how to use skills from this repository with Claude Code (Anthropic's AI coding assistant).

---

## How Claude Code uses SKILL.md exports

Claude Code reads skill files and uses their `description` field to decide when to apply a skill during a conversation. When Claude receives a message that semantically matches a skill's description, it applies the instructions in that skill's `SKILL.md` body.

Like OpenAI Codex, this matching is **automatic** — Claude routes to the appropriate skill without explicit user invocation (if `auto: true` is set and the user has loaded the skill).

---

## Claude-specific frontmatter fields

The Claude export (`exports/claude/SKILL.md`) has additional frontmatter fields that are specific to Claude's behavior:

```yaml
---
name: good-function-design
description: Write small, readable, testable Python functions with clear names and explicit inputs and outputs. Use when writing or refactoring Python functions.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---
```

### Field explanations

**`name`**
The unique identifier for this skill. Used when referencing the skill by name.

**`description`**
The routing trigger. Claude uses this to semantically match incoming messages. Write this carefully — see [description-writing-guide.md](../description-writing-guide.md).

**`disable-model-invocation`**
When `true`, Claude will not automatically invoke this skill based on description matching. It can only be used when explicitly called by name. Default: `false`.

**`user-invocable`**
When `true`, users can explicitly invoke this skill by name (e.g., "Use the good-function-design skill to help me with this function"). Default: `true`.

**`allowed-tools`**
A list of tools (code execution, file reading, etc.) that this skill is allowed to use. An empty list means no restrictions. You can restrict tools for safety-critical skills.

---

## How auto-matching works in Claude

Claude's auto-matching uses the `description` field in a semantic similarity search. When a user message arrives:

1. Claude computes the semantic similarity between the message and all loaded skill descriptions
2. If a skill's description matches with sufficient confidence, Claude activates that skill
3. Claude follows the skill's `INSTRUCTIONS.md` content when generating a response

Auto-matching works best when:
- The description is specific and unambiguous
- The description includes context about *when* the skill applies
- There are no overlapping descriptions across skills

---

## How user invocation works

When `user-invocable: true` is set, users can explicitly call a skill:

> "Use the good-function-design skill to review my function."

Claude will recognize the skill by name and apply it, even if the auto-match would not have triggered.

This is useful for:
- Users who want a specific skill even when auto-routing would pick a different one
- Skills that are niche and rarely auto-match but are valuable when needed
- Testing whether a skill is loaded and working

---

## Using skills with CLAUDE.md

Claude Code supports a `CLAUDE.md` file at the root of a project or in your home directory. This file provides persistent instructions that Claude follows across conversations.

You can include skill instructions in your `CLAUDE.md` by referencing or copying the content from `exports/claude/SKILL.md`.

Alternatively, if you use Claude Code's official skill loading mechanism, point it at the exported `SKILL.md` files in this repository.

---

## Regenerating the Claude export

If you update the canonical skill files, regenerate the Claude export:

```bash
python tools/render_claude_skill.py skills/good-function-design
```

Or for all skills:

```bash
python -m agent_skillbook.cli render
```
