---
name: experiment-runbook-discipline
description: Plan, launch, monitor, and document long-running experiments or validation sweeps with fresh experiment prefixes, live status artifacts, rolling logs, and final metric verification. Use when running smoke scopes, staged batches, full sweeps, or reruns after logic changes.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Experiment Runbook Discipline

Use this skill to keep long-running experiments observable, reproducible, and easy to audit later. Treat every substantial run as an investigation with durable artifacts, not as a terminal session that disappears once the process ends. The goal is not only to start the job, but to make it easy for another person or agent to answer four questions at any time: what is running, what logic version it uses, whether it is progressing, and how the final metrics turned out.

---

## Core principles

### 1. Create a written trail before execution

Create a markdown investigation note before the run starts. Record the dataset path, subject list or scope, experiment goal, chosen prefix, and whether existing outputs may be reused or must be force-rerun.

### 2. Treat the experiment prefix as a logic boundary

Use a fresh experiment prefix whenever logic changes in a way that could affect results. Do not mix outputs from different logic versions under the same prefix.

### 3. Make long runs observable

For any run that may take meaningful time, create or reuse a runner that writes:

- a rolling text log
- a live status JSON file
- a live status Markdown file

If the run is long enough to justify background execution, launch it in the background and immediately verify that it is actually progressing.

### 4. Verify progress, not only process existence

Do not assume a run is healthy because a process exists. Confirm that completed counts, timestamps, or other progress indicators are advancing.

### 5. Close the run with artifact and metric checks

A run is not complete just because files were written. Confirm the expected summary files exist and report the actual metrics from them.

---

## Step-by-step process

### Step 1: Confirm scope

Confirm the dataset path and the exact scope of the run. Decide whether the task is:

- a smoke scope
- a staged batch
- a full sweep

If the scope is unclear, infer the smallest safe scope first and promote to a larger run only after the smaller scope is clean.

### Step 2: Create the markdown note first

Write the investigation note before launching anything. Capture:

- purpose of the run
- dataset path
- subject list, split, or cohort
- experiment prefix
- whether outputs will be reused or force-rerun
- commands or entry points used

Update this note during the run and after completion.

### Step 3: Choose a fresh prefix

Pick a prefix that clearly separates this run from older artifacts. If logic changed, increment the prefix even if the dataset and scope are unchanged. Treat old outputs as historical evidence, not as inputs to the new conclusion.

### Step 4: Prepare observability

Make sure the run emits at least:

- a rolling text log for append-only progress and errors
- a live status JSON file for machine-readable state
- a live status Markdown file for quick human inspection

Tell the user exactly which files can be watched live.

### Step 5: Launch and verify

Launch the run in the foreground or background as appropriate. Then verify all of the following:

- the process is alive
- the log is updating
- the live status files exist
- the completed count or equivalent progress signal is increasing

If the run goes quiet for too long, inspect the log and process state before restarting.

### Step 6: Finish with explicit validation

When the run finishes, check for the expected outputs such as:

- summary CSV
- overall JSON
- per-subject or per-unit artifacts

Then extract and report the key metrics from those outputs. Do not report success without citing the final artifacts that justify it.

### Step 7: Handle logic changes correctly

If you changed scoring, preprocessing, evaluation logic, or any other result-affecting code, do all of the following:

- increment the experiment prefix
- rerun the previously validated scopes under the new prefix
- update the markdown note with what changed and why
- record what was revalidated and what remains pending

---

## Rules

- Always create the markdown investigation note before the run.
- Always confirm dataset path and scope before launching substantial work.
- Always choose a fresh prefix after logic changes.
- Always provide exact live-watch paths for logs and status files.
- Always verify progress by observing changing counters, timestamps, or completed outputs.
- Always report final metrics from the generated summary artifacts.
- Never reuse old prefixes after result-affecting logic changes.
- Never restart a quiet run until you inspect logs and process state.
- Never claim completion based only on process exit or file existence.

---

## Common mistakes to avoid

- **Ad hoc execution**: Starting a long run without a note, prefix, or live status files makes later debugging much harder.
- **Prefix reuse after logic changes**: Reusing an old prefix contaminates comparisons and makes it unclear which logic produced which results.
- **Watching only the terminal**: A detached terminal is not durable evidence. Keep rolling logs and status artifacts on disk.
- **Checking liveness but not progress**: A stuck process can stay alive for hours. Verify that meaningful counters move.
- **Stopping at file existence**: A summary file can exist and still contain failed or partial results. Read the final metrics.
- **Skipping revalidation after fixes**: If logic changed, rerun the scopes that previously established confidence.

---

## Condensed checklist

- Confirm dataset path and scope.
- Create the markdown note first.
- Choose a fresh experiment prefix.
- Decide reuse versus force-rerun.
- Ensure rolling log plus live JSON and Markdown status files.
- Launch and verify real progress.
- Tell the user which files to watch live.
- Validate final artifacts and metrics.
- If logic changed, increment prefix and rerun validated scopes.
