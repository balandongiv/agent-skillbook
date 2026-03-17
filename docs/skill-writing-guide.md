# Skill Writing Guide

This guide covers how to design, write, and maintain skills that work well in practice.

---

## Design principle: one skill per workflow

The most common mistake when writing skills is making them too broad.

A skill should cover **one specific workflow** or **one specific class of problem**. If you find yourself writing "this skill handles X, Y, and Z", it probably should be three separate skills.

**Too broad:**
> "Helps with writing Python code"

**Focused:**
> "Write small, readable, testable Python functions with clear names and explicit inputs and outputs."

The focused skill is easier to trigger accurately, easier to follow, and easier to improve over time.

---

## Writing good instructions

The `INSTRUCTIONS.md` file is what the AI agent reads. Write it as if you are handing a new colleague a standards document. Be precise.

### Structure your instructions

Use clear headings to organize the content:

```markdown
## Core principles

## Step-by-step process

## Rules

## Common mistakes to avoid
```

### Be specific and actionable

Vague:
> "Write clean code."

Specific:
> "Keep functions under 20 lines. If a function grows beyond 20 lines, identify whether it has more than one responsibility. If it does, extract each responsibility into its own named function."

### Explain the why

Agents (and humans) follow rules better when they understand the reason:

> "Avoid side effects unless intentional. Pure functions — functions that only compute a return value from their inputs — are easier to test, easier to reason about, and safer to reuse in different contexts."

### Include rules, not suggestions

Soft language like "you might consider" or "it can be helpful to" does not produce consistent behavior. Use direct, imperative language:

> "Always write a docstring. Always return a value explicitly. Never use mutable default arguments."

### Aim for at least 200 words

Thin instructions produce thin behavior. Take the time to spell out the full standard, including edge cases.

---

## Writing good examples

The `EXAMPLES.md` file shows the skill applied in practice. Good examples:

1. **Use realistic code or content** — not toy examples
2. **Show a clear before and after** — the contrast makes the lesson obvious
3. **Include an explanation** — "why is the after version better?"
4. **Cover edge cases** — not just the easy case

### Example template

```markdown
## Example 1: Refactoring a multi-responsibility function

### Before

def process_user(user_id, db, emailer):
    # 40 lines doing validation, DB queries, email sending, logging
    ...

### After

def validate_user_id(user_id: str) -> bool:
    ...

def fetch_user_from_db(user_id: str, db: Database) -> User:
    ...

def send_welcome_email(user: User, emailer: Emailer) -> None:
    ...

### Why it's better

Each function has one job. You can test validation without a database.
You can test the email logic without needing a real user record.
```

### How many examples?

At least two per skill. Three to five is better. More examples help the agent generalize.

---

## Writing good test prompts

Test prompts in `TESTS.md` serve two purposes:
1. **Human verification** — you can paste these into an AI agent to check if the skill triggers
2. **Regression tests** — if you change the description, you can quickly re-test all prompts

### Write prompts that sound like real user messages

Real:
> "Write a function to process user data and save it to the database."

Not realistic:
> "Apply the good-function-design skill."

### Cover edge cases and near-misses

Include prompts that are similar to other skills but should still trigger this one:
> "This function is hard to unit test, what should I do?"

### Five prompts minimum

You need enough coverage to catch routing failures.

---

## Keeping skills maintainable

Skills drift over time. Here are practices that help:

1. **Update CHANGELOG.md with every change.** Even small wording changes. This makes it easy to understand why a skill evolved.

   Use an `## [Unreleased]` section for ongoing changes. When you cut a repository release, move those notes into a dated semantic version section.

2. **Add a test prompt for every bug.** If a skill fires incorrectly or fails to fire, add a test prompt that captures the case. This prevents the same bug from returning.

3. **Review the description periodically.** As your use cases change, the routing description may need updating.

4. **Keep instructions DRY.** If two skills share a lot of instructions, consider extracting shared principles into a documentation page rather than duplicating them.

5. **Use the validator.** Run `agent-skillbook validate` before every commit. It catches common issues automatically.

   The validator also checks version awareness: each skill changelog must include `## [Unreleased]`, and the repository version must stay synchronized across `pyproject.toml`, `src/agent_skillbook/__init__.py`, and the README status line.

