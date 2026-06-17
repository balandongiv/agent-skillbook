# Examples: Find Extra Analyses from Abstract or Results

## Example 1: Grounded proposals vs generic filler

### Before (without this skill)

```
Suggestions: try more models, add more data, use deep learning, report more metrics.
```

### After (with this skill applied)

```
Input claim: "Method M beats baselines B1, B2 on dataset D (macro-F1)."

1. Cross-dataset generalisation [feasibility: reuse if 2nd dataset exists]
   Targets: the implicit generalisation claim. Run M and baselines on a second dataset D2.
   Outcome meaning: small gap -> transfers; large gap -> dataset-specific.
2. Paired significance + effect size [feasibility: reuse existing per-item scores]
   Targets: "beats baselines". Wilcoxon on matched items, correct for multiple comparisons, report
   effect size. Outcome: confirms whether the F1 gap is statistically real.
3. Error-structure analysis [feasibility: reuse predictions]
   Targets: why M wins. FP:FN ratio per method. Outcome: reveals precision/recall trade-off regime.
```

### Why it's better

Each proposal names the claim it tests, what data it needs, and how to read the result — actionable
instead of generic.

---

## Example 2: From an abstract sentence to a feasibility-ranked shortlist

### Before (without this skill)

> Abstract: "Our thresholding pipeline is robust across epoch durations and channels."

A reviewer just asks "is it really robust?"

### After (with this skill applied)

```
Robustness is claimed twice (epoch duration, channels) but may be unquantified. Proposals:
A. Epoch-duration sweep with significance vs a reference duration  [reuse: likely]
B. Channel-robustness: cross-method agreement on selected channel  [reuse: likely]
C. Sensitivity to the screening threshold parameter                [reuse: likely]
Ranked A > B > C: A directly substantiates the headline "robust across epoch durations" claim and is
cheap if per-duration scores exist.
```

### Why it's better

The vague "robust" claims are turned into specific, prioritised analyses that would actually back them.
