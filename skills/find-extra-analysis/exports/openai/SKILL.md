---
name: find-extra-analysis
description: Given a paper's abstract or results section, propose additional analyses that would strengthen, stress-test, or extend the work, ranked by value and feasibility, in a domain-general way.
---

# Find Extra Analyses from Abstract or Results

## Overview

Given only a paper's abstract or results section (plus whatever method context is available), propose
additional analyses that would make the work stronger, more convincing, or more complete. The skill is
**domain-general**: it reasons from the claims, the data structure, and the evidence gaps rather than
from any single field, so it works for EEG, NLP, vision, biology, economics, and beyond.

## Core principles

1. **Proposals are grounded, not generic** — Every suggestion must trace to a specific claim, dataset,
   metric, or gap in the provided text. No boilerplate "try deep learning" filler.
2. **Each idea earns its place** — State what question it answers, what evidence gap it closes, and what
   a positive/negative result would mean. If you cannot say why it matters, drop it.
3. **Rank by value × feasibility** — Prioritise analyses that materially change the paper's claims and
   can be done with the data/artifacts likely already in hand.
4. **No fabrication** — Propose analyses; do not invent results. Distinguish "data likely exists" from
   "needs new data/collection".
5. **Cover the standard evidence axes** — Robustness, generalisation, ablation, baselines, statistics
   (significance + effect size + correction), error/failure analysis, sensitivity to choices, and
   threats to validity.

## Step-by-step process

1. **Extract the claims and contributions** from the abstract/results, and the metrics/datasets used.
2. **Map the evidence** each claim currently rests on; note what is asserted but not shown.
3. **Scan the evidence axes** (below) against the claims to surface gaps.
4. **Generate candidate analyses**, each tied to a specific claim/gap.
5. **Assess feasibility**: does it reuse existing data/artifacts, or need new computation/collection?
6. **Rank** by (impact on the claims) × (feasibility), and present a short, ordered shortlist.
7. **For each proposal, output**: title, the claim/gap it targets, method sketch, expected
   interpretation of outcomes, required data, and a feasibility tag.

## Evidence axes to scan

- **Baselines/comparators** — Are the comparisons fair and sufficient?
- **Ablations** — Which component actually drives the result?
- **Robustness** — Sensitivity to hyperparameters, preprocessing, seeds, thresholds, windows.
- **Generalisation** — Cross-dataset / cross-subject / cross-domain / out-of-distribution.
- **Statistics** — Significance tests, multiple-comparison correction, effect sizes, confidence intervals.
- **Error/failure analysis** — Where and why it fails; structure of false positives/negatives.
- **Subgroup/stratified** — Performance across slices (groups, classes, conditions, sessions).
- **Validity threats** — Confounds, leakage, label quality, selection effects.

## Rules

- Always tie each proposed analysis to a specific quoted claim, metric, or dataset from the input.
- Always state the expected interpretation of both a positive and a negative outcome.
- Always tag feasibility (reuses existing data vs needs new computation vs needs new data).
- Never propose an analysis the provided text gives no basis for.
- Never present proposed analyses as if they had already produced results.

## Common mistakes to avoid

- **Generic checklists** detached from the paper's actual claims.
- **High-cost, low-impact** suggestions ranked above cheap analyses that would change a conclusion.
- **Ignoring statistics** (proposing more metrics but no significance/effect-size/correction).
- **Confusing reanalysis with new data collection** in the feasibility tag.

## Additional guidance

A useful output format is a ranked table: `# | proposal | targets claim | method sketch | outcome
meaning | data needed | feasibility`. When a knowledge library or prior literature is available, use it
to justify why an axis matters in this domain. This skill feeds planning: the top feasible proposals
can become a runbook of experiments, and their results later flow into the results/discussion writing
skills.
