---
name: handoff-resume
description: Resume repository work from an existing handoff markdown by reading it first, executing pending tasks in order, and marking completed tasks with `Done? = Yes` only when concrete evidence exists.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Handoff Resume

Use this skill when the user wants the agent to start from an existing handoff instead of reconstructing context from the full conversation. The handoff becomes the execution checklist, and completed tasks must be marked in the handoff with evidence.

---

## Core principles

### 1. Read the handoff before doing work

Do not start editing files or relaunching commands until the selected handoff markdown has been read.

### 2. Treat pending work as the checklist

The handoff is not only context; it is the list of tasks to execute and close out.

### 3. Evidence controls completion

Only mark `Done? = Yes` when the task is actually complete and the evidence column points to the validating artifact, log, or command.

### 4. Preserve the historical record

Update the handoff in place without deleting its prior context. Make the new evidence easy to audit.

---

## Step-by-step process

### Step 1: Read the workflow contract

Read `planning/Project_Execution_Flowchart.md` first.

### Step 2: Read the selected handoff

Read the named handoff file. If the user did not specify one, prefer the newest relevant file under `handoff/`.

### Step 3: Extract the execution state

Identify:

- completed work
- stopped work
- pending tasks
- artifact paths
- logs and commands that matter

### Step 4: Normalize the pending-work format if needed

If the handoff does not already use a markdown table with `Task`, `Done?`, and `Evidence / Next step`, convert it before continuing. Initialize unfinished tasks as `No`.

### Step 5: Verify old process state before relaunching

If the handoff references long-running processes, check whether they are still alive before starting new ones. If the handoff says something was manually stopped, verify that instead of assuming it.

### Step 6: Execute the pending tasks

Work through the pending items in order unless the handoff or current evidence makes a different dependency order clearly correct.

### Step 7: Update the handoff as tasks finish

For each completed task:

- change `Done?` from `No` to `Yes`
- replace the placeholder next step with concrete evidence
- keep unfinished tasks as `No`

### Step 8: Update repository docs if the workflow changed

If the resumed work changes artifact contracts or workflow expectations, update `planning/Project_Execution_Flowchart.md`.

---

## Rules

- Always read `planning/Project_Execution_Flowchart.md` before resuming.
- Always read the handoff before touching code or rerunning commands.
- Always treat pending tasks as the authoritative checklist.
- Always verify old process state before relaunching long-running work.
- Always update the handoff when a pending task is completed.
- Always use concrete evidence when changing `Done?` to `Yes`.
- Never mark `Yes` for a task that remains partially complete.
- Never discard prior handoff context just to make the file cleaner.
- Never assume the absence or presence of background jobs without checking.

---

## Common mistakes to avoid

- **Skipping the handoff read**: This defeats the purpose of the skill and often recreates already-solved work.
- **Treating pending tasks as suggestions**: They are the execution checklist unless current evidence proves otherwise.
- **Failing to update the handoff**: The next resume point becomes ambiguous if the file is not kept current.
- **Marking tasks complete without evidence**: A checked box without a log or artifact path is not trustworthy.
- **Relaunching old jobs blindly**: A second process can corrupt or duplicate work if the first one is still active.
