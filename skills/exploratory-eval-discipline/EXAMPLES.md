# Examples: Exploratory Evaluation Discipline

---

## Example 1: Pre-registering falsifiers instead of post-hoc criteria

### Before (without this skill)

```text
Run the new feature classifier.
Held-out F1 = 0.71. "Great, it works — ship it."
(No baseline comparison; success defined after seeing the number.)
```

### After (with this skill applied)

```text
Before running, write into the note:
- ACCEPT if held-out long-F1 clearly beats the baseline scalar (0.63).
- REJECT (falsifier) if the method's score correlates with the trivial duration cue at r > 0.90.
- REJECT if residual AUROC after removing the baseline signal <= 0.55.
- REJECT if a channel-permutation drops AUC by < 0.05 (method isn't using the channels).
Then run, apply the falsifiers, and only then read held-out once.
```

### Why it's better

The method is judged against criteria fixed in advance, so a good-looking number that only
re-encodes the trivial cue is caught instead of celebrated.

---

## Example 2: Development vs held-out, and beating the baseline

### Before (without this skill)

```text
Tune the model on all subjects.
Report the best split's F1 as the method's performance.
```

### After (with this skill applied)

```text
1. Fix splits first: LOSO development subjects; a sealed held-out set.
2. Iterate and select ONLY on LOSO development.
3. Baseline (untuned scalar): dev ~0.55, held-out ~0.63 — this is the bar.
4. Candidate: dev 0.82 but held-out 0.51 -> does NOT beat baseline held-out -> not adopted.
5. Report: "held-out long-F1 0.51 vs baseline 0.63 on the 8-subject held-out split (exploratory)."
```

### Why it's better

The held-out set is read once and never tuned against, and the candidate is judged against the
simple baseline — exposing that a strong development score did not generalize.

---

## Example 3: Reporting a small-sample result honestly

### Before (without this skill)

```text
"Our method achieves F1 0.82 on blink sub-classification."
```

### After (with this skill applied)

```text
"On three development sessions (LOSO) the method reaches 0.82; on the 8-subject held-out split
it reaches 0.51 vs the 0.63 baseline. These are exploratory figures for method comparison on a
small split (n subjects stated), not general performance, and are expected to change under a
larger, audited-label evaluation. Several methods plateau near ~0.6, which points at a possible
label ceiling (mislabeled/unannotated events) to audit."
```

### Why it's better

The claim carries its split, n, baseline comparison, and caveat, and it surfaces the
label-ceiling hypothesis instead of implying a general result.
