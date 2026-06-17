# Write Discussion Section with Defensible Claims

## Overview

Write a discussion that interprets the reported results honestly: what they mean, how they relate to
prior work, what is genuinely novel, and where the study is limited — without overclaiming. Every
interpretation must be anchored to a result already in the results section, and causal/novelty language
must stay defensible. The discussion adds meaning, not new numbers.

## Core principles

1. **Anchor every interpretation to a reported result** — Do not introduce new measurements; refer to
   the numbers/tables already in the results. If you need a number that is not reported, that is a
   results problem, not a discussion sentence.
2. **Defensible language by default** — Prefer "suggests", "is consistent with", "may", "to our
   knowledge, among the first", "within the tested conditions". Avoid "proves", "guarantees", "causes",
   "universally", "first ever", and unqualified "novel".
3. **Match claims to evidence direction** — Causal/mechanism statements must align with what the data
   actually show; keep the strength hedged unless an ablation/derivation establishes the direction.
4. **Limitations are honest and specific** — A dedicated limitations paragraph grounded in the real
   scope: datasets, design choices, untested conditions, missing comparisons, generalisation threats.
5. **No unsupported contribution claims** — Do not claim analyses or capabilities the paper does not
   actually report (cross-check with a claim/citation audit).

## Step-by-step process

1. **Read the results** and list the key findings worth interpreting (and their exact references).
2. **Draft the main-implication paragraph(s)**: what the headline result means, tied to the reported
   values and tables.
3. **Relate to prior work** using only library-backed citations; contrast rather than restate.
4. **Calibrate strength**: convert any causal/absolute/novelty wording to hedged, defensible forms.
5. **Write the limitations paragraph** covering dataset scope, method assumptions, missing baselines
   (e.g. no deep-learning comparison), preprocessing/annotation specificity, and generalisation.
6. **Add a measured novelty statement** ("to our knowledge, among the first ...") only if supportable.
7. **Audit** the section: every claim atomised, every citation relevant, no number beyond the results,
   no overclaim words left.

## Rules

- Always anchor interpretations to results already reported; never introduce new numbers here.
- Always use hedged, defensible language for causal and novelty claims.
- Always include an honest, specific limitations paragraph.
- Never use "proves/guarantees/causes/universally/first ever" or unqualified "novel".
- Never claim a contribution or analysis the paper does not actually report.

## Common mistakes to avoid

- **Causal overreach** — "X causes Y" from a correlational/observational result.
- **Novelty inflation** — "the first study" without the "to our knowledge, among the first" hedge.
- **New numbers in the discussion** that never appeared in the results.
- **Vague limitations** ("more work is needed") instead of specific, scope-grounded ones.
- **Restating results** instead of interpreting them.

## Common softening map

- "proves / demonstrates conclusively" -> "suggests / is consistent with"
- "causes / biases upward" -> "may distort / may bias / tends to"
- "the first study" -> "to our knowledge, among the first"
- "universally improves / always" -> "improves within the tested conditions / across the evaluated datasets"

## Additional guidance

Keep one idea per paragraph (main implication, mechanism, prior-work relation, epoching/method nuance,
limitations, novelty). This skill pairs with `write-results-section` (the anchor), `citation-audit` and
`atomise-claims` (overclaim/citation checks), and `literature-review-writing` (library-backed prior-work
citations). When revising an existing discussion, soften flagged claims in place and update any stale
numbers to match the current results.
