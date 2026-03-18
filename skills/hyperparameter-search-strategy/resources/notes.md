# Notes: Hyperparameter Search Strategy

Decision hints to preserve across experiments:

- use random search as the default baseline for large or mixed spaces
- use Bayesian optimization when evaluations are expensive and the space is well structured
- use successive halving or Hyperband when weak candidates can be discarded early
- use evolutionary methods for irregular or conditional spaces
- use population-based training only for iterative training with online adaptation
- allow exhaustive enumeration only when the discrete space is clearly tiny and cheap

Always record:

- objective metric
- search budget
- search space definition
- chosen strategy and rationale
- best configuration and confirmation result
