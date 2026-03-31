---
name: handoff
description: Create operational handoff markdowns that capture what was completed, what is stopped, what remains pending, which artifacts matter, and which commands the next agent should run next.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Handoff

Use this skill to create a repository-local handoff that another agent can resume from without reconstructing state from chat history. The handoff must be operational: it should identify concrete artifacts, process state, pending tasks, and next commands.

---

## Core principles

### 1. Inspect current reality before writing the note

Use the current repository state, logs, artifact paths, and process list as the source of truth. Do not rely on memory alone.

### 2. Separate completed work from stopped work

A handoff should distinguish code edits, regenerated outputs, and work that was interrupted or intentionally stopped. Do not blur these together.

### 3. Make pending work executable

Pending work should read like a checklist the next agent can complete and mark with evidence. Avoid vague prose.

### 4. Record exact evidence

Use exact paths, run prefixes, hashes, log files, and commands. The next agent should not have to infer where outputs live.

---

## Step-by-step process

### Step 1: Read the repository workflow contract

Read `planning/Project_Execution_Flowchart.md` first so the handoff uses the repository's current artifact and workflow language.

### Step 2: Inspect the live state

Before writing:

- inspect `git status --short`
- inspect the relevant logs, especially `.codex-tmp/live_logs/` when present
- inspect current outputs and status files
- inspect active processes if long-running work may still exist

### Step 3: Write the handoff file

Write a markdown file under `handoff/`. Prefer a date- or task-specific filename that the next agent can find easily.

### Step 4: Include the required sections

Every handoff must include:

- `Scope`
- `What Has Been Done`
- `What Is Stopped`
- `Current Working State`
- `Pending Work`
- `Suggested Next Commands`
- `Open Risks`

### Step 5: Use a structured pending-work table

Inside `Pending Work`, use a markdown table with:

- `Task`
- `Done?`
- `Evidence / Next step`

Default incomplete tasks to `No`. Only write `Yes` when the task is actually complete and evidenced.

### Step 6: Record process state explicitly

If background jobs were running, state whether they are still alive, already finished, or manually stopped. Do not say a run "finished" unless status artifacts or logs confirm that.

### Step 7: Update repository docs when the handoff contract changes

If the handoff workflow, required sections, or storage location changes, update `planning/Project_Execution_Flowchart.md`.

---

## Rules

- Always read `planning/Project_Execution_Flowchart.md` first.
- Always inspect current reality instead of relying on conversation history alone.
- Always write handoffs under `handoff/`.
- Always include the required sections.
- Always use the `Task | Done? | Evidence / Next step` table for pending work.
- Always use exact file paths and log paths.
- Always state whether relevant background processes are still alive.
- Always distinguish code changes from regenerated outputs.
- Never mark `Done?` as `Yes` without concrete evidence.
- Never claim a run completed solely because a process exited.
- Never omit the dirty-worktree state when it matters for resuming safely.

---

## Common mistakes to avoid

- **Narrative recap without operations**: A story of the session is not enough; the next agent needs commands and artifact paths.
- **No pending-task structure**: Loose bullets make it hard to tell what is actually left to do.
- **Assuming process state**: A stopped terminal and a stopped process are not the same thing.
- **Missing validation evidence**: If a PDF was rebuilt or a run finished, record the exact log or output path.
- **Overwriting history**: Preserve the context of what happened; append clear updates rather than erasing the trail.
