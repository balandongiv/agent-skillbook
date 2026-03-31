# Examples: Good Description Writing

---

## Example 1: Fixing a vague tool description

### Before (without this skill)

```yaml
name: save_record
description: Handles saving records to the system.
```

### After (with this skill applied)

```yaml
name: save_record
description: >
  Persist a new or updated record to the database.
  Use when the user has confirmed changes and wants to save them permanently.
```

### Why it's better

The original "handles saving records to the system" is vague on all dimensions: what kind of record, which system, when to call it. The improved version names the specific action (persist), the target (database), and the trigger condition (after user confirmation). An AI agent can now distinguish this tool from `fetch_record`, `delete_record`, or `validate_record`.

---

## Example 2: Fixing a skill summary that causes false positives

### Before (without this skill)

```yaml
slug: code-review-checklist
summary: Helps with reviewing code.
```

This skill was triggering for almost every coding conversation, even when the user just wanted to write new code rather than review existing code.

### After (with this skill applied)

```yaml
slug: code-review-checklist
summary: >
  Review existing Python code against a quality checklist covering readability,
  testability, error handling, and naming conventions. Use when the user asks
  for a code review or quality assessment of existing code.
```

### Why it's better

The improved description names the specific activity (review existing code), the method (checklist), the domains covered (readability, testability, etc.), and the trigger context (when the user asks for a review). A user asking "write me a function" will no longer match this skill — they are not asking for a review. The routing is now accurate.

---

## Example 3: Writing a description from scratch for a new skill

### Situation

You are writing a new skill called `sql-query-optimization`. Before writing the description, you brainstorm:
- What does this skill do? It analyzes slow SQL queries and suggests optimizations.
- What are the outputs? Specific rewrite suggestions with explanations.
- When is it relevant? When a query is slow, when indexes are missing, when EXPLAIN output shows table scans.
- Who is the audience? Developers who already have a working query but need it to perform better.

### Applying the formula

> **[Verb]** + **[specific output]** + **[context]**

> "Analyze slow SQL queries and suggest index additions, query rewrites, and execution plan improvements. Use when a working query is too slow for production or when EXPLAIN shows full table scans."

### Why this works

- Starts with a verb: "Analyze"
- Names the specific output: "index additions, query rewrites, execution plan improvements"
- Distinguishes from a general "write SQL" skill by including "slow" and "execution plan"
- Includes the trigger context: "when a working query is too slow"
