---
name: code-readability-best-practices
description: Review and refactor code for top-down readability by reorganizing functions, grouping related helpers, and rewriting noisy comments without changing behavior.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Code Readability Best Practices

This skill is for reviewing or refactoring code so it is easier to read in one pass. Apply it when a file feels jumpy, helpers are scattered, comments are noisy, or the overall flow is hard to follow even though the behavior is mostly correct.

The core idea is that readable code should feel like a guided flow. The highest-level purpose should appear first, supporting details should appear beneath the place they are introduced, and the remaining comments should explain non-obvious context rather than obvious syntax. Think of the file like a newspaper: the headline goes at the top, supporting detail appears below it, and smaller details appear further down.

---

## Core principles

### 1. Put the headline function first

Start with the function that best explains what the file does overall. A reader should learn the main purpose of the file by reading the first important function, not by hunting through low-level helpers.

### 2. Put details below where they are introduced

When a high-level function calls helpers, place those helpers below it whenever practical. Let the reader move downward from intent to implementation detail.

### 3. Group related code by purpose

Keep functions with the same concern near each other. Orchestration, business logic, persistence, formatting, validation, and shared utilities should naturally form clusters instead of being interleaved.

### 4. Optimize for scanability

Organize code for the next reader, not only for execution. A person should be able to scan from top to bottom and progressively understand more detail without constant jumping.

### 5. Keep comments specific and useful

Comments should explain what code alone cannot: a reason, constraint, workaround, business rule, risk, or precise future fix. If a comment only restates the code, sounds vague, or preserves stale history, remove or rewrite it.

### 6. Prefer plain text comments

Comments should read cleanly in an editor, diff, terminal, or copied snippet. Avoid HTML, decorative markup, and formatting tricks that add clutter.

---

## Function organization best practices

### 1. Put the highest-level function at the top

Start with the function that best explains what the code does overall. That top function is the headline. A reader should understand the file's purpose by reading it first.

### 2. Place details below where they are mentioned

When a top-level function calls helpers, define those helpers below it whenever practical.

This creates a natural downward reading flow:

- top: intent
- middle: supporting steps
- bottom: low-level utilities

### 3. Let the file read from high level to low level

A reader should be able to move downward through the file and progressively learn more detail. Avoid forcing the reader to jump around the file to understand a simple flow.

### 4. Keep called functions close to their caller

If `processUserReport()` calls `fetchUserData()`, `buildReport()`, and `saveReport()`, those functions should usually appear below it, near that flow.

### 5. Group by purpose and affinity

Functions that belong to the same concern should live near each other.

Examples:

- report-building helpers together
- formatting helpers together
- persistence helpers together
- validation helpers together

### 6. Separate layers naturally

A file becomes easier to scan when it naturally falls into layers:

- orchestration or entry-point logic
- domain or transformation logic
- persistence or I/O helpers
- shared formatting or utility helpers

### 7. Group shared utilities together

Utilities used across multiple functions should usually live together lower in the file, instead of being scattered.

### 8. Use naming patterns to reinforce structure

Related helpers should often share a naming pattern.

Examples:

- `formatDate()` and `formatScore()`
- `loadUser()` and `loadAccount()`
- `saveReport()` and `saveInvoice()`

Consistent naming helps the file self-organize.

### 9. Optimize for reading, not just execution

The goal is not only that the code works. The goal is that someone can read it in order and understand it quickly.

---

## Comment best practices

### 1. Do not write vague comments

Bad comments mumble. Avoid comments like:

- `not sure if it works`
- `might cause an issue`
- `edge case`

These create uncertainty without giving useful guidance.

### 2. If you are unsure, write a concrete TODO

If a behavior is uncertain, say exactly:

- what the risk is
- under what condition it appears
- what someone should check next

Good example:

```js
// TODO: Add a timeout check here.
// If the server response takes longer than 5 seconds,
// the UI can freeze.
```

### 3. Do not dump irrelevant detail

Avoid comments full of background material that does not help the next reader act.

Examples of low-value detail inside code comments:

- old implementation history
- author or date trivia
- outdated migration notes
- long backstory that belongs in a pull request, issue, or changelog

