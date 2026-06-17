# Examples: Write Results Section from Verified Numbers

## Example 1: Sourced, referenced reporting vs vague prose

### Before (without this skill)

```
Our method performed significantly better than the baselines and was robust across settings.
```

### After (with this skill applied)

```
Across all 104 sessions (Table~\ref{tab:main}), Proposed-Med achieved the best macro-$F_1$ (0.867),
versus 0.853 for Proposed-Mean, 0.795 for BLINKER-concat, and 0.737 for MNE-annot. By paired Wilcoxon
with Bonferroni correction over six comparisons, Proposed-Med significantly outperformed all three
(corrected $p = 6.6\times10^{-6}$, $1.3\times10^{-4}$, and $1.4\times10^{-6}$ respectively).
```

### Why it's better

Every value is from the result artifact, the table is referenced, and the statistics are exact (test,
correction, comparison count, p-values) instead of a bare "significantly better".

---

## Example 2: Honest failure-mode and ghost-analysis handling

### Before (without this skill)

```
Naive concatenation fails primarily by reducing recall. Sensitivity analysis confirms robustness to
the n_min parameter.
```

(The data show concatenation is false-positive-heavy; there is no n_min results file.)

### After (with this skill applied)

```
Naive concatenation produced lower macro-$F_1$ through an unfavourable precision-recall trade-off:
BLINKER-concat had the highest recall (0.974) but the lowest precision (0.705) (Table~\ref{tab:main}).
% n_min sensitivity removed: no results artifact exists for this analysis.
```

### Why it's better

The mechanism now matches the data direction, and the unsupported n_min sentence is removed rather than
asserted without a results file.
