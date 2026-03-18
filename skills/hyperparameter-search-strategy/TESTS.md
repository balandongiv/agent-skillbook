# Test Prompts: Hyperparameter Search Strategy

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "I need the best threshold and window-size pair for this detector, but grid search will take too long."

Expected behavior: The agent recommends a more efficient search method, explains why brute-force is a poor default here, and defines the objective and budget first.

---

## Test Prompt 2

> "Help me choose between random search and Bayesian optimization for tuning these model parameters."

Expected behavior: The agent compares the two strategies based on evaluation cost, search-space structure, and budget instead of giving a generic answer.

---

## Test Prompt 3

> "This training pipeline can stop weak candidates after a few epochs. What search strategy should we use?"

Expected behavior: The agent recommends successive halving or Hyperband, explains why early stopping is useful here, and describes the assumptions required.

---

## Test Prompt 4

> "The parameter space is mixed and partly conditional. What tuning method fits best?"

Expected behavior: The agent avoids default grid search, considers random or evolutionary methods, and explains how irregular structure affects the choice.

---

## Test Prompt 5

> "There are only eight parameter combinations. Do we really need something fancier than checking all of them?"

Expected behavior: The agent allows exhaustive enumeration if it is clearly cheaper and simpler, and explicitly states that the exception is justified by the tiny search space.