### 4. Do not write a novel for obvious code

If a one-line function already clearly says what it does, do not add a long paragraph explaining it.

Bad:

```js
// This function uses the Base64 encoding standard defined in RFC 4648...
function encodeImage(data) {
  return Buffer.from(data).toString('base64');
}
```

Better:

```js
function encodeImage(data) {
  return Buffer.from(data).toString('base64');
}
```

If the comment adds no critical context, delete it.

### 5. Comments should explain what code alone cannot

Useful comments usually explain one of these:

- why something exists
- a non-obvious constraint
- a workaround for a bug or environment issue
- a business rule
- a risk or caveat
- a future fix in precise terms

### 6. Delete stale historical comments

If a comment mostly says what happened years ago, who wrote it, or how an older version worked, it is probably noise in the codebase.

Move history to:

- version control
- commit messages
- pull requests
- issue trackers
- design docs

### 7. Prefer plain text comments

Do not fill code comments with HTML or presentation markup.

Comments should be readable directly in the editor.

Avoid comments like:

```js
// <p>Calculates the <b>final price</b> for the cart items.</p>
// <ul><li>Applies seasonal discounts</li></ul>
```

Prefer plain text:

```js
// Calculates the final price for cart items.
// Applies seasonal discounts and region-based tax.
```

### 8. Make comments readable everywhere

A comment should still be readable in:

- a plain editor
- a diff view
- a code review tool
- a terminal
- copied snippets

Plain language beats formatting tricks.

### 9. Comments should reduce noise, not add it

Every comment should earn its place. If removing a comment makes the code cleaner and loses nothing important, remove it.

---

## Review workflow

When applying this skill to a file, use this workflow.

### Step 1: Find the headline

Identify the function that best expresses the file's main job. Move it near the top if needed.

### Step 2: Walk the call flow

Read the main function and list the helpers it calls. Check whether those helpers appear below it in a sensible order.

### Step 3: Group by concern

Reorganize helpers into logical clusters, such as:

- orchestration
- business logic
- data access
- formatting
- shared utilities

### Step 4: Review every comment

For each comment, ask:

- Is it specific?
- Is it still true?
- Does it explain something non-obvious?
- Would the code be clearer without it?

### Step 5: Rewrite or remove

- rewrite vague comments into precise guidance
- delete comments that restate code
- delete stale history comments
- convert markup-heavy comments to plain text

### Step 6: Verify readability

A new reader should be able to:

- understand the purpose from the top of the file
- follow the flow downward
- find related helpers nearby
- understand the few comments that remain immediately

---

## Rules

- Preserve behavior unless the user explicitly asks for a logic change.
- Prioritize readability and scanability over clever ordering tricks.
- Explain structural changes in terms of top-down flow and grouping.
- Explain comment changes in terms of specificity and noise reduction.
- Prefer deleting weak comments over lightly rewording them.
- Prefer plain language over decorative formatting inside comments.
- Keep related helpers close together when they support the same flow.
- Put shared utilities together lower in the file when multiple areas depend on them.

---

## Common mistakes to avoid

- **Bottom-up organization**: Low-level helpers appear first, so the main purpose is hidden.
- **Scattered call flow**: A caller and its helpers are separated by unrelated code.
- **Mixed concerns**: Formatting, persistence, validation, and orchestration are interleaved without structure.
- **Vague comments**: Notes like `might fail` or `weird edge case` create noise without direction.
- **Historical comments**: Backstory remains in code long after it stopped helping the next reader.
- **Markup-heavy comments**: HTML or rich formatting makes comments harder to read in normal tools.
- **Readability-only refactors that accidentally change behavior**: Keep logic stable unless change is requested.

---

## Condensed rule set

- Put the headline function first.
- Put implementation details below where they are mentioned.
- Let the file read top-down.
- Keep related functions close.
- Group shared utilities together.
- Use naming to reveal structure.
- Do not write vague comments.
- Turn uncertainty into precise TODOs.
- Do not keep history lessons in code comments.
- Do not overexplain obvious code.
- Use plain text comments.
- Keep comments readable everywhere.
- Remove noise aggressively.

