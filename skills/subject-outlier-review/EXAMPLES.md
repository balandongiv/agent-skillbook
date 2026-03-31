# Examples: Subject Outlier Review

---

## Example 1: Auditing a suspected weak subject

### Before (without this skill)

```text
Performance is low. Drop the worst subject and report the new score.
```

### After (with this skill applied)

```text
1. Load `05_models/subject_performance.parquet` or derive it from `predictions.parquet`.
2. Rank subjects by MCC, balanced accuracy, and support.
3. Show the full comparison table.
4. Diagnose the weakest subject before recommending any exclusion.
5. State whether exclusion is justified, not justified, or still unproven.
```

### Why it's better

The improved approach turns an intuition into an auditable review and prevents silent cherry-picking.

---

## Example 2: Handling justified exclusion correctly

### Before (without this skill)

```text
S11 looks bad. Remove it from the final result.
```

### After (with this skill applied)

```text
1. Document why S11 appears invalid or corrupted.
2. Rerun with `analysis.evaluation.exclude_subject_ids`.
3. Keep both the full-cohort and filtered-cohort results.
4. Report that the exclusion is an explicit evaluation decision, not a replacement of history.
```

### Why it's better

It preserves traceability and makes the exclusion reviewable by someone reading the results later.

---

## Example 3: Rejecting exclusion when evidence is weak

### Before (without this skill)

```text
This subject has the lowest score, so it should probably be removed.
```

### After (with this skill applied)

```text
Conclusion: exclusion is still unproven.

Evidence:
- low MCC
- normal support
- no confirmed preprocessing or annotation issue
- class distribution is difficult but still plausible

Next step:
- inspect data-quality signals before any filtered rerun
```

### Why it's better

It keeps the evaluation honest when the case for exclusion has not actually been established.
