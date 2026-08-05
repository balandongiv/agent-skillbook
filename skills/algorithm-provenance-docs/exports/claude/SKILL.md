---
name: algorithm-provenance-docs
description: Document every explored algorithm with a fixed integration report — source paper/repo, hypothesis, method, pre-registered falsifiers, exploratory results with caveats, and how to select, run, and test it independently — so future agents can evaluate or modify it without reconstructing history.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Algorithm Provenance Documentation

## Overview

When many algorithms are explored and then consolidated into one repository, the code alone is
not enough: a future agent must be able to understand *why* each method exists, *where* it came
from, *what* it claimed, and *how* to run and test it — without reconstructing the history from
commits. This skill defines a **fixed per-algorithm integration report** so every method is
documented the same way, is independently selectable and testable, and carries honest,
exploratory provenance.

## Core principles

1. **One report per algorithm, same shape every time.** Each algorithm gets a
   `docs/algorithms/<name>.md` following an identical section order, so reports are comparable
   and a reader always knows where to find provenance, method, results, and how-to-run.
2. **Provenance is mandatory.** Record the source paper (and where it lives in the reference
   list), the source repository if any, the method it implements, and the hypothesis it tests.
   Ground every claim in a real reference — never invent a citation.
3. **Falsifiers, not just results.** State the pre-registered conditions under which the method
   would be rejected (correlation caps, residual floors, permutation deltas), alongside the
   results — so the report shows how the method was tested, not just that it "worked".
4. **Results carry their caveat.** Report the split (which subjects/sessions), the n, and that
   the figures are exploratory for method comparison, not general performance. Compare against
   the baseline. Never let a small-split number read as a general claim.
5. **Independently selectable, runnable, testable.** Document the stable selector name, the
   module path, the thin runner script, and the unit test — so the algorithm can be chosen,
   executed, and verified on its own.
6. **Lean and single-source.** Point at the shared harness and single-source modules the
   algorithm reuses; do not restate their internals. The report links, it does not duplicate.
7. **Future-agent test.** The report passes if a new agent can, from it alone, understand the
   idea, find its code, run it, test it, and know what would falsify it — with no git archaeology.

## The fixed report sections

Write each `docs/algorithms/<name>.md` with these sections, in order:

1. **Name & one-line summary** — stable selector + what it does.
2. **Provenance** — source paper (+ where it is listed), source repo, branch/idea origin.
3. **Hypothesis** — the claim the method tests.
4. **Method** — how it works, at a level a new agent can follow; link the shared harness it reuses.
5. **Inputs / modalities** — which signals/channels it uses.
6. **Pre-registered falsifiers** — the reject conditions fixed before running.
7. **Results (exploratory)** — split, n, scores, baseline comparison, and the caveat.
8. **How to select / run / test** — selector name, module path, runner script, unit test command.
9. **Status & limitations** — what is unresolved, what would change the conclusion.

## Step-by-step process

1. **Gather provenance** from the reference list and the workstream that built the algorithm.
2. **Fill the fixed sections** in order; keep the shape identical to the other reports.
3. **State falsifiers and results together**, with the split, n, baseline, and exploratory caveat.
4. **Record the how-to-run**: selector name, module path, runner, and the exact test command.
5. **Link, don't duplicate** the shared harness and single-source modules.
6. **Cross-check the registry/index** so the doc path, selector name, and modalities match the
   code, and add the report to the catalogue/README.
7. **Apply the future-agent test**: can someone act on this report without the git history? If
   not, fix the gap.

## Rules

- Always use the same fixed section order for every algorithm report.
- Always record provenance (paper + where listed, repo, origin) and ground claims in real references.
- Always state pre-registered falsifiers alongside results.
- Always attach split, n, baseline comparison, and the exploratory caveat to any result.
- Always document the selector name, module path, runner, and unit-test command.
- Never duplicate shared-harness internals in the report; link to the single source.
- Never let a small-split exploratory number read as a general performance claim.

## Common mistakes to avoid

- **Results without provenance.** A score with no paper/repo/hypothesis is unreusable and
  unverifiable. Provenance is mandatory.
- **Missing falsifiers.** Reporting only what passed hides how (or whether) the method was
  tested. Include the reject conditions.
- **Over-claiming.** A three-session number written as general performance. Attach split, n,
  baseline, and caveat.
- **No how-to-run.** A report a future agent cannot act on. Give the selector, module, runner,
  and test command.
- **Duplicating the harness.** Restating shared evaluation/matching logic per report causes
  drift. Link to the single source.
- **Inconsistent shape.** Reports that each use a different structure are not comparable. Keep
  the fixed section order.
