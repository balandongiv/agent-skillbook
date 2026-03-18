# Examples: Hyperparameter Search Strategy

---

## Example 1: Replacing a wasteful grid with random search

### Before (without this skill)

```text
Tune a detector over:
- threshold: 0.05 to 0.95 in steps of 0.05
- smoothing window: 3, 5, 7, 9, 11
- refractory period: 50, 75, 100, 125, 150

Run the full grid because it is the most complete approach.
```

### After (with this skill applied)

```text
1. Define the objective metric and the trial budget.
2. Classify the space as mixed and moderately large.
3. Choose random search as the default baseline.
4. Sample a fixed number of trials, for example 80 to 120, under the same validation protocol.
5. Record in experiment metadata:
   - strategy: random search
   - rationale: large mixed space; grid is wasteful
   - budget: N trials
   - best parameter set and metric
6. Reconfirm the best setting on a repeated or held-out validation run.
```

### Why it's better

Random search covers more unique combinations for the same budget and avoids spending most of the budget on a rigid grid that may over-sample unimportant dimensions.

---

## Example 2: Using Hyperband for iterative training

### Before (without this skill)

```text
Train 60 model configurations to full completion.
Only compare them after every run reaches the final epoch.
```

### After (with this skill applied)

```text
1. Recognize that training is iterative and early metrics are informative.
2. Choose successive halving or Hyperband.
3. Start many candidates with a small resource budget.
4. Promote only the stronger candidates to larger budgets.
5. Fully train the survivors and compare them under the same final evaluation rule.
6. Record why early stopping was valid for this pipeline.
```

### Why it's better

The improved approach spends less compute on weak candidates and concentrates the budget on promising ones, which is exactly what successive halving and Hyperband are designed to do.

---

## Example 3: Allowing exhaustive enumeration in a tiny space

### Before (without this skill)

```text
We should use Bayesian optimization because advanced methods are always better.
The search space is:
- threshold pair A/B: 3 choices
- voting rule: 2 choices
```

### After (with this skill applied)

```text
1. Count the combinations: 3 x 2 = 6.
2. Note that each evaluation is cheap.
3. Choose exhaustive enumeration.
4. Record the rationale: the space is tiny and enumeration is cheaper and simpler than a more complex optimizer.
```

### Why it's better

This version uses the simplest method that is actually appropriate. The skill does not ban exhaustive search outright; it only requires explicit justification when enumeration is the right answer.
