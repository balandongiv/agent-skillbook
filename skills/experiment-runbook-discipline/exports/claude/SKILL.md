---
name: experiment-runbook-discipline
description: Plan, launch, monitor, and document long-running experiments or validation sweeps with smallest-real-data smoke scopes, fresh experiment prefixes, live status artifacts, rolling logs, and promotion to full runs only after explicit pass criteria are met.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Experiment Runbook Discipline

Use this skill to keep long-running experiments observable, reproducible, and easy to audit later. Treat every substantial run as an investigation with durable artifacts, not as a terminal session that disappears once the process ends. The goal is not only to start the job, but to make it easy for another person or agent to answer four questions at any time: what is running, what logic version it uses, whether it is progressing, and how the final metrics turned out. When the user cares about true pipeline readiness, prefer the smallest real-data smoke scope first and promote only after explicit pass criteria are satisfied.

---

## Core principles

### 1. Start with the smallest real-data scope that can prove the claim

If the user wants to validate a pipeline, experiment stack, or result-producing workflow, use real data first whenever it is available and safe to use. Synthetic data is excellent for unit tests and regression coverage, but it is not enough to claim that the real file layout, annotations, caches, or dependency boundaries work correctly.

### 2. Create a written trail before execution

Create a markdown investigation note before the run starts. Record the dataset path, subject list or scope, experiment goal, chosen prefix, and whether existing outputs may be reused or must be force-rerun.

### 3. Treat the experiment prefix as a logic boundary

Use a fresh experiment prefix whenever logic changes in a way that could affect results. Do not mix outputs from different logic versions under the same prefix.

### 4. Treat editable local dependencies as part of the run logic

If the environment uses editable local packages, record that fact in the investigation note and include the relevant local repo path or package name in the run scope. If a failure originates inside that dependency, patch the dependency, then rerun the appropriate smoke scope before promoting the broader run.

### 5. Make long runs observable

For any run that may take meaningful time, create or reuse a runner that writes:

- a rolling text log
- a live status JSON file
- a live status Markdown file
- any required summary EDA, index, or catalog artifact that proves the outputs are structurally sane

If the run is long enough to justify background execution, launch it in the background and immediately verify that it is actually progressing.

### 6. Verify progress, not only process existence

Do not assume a run is healthy because a process exists. Confirm that completed counts, timestamps, or other progress indicators are advancing.

### 7. Close the run with artifact and metric checks

A run is not complete just because files were written. Confirm the expected summary files exist and report the actual metrics from them.

---

## Step-by-step process

### Step 1: Confirm scope

Confirm the dataset path and the exact scope of the run. Decide whether the task is:

- a smoke scope
- a staged batch
- a full sweep

If the scope is unclear, infer the smallest safe real-data scope first and promote to a larger run only after the smaller scope is clean.

### Step 2: Create the markdown note first

Write the investigation note before launching anything. Capture:

- purpose of the run
- dataset path
- subject list, split, or cohort
- experiment prefix
- whether this is a real-data smoke, staged batch, or full sweep
- editable local dependencies that are in scope
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
- any summary EDA, index, or catalog artifact that proves the outputs are structurally sane

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
- rerun the smallest real-data smoke if the change touched a local editable dependency or a core stage boundary
- update the markdown note with what changed and why
- record what was revalidated and what remains pending

---

## Rules

- Always create the markdown investigation note before the run.
- Always confirm dataset path and scope before launching substantial work.
- Always prefer real-data smoke scopes for pipeline validation when real data is available.
- Always choose a fresh prefix after logic changes.
- Always record editable local dependencies that affect the run.
- Always provide exact live-watch paths for logs and status files.
- Always verify progress by observing changing counters, timestamps, or completed outputs.
- Always report final metrics from the generated summary artifacts.
- Always rerun the smoke scope after result-affecting fixes in a local editable dependency.
- Never reuse old prefixes after result-affecting logic changes.
- Never treat synthetic-only smoke as sufficient evidence for real-data pipeline readiness when the user asked for actual dataset validation.
- Never restart a quiet run until you inspect logs and process state.
- Never claim completion based only on process exit or file existence.

---

## Common mistakes to avoid

- **Ad hoc execution**: Starting a long run without a note, prefix, or live status files makes later debugging much harder.
- **Prefix reuse after logic changes**: Reusing an old prefix contaminates comparisons and makes it unclear which logic produced which results.
- **Watching only the terminal**: A detached terminal is not durable evidence. Keep rolling logs and status artifacts on disk.
- **Checking liveness but not progress**: A stuck process can stay alive for hours. Verify that meaningful counters move.
- **Using only synthetic smoke for a real-data claim**: Unit tests may pass while real annotations, layout, or dependencies still fail.
- **Forgetting editable dependencies**: If a local package is installed editable, its bugs are part of the run logic and should be tracked explicitly.
- **Stopping at file existence**: A summary file can exist and still contain failed or partial results. Read the final metrics.
- **Skipping revalidation after fixes**: If logic changed, rerun the scopes that previously established confidence.

---

## Condensed checklist

- Confirm dataset path and scope.
- Prefer the smallest representative real-data smoke scope first.
- Create the markdown note first.
- Choose a fresh experiment prefix.
- Record editable local dependencies in scope.
- Decide reuse versus force-rerun.
- Ensure rolling log plus live JSON and Markdown status files.
- Launch and verify real progress.
- Tell the user which files to watch live.
- Validate final artifacts and metrics.
- If logic changed, increment prefix and rerun validated scopes.
