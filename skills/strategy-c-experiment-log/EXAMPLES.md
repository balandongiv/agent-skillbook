# Examples: Strategy C Experiment Log

## Example 1: Logging an exploratory parameter sweep

### Before (without this skill)

```
Ran a few scan-scale values for Strategy C and kept the best one. No record of what was tried or why.
```

### After (with this skill applied)

```
## Strategy: Scan-scale sweep for Strategy C Stage 1
- Date: 2026-06-17
- Proposal: Sweep scan_scale in {0.05, 0.12, 0.20} to set the Stage 1 screening sensitivity.
- Rationale: Stage 1 recall bounds the whole pipeline; the current 0.12 was never compared.
- Status: Completed
### Implementation
- Files Changed: src/strategy_c/stage1.py
- Commits: <hash>
### Performance & Metrics
- Before / After / Change: macro-F1 0.81 -> 0.83 at 0.12 (source: runs/expC/summary.csv)
### Implementation Benefits
- Keeps a cleaner candidate-region contract for downstream stages than the A baseline.
### Issues Encountered / Outcome / Learnings
- 0.20 over-screened; 0.12 retained. Next time log per-session variance too.
```

### Why it's better

The experiment is traceable: rationale, files, metrics-with-sources, and a verdict future agents can build on.

---

## Example 2: Recording a dead end honestly

### Before (without this skill)

```
Tried an alternate Stage 1 estimator, it didn't help, moved on (nothing written down).
```

### After (with this skill applied)

```
## Strategy: Alternate Stage 1 estimator (variance-based)
- Date: 2026-06-17 | Status: Abandoned
- Outcome: No improvement (macro-F1 0.83 -> 0.82); added complexity.
- Implementation Benefits: None demonstrated over Strategy A/B.
- Learnings: Variance-based screening is more fragile to outlier epochs; do not retry without robust centering.
```

### Why it's better

The dead end is captured so the same unproductive path is not repeated, with an explicit "no benefit" note.
