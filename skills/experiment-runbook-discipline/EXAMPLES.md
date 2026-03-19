# Examples: Experiment Runbook Discipline

---

## Example 1: Turning a full sweep into an observable run

### Before (without this skill)

```text
Run the full validation over all subjects tonight.
Use the same prefix as the last run.
Leave it in a terminal window.
Tomorrow, check whether some output files exist.
```

### After (with this skill applied)

```text
1. Create docs/findings/2026-03-18-exp12-validation.md before the run.
2. Record the dataset path, subject list, and scope: full sweep.
3. Choose a fresh prefix: exp12.
4. Launch through a runner that writes:
   - logs/exp12.log
   - status/exp12.json
   - status/exp12.md
5. Start in the background and verify:
   - the process is alive
   - the log is updating
   - completed_count is increasing
6. Tell the user exactly which files to watch live.
7. On completion, confirm:
   - results/exp12/summary.csv
   - results/exp12/overall.json
   - expected per-subject artifacts
8. Report the final metrics from the summary files.
```

### Why it's better

The improved version creates a durable trail before the run starts, makes the long run observable while it is executing, and ends with explicit artifact and metric checks instead of a vague "it finished" conclusion.

---

## Example 2: Rerunning safely after a logic change

### Before (without this skill)

```text
Fix the scoring bug.
Reuse exp12 because the dataset is the same.
Run only the missing subjects.
Compare new numbers against the old note informally.
```

### After (with this skill applied)

```text
1. Record the scoring fix in a markdown investigation note.
2. Increment the prefix from exp12 to exp13.
3. Rerun the previously validated smoke group under exp13.
4. If the smoke scope is clean, rerun the staged batch or full sweep under exp13.
5. Keep exp12 as old-logic evidence; do not mix it into exp13 conclusions.
6. Update the note with:
   - what changed
   - why it changed
   - what was revalidated
   - which final artifacts and metrics now represent the current logic
```

### Why it's better

The new approach preserves a clean boundary between logic versions. It protects reproducibility, avoids mixed evidence, and makes it obvious which outputs belong to the current implementation.

---

## Example 3: Using a smoke scope before a costly full run

### Before (without this skill)

```text
Run the full experiment immediately.
If something fails after six hours, patch it and restart.
```

### After (with this skill applied)

```text
1. Classify the first run as a smoke scope.
2. Use a fresh prefix such as exp21-smoke.
3. Confirm that logs, live status files, and expected summary artifacts all behave correctly.
4. Promote to a staged batch only after the smoke scope is clean.
5. Launch the full sweep under a separate prefix once the smaller scopes prove the pipeline is healthy.
```

### Why it's better

This version buys confidence cheaply. Small scopes catch broken paths, missing outputs, and stalled progress earlier, which reduces wasted compute time on the full sweep.

---

## Example 4: Treating editable local dependencies as part of the validation run

### Before (without this skill)

```text
The full run failed inside a package that is installed editable from a local repo.
Patch around it downstream and continue the batch.
```

### After (with this skill applied)

```text
1. Record the editable dependency and local repo path in the investigation note.
2. Stop promotion to larger scopes.
3. Fix the bug at the dependency source.
4. Rerun the smallest real-data smoke scope under a fresh prefix.
5. Promote back to staged or full runs only after the smoke scope is clean again.
```

### Why it's better

It keeps the validation honest, fixes the real source of failure, and prevents a broken dependency from contaminating later runs.
