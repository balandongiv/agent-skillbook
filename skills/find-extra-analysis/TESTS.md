# Test Prompts: Find Extra Analyses from Abstract or Results

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Here is my abstract — what extra analyses should I run to strengthen the paper?

Expected behavior: Extract claims/metrics, scan evidence axes, and return a feasibility-ranked list of
grounded analysis proposals.

---

## Test Prompt 2

> Read my results section and find gaps a reviewer would attack.

Expected behavior: Identify under-supported claims (robustness, baselines, statistics, generalisation)
and propose analyses that close each gap, with outcome interpretations.

---

## Test Prompt 3

> Suggest additional experiments, but only ones I can do with the data I already have.

Expected behavior: Prioritise proposals tagged as reusing existing artifacts and clearly separate them
from ones needing new data.

---

## Test Prompt 4

> This is a genomics results table — what further analyses make sense?

Expected behavior: Apply the domain-general evidence axes (ablation, robustness, stratified, stats) to
the provided table without assuming a specific field.

---

## Test Prompt 5

> Rank the extra analyses by how much they'd change my conclusions.

Expected behavior: Order proposals by impact-on-claims times feasibility and explain the ranking.
