---
name: hyperparameter-search-strategy
description: Choose efficient hyperparameter search strategies for finding optimal parameter sets or parameter pairs, favoring random search, Bayesian optimization, successive halving, evolutionary methods, or population-based training over brute-force grids. Use when an experiment, detector, or training pipeline must tune parameters under compute and evaluation-cost constraints.
---

# Hyperparameter Search Strategy

Use this skill when the core problem is not "run the experiment" but "decide how to search for a better parameter setting." The main responsibility of this skill is to choose a search strategy that matches the shape of the search space and the cost of evaluation. Do not default to brute-force grid search unless the space is genuinely tiny and exhaustive enumeration is clearly cheaper and simpler than anything smarter.

Treat search strategy as an engineering decision with tradeoffs. You must define the objective, the budget, and the evaluation protocol before recommending a method. A good answer explains why the chosen search method fits the detector or training loop, what compute budget it assumes, what evidence will count as improvement, and how the rationale will be recorded in experiment metadata.

---

## Core principles

### 1. Start with the objective and budget

Identify the metric to optimize, the evaluation cost per trial, the acceptable wall-clock budget, and any resource limits. A search method is only appropriate relative to these constraints.

### 2. Do not assume grid search

Brute-force grid search wastes trials in large or mixed spaces because it evaluates many unimportant combinations. Use it only when the total number of combinations is truly small and exhaustive search is obviously the cheapest correct option.

### 3. Match the method to the search space

Choose the method based on:

- number of parameters
- continuous versus discrete dimensions
- conditional or irregular structure
- whether partial evaluations are meaningful
- cost and noise of each evaluation

### 4. Record the rationale

Always record the chosen strategy, search space, budget, seeds, stopping rule, and rationale in experiment metadata or the run note.

### 5. Separate tuning from final evaluation

Use validation data, cross-validation, or another tuning-safe protocol during the search. Keep the final test or held-out evaluation out of the tuning loop.

---

## Method selection guide

### Use random search as the default baseline

Prefer random search when the space is large, mixed, or only a few parameters matter strongly. Random search usually beats coarse grids for the same budget because it covers more unique combinations.

### Use Bayesian optimization when evaluations are expensive

Prefer Bayesian optimization when:

- each evaluation is expensive
- the search space is reasonably structured
- you can benefit from model-based trial selection

Bayesian optimization is usually a strong choice when you expect relatively few trials and want each next trial to use information from earlier ones.

### Use successive halving or Hyperband when weak candidates can be discarded early

Prefer successive halving or Hyperband when:

- the training or evaluation loop is iterative
- early results are predictive enough to rank candidates
- partial-resource evaluations are much cheaper than full evaluations

This is often the best choice for model-training workflows where poor candidates can be stopped after a few epochs or batches.

### Use evolutionary methods for irregular or conditional spaces

Prefer evolutionary algorithms when:

- the search space has conditional branches
- parameters interact in non-smooth or highly non-convex ways
- mutation and selection are easier to express than a structured surrogate model

Evolutionary methods are especially useful when candidate representations are awkward for grid or Bayesian approaches.

### Use population-based training only for iterative training with online adaptation

Use population-based training only when the model or detector supports iterative training and can adapt hyperparameters during the run. Do not recommend it for one-shot evaluators or static scoring pipelines.

### Allow exhaustive enumeration only when it is clearly cheap

Exhaustive enumeration is acceptable when the space is small, discrete, and cheap enough that smarter optimization adds complexity without savings. State the combination count and explain why enumeration is cheaper.

---

## Step-by-step process

### Step 1: Define the search problem

Write down:

- objective metric
- candidate parameters and ranges
- any parameter pairs or dependencies
- evaluation dataset or protocol
- compute budget
- stopping rule

### Step 2: Classify the search space

Determine whether the space is:

- small or large
- continuous, discrete, or mixed
- regular or conditional
- cheap or expensive to evaluate
- compatible with early stopping or not

### Step 3: Choose the search strategy

Select the method that best matches the space and budget:

- random search for large or mixed spaces
- Bayesian optimization for expensive structured evaluations
- successive halving or Hyperband for iterative workflows with useful partial signals
- evolutionary methods for irregular or conditional spaces
- population-based training for iterative training with online adaptation
- exhaustive enumeration only for tiny cheap spaces

Explain the choice plainly.

### Step 4: Define fairness and reproducibility

Hold constant what should stay constant across trials. Specify seeds, evaluation splits, resource caps, and any repeated runs needed to reduce noise. Compare candidates under the same rules.

### Step 5: Record and review outcomes

For every search, record at minimum:

- strategy used
- reason for choosing it
- search budget
- best parameter set
- best observed metric
- whether the result was reconfirmed on a repeated or held-out evaluation

Do not call a configuration "optimal" until it survives a sensible confirmation step.

---

## Rules

- Never default to brute-force grid search without a concrete justification.
- Always state the metric, budget, and evaluation protocol before recommending a search method.
- Always record why the chosen method fits the detector or training loop.
- Always keep the final test evaluation outside the tuning loop.
- Always compare candidates under a fair and consistent budget.
- Prefer random search as the default baseline for large or mixed spaces.
- Prefer Bayesian optimization when trials are expensive and the space is structured enough for model-based selection.
- Prefer successive halving or Hyperband when weak candidates can be cut early.
- Prefer evolutionary methods for irregular or conditional spaces.
- Use exhaustive enumeration only when the discrete space is plainly small and cheap.

---

## Common mistakes to avoid

- **Grid search by habit**: A large grid feels systematic, but it often wastes budget on unimportant combinations.
- **No explicit budget**: Without a budget, any search strategy recommendation is incomplete.
- **Tuning on the test set**: This inflates confidence and invalidates the final evaluation.
- **Unfair trial comparisons**: Changing seeds, data splits, or resource limits between candidates makes the comparison noisy and misleading.
- **Choosing Bayesian optimization for a badly structured conditional space**: A surrogate model may struggle if the space is too irregular.
- **Using Hyperband when partial progress is not predictive**: Early stopping only helps if early performance says something useful about final performance.
- **Declaring victory from one lucky trial**: Reconfirm the best setting before treating it as the new default.

---

## Condensed decision rules

- Large or mixed space: start with random search.
- Expensive structured evaluations: consider Bayesian optimization.
- Iterative training with meaningful early signals: use successive halving or Hyperband.
- Irregular or conditional space: consider evolutionary search.
- Online hyperparameter adaptation during training: use population-based training.
- Tiny cheap discrete space: exhaustive enumeration is acceptable with explicit justification.
