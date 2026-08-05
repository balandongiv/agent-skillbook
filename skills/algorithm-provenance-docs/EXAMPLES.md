# Examples: Algorithm Provenance Documentation

---

## Example 1: From a bare code drop to a provenance report

### Before (without this skill)

```text
docs/algorithms/tonic-eog.md:
"Tonic EOG classifier. Gets 0.58 F1. See the code."
```

### After (with this skill applied)

```text
docs/algorithms/tonic-eog.md  (fixed sections):
1. Name & summary   : tonic_eog — classify events by the tonic EOG standing-potential step.
2. Provenance       : <paper title> (listed in setting/academic_reference.csv, key ...);
                      origin branch agent/ml/tonic-eog.
3. Hypothesis       : a sustained closure shifts the tonic EOG level more than a normal blink.
4. Method           : window the event, measure the tonic step; reuses the shared
                      match/metrics harness (link) — not restated here.
5. Inputs           : EOG channels.
6. Falsifiers       : reject if score correlates with plateau duration r > 0.90;
                      reject if residual AUROC <= 0.55.
7. Results (exploratory): dev (3 sessions, LOSO) 0.61; held-out (8 subj) 0.58 vs baseline 0.63.
                      Exploratory, method comparison only — not general performance.
8. Run/test         : selector "tonic_eog"; module .../tonic_eog_features.py;
                      scripts/run_tonic_eog.py; pytest tests/test_tonic_eog.py -q.
9. Status           : does not beat baseline held-out; label ceiling suspected.
```

### Why it's better

A future agent can understand the idea, its source, what would falsify it, how it scored (with
caveat), and how to run and test it — from the report alone, with no git archaeology.

---

## Example 2: Keeping results honest and linked, not duplicated

### Before (without this skill)

```text
"Achieves F1 0.82 on blink sub-classification."
(pastes a copy of the event-matching and metric code into the doc)
```

### After (with this skill applied)

```text
Results (exploratory): 0.82 on 3 development sessions (LOSO); 0.51 on the 8-subject held-out
split vs the 0.63 baseline. Exploratory figures for method comparison, expected to change under
a larger audited-label evaluation.

Method: event matching and metrics use the shared harness (see docs/architecture.md and
detection/evaluation.py) — not reproduced here.
```

### Why it's better

The number carries its split, n, baseline, and caveat, and the report links the single-source
harness instead of duplicating it (which would drift out of sync).

---

## Example 3: Cross-checking the report against the registry

### Before (without this skill)

```text
Doc says module "eog_tonic.py", selector "tonicEOG", modality "eeg".
Registry says module "tonic_eog_features.py", name "tonic_eog", modality "eog".
```

### After (with this skill applied)

```text
1. Read the registry entry for the algorithm.
2. Make the doc's selector name, module path, runner, and modalities match it exactly.
3. Add the report to docs/algorithms/README.md (the catalogue).
```

### Why it's better

The documentation and the code agree, so selecting/running the algorithm from the report
actually works.
