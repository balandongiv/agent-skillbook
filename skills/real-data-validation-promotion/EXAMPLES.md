# Examples: Real-Data Validation Promotion

---

## Example 1: Replacing synthetic smoke with the smallest real-data validation

### Before (without this skill)

```text
Run the pipeline on synthetic fixtures.
If the unit tests pass, assume the real dataset pipeline is okay.
Then launch the full sweep.
```

### After (with this skill applied)

```text
1. Keep the unit tests for isolated logic.
2. Choose one real subject/session that exercises the true file layout.
3. Run the real stage entrypoint on that one case first.
4. Inspect the actual summary artifacts and counts.
5. Promote to the broader sweep only after the one-case smoke is clean.
```

### Why it's better

It validates the actual dataset contract before paying the cost of a full run.

---

## Example 2: Fixing an issue in an editable local dependency

### Before (without this skill)

```text
The run fails inside a local package installed editable.
Wrap the call in try/except in the main project and continue.
```

### After (with this skill applied)

```text
1. Record the editable dependency and its local repo path.
2. Step into the dependency and confirm the failure source.
3. Patch the dependency itself.
4. Rerun the smallest real-data smoke scope.
5. Promote back to the larger run only after that smoke scope passes.
```

### Why it's better

The validation stays truthful because the real source of failure is fixed and revalidated.

---

## Example 3: Splitting readable EDA from heavy plots

### Before (without this skill)

```text
Write one huge HTML file that mixes summary EDA, artifact counts, and every single plot.
```

### After (with this skill applied)

```text
1. Write one summary EDA HTML for counts, distributions, schema checks, and naming examples.
2. Write a separate plot-gallery HTML for the heavy per-event visuals.
3. Use the summary EDA as the validation artifact you inspect first.
```

### Why it's better

The validation remains easy to inspect while still preserving the detailed gallery for deeper debugging.
