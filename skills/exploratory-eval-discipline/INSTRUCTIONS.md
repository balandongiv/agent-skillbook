# Exploratory Evaluation Discipline

## Overview

On small research datasets — a handful of subjects, a few sessions — it is dangerously easy
to fool yourself: a method looks strong on one split, or it "wins" only because it re-encodes a
trivial signal, and the number gets quoted as if it were general performance. This skill keeps
exploratory method comparison honest. Before running, you **pre-register falsifiers**; you
separate a **leave-one-subject-out (LOSO) development split** from a **held-out evaluation
split**; you require every candidate to **beat the simplest baseline**; and you never state
general performance from a small development split.

## Core principles

1. **Pre-register falsifiers before you run.** For each method, write down — in advance — the
   conditions under which you will *reject* it, not just accept it. Examples: "its score must
   not correlate above r with the trivial cue"; "the residual AUROC after removing the baseline
   signal must exceed t"; "a channel/feature permutation must drop AUC by at least d". A method
   that only survives because the criteria were invented afterward has not been tested.
2. **Separate development from held-out evaluation.** Tune, select, and iterate only on the
   development split (LOSO across subjects so no subject trains and tests itself). Touch the
   held-out split **once**, at the end, to read out — never to tune. A number you optimized
   against is not an estimate of generalization.
3. **Beat the simplest baseline or it does not count.** Keep an untuned, obvious baseline
   (e.g. a single interpretable scalar) as the bar. A complex method that does not clearly beat
   that baseline on the held-out split has not earned adoption, regardless of its development
   score.
4. **Watch for leakage and trivial-cue shortcuts.** If a method's output is highly correlated
   with a simple cue it was supposed to improve on, it is probably re-encoding that cue. The
   pre-registered correlation/residual falsifiers exist to catch exactly this.
5. **Report exploratory numbers as exploratory.** State the split (which subjects/sessions), the
   n, and that the figures are for *method comparison*, not general performance. Expect them to
   change under a larger, audited evaluation, and say so.
6. **Consider the label ceiling.** When many methods plateau at the same modest score, suspect
   the labels, not just the models. Mislabeled or unannotated events cap achievable performance;
   note this as a hypothesis to test by auditing labels, not as a model failure.

## Step-by-step process

1. **Define splits first.** Fix the LOSO development subjects/sessions and the held-out
   evaluation set before running anything. Do not move items between them later.
2. **Pre-register criteria.** For each method, write the accept thresholds *and* the falsifiers
   (correlation caps, residual-AUROC floors, permutation deltas) into a note before the run.
3. **Fix the baseline.** Record the simple baseline's development and held-out scores as the bar.
4. **Develop on LOSO only.** Iterate, tune, and select using the development split. Keep the
   held-out set sealed.
5. **Run the falsifiers.** Reject any method that trips a pre-registered falsifier, even if its
   headline score looks good.
6. **Read out held-out once.** Evaluate the surviving methods on the held-out split a single
   time; compare against the baseline.
7. **Report honestly.** Give the split, n, the baseline comparison, and the exploratory caveat.
   If methods plateau together, flag the label-ceiling hypothesis.

## Rules

- Always pre-register falsifiers before running; never invent pass criteria after seeing results.
- Always keep development (LOSO) and held-out splits separate; touch held-out only once, to read out.
- Always require a candidate to beat the simple baseline on held-out before adopting it.
- Always check whether a "winning" method just re-encodes a trivial cue (correlation/residual test).
- Never quote a small development-split number as general performance; state the split, n, and caveat.
- When many methods plateau together, flag the label-ceiling hypothesis instead of assuming model failure.

## Common mistakes to avoid

- **Post-hoc criteria.** Deciding what counts as success after seeing the numbers. Write
  falsifiers first.
- **Tuning on the held-out set.** Any selection against held-out turns it into a second
  development set and destroys the generalization estimate.
- **Ignoring the baseline.** Reporting a method's absolute score without comparing to the simple
  baseline hides that it may add nothing.
- **Missing leakage.** Accepting a method whose output is ~identical to the cue it claimed to
  improve. Run the correlation/residual falsifier.
- **Over-claiming.** Presenting a few-subject development number as general performance. Always
  attach the split, n, and exploratory caveat.
- **Blaming the model for a label ceiling.** When everything plateaus, audit the labels before
  concluding the methods failed.
