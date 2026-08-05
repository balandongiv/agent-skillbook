# Manuscript Artifact Provenance and Generator Naming

## Overview

An analysis repository drifts: scripts accumulate, run directories multiply, experiments get
dropped from the paper but their code stays, and eventually nobody can answer "which script
made Table 4, and from which data?" This skill makes that question answerable by construction —
one artifact, one generator, one source of truth — and enforces the mapping mechanically so the
answer stays correct as the manuscript is revised.

## Core principles

1. **The filename states the artifact.** A script that produces a manuscript artifact is named
   for it: `tab4_strategy_comparison.py`, `fig7_pr_operating_points.py`,
   `tab13_fig10_epoch_duration.py` when one analysis yields both. Reading `ls` tells you the
   mapping without opening a file. Scripts that only produce intermediate data keep descriptive
   names — the convention marks the manuscript boundary.
2. **One source of truth for published numbers.** Exactly one directory backs the paper. Working
   directories (`runs/`, `runs0/`, `runs_second_iteration/`) are for iteration and must never be
   read by a generator. Encode the path in config, not in each script.
3. **One shared data layer.** Every generator imports the same module for loading results,
   aggregating, and writing `.tex`/figures. Duplicated loading logic is where two tables silently
   start disagreeing — one gets a filter fix and the other does not.
4. **The mapping is machine-checkable.** A manifest lists every artifact with its generator,
   its inputs, its aggregation rule, and its outputs. A `check` command fails when a generator,
   input, or output is missing. Prose documentation drifts; a failing command does not.
5. **Deleting an experiment means deleting all of it.** Scripts, config files, generated `.tex`,
   `\input` lines, section text, and cross-references. A half-removed experiment leaves undefined
   references and orphaned tables that compile fine and mislead a reader.
6. **A clean exit code is not evidence.** Verify the artifacts themselves — a generator can write
   an empty table, and LaTeX can compile a document with content silently missing.

## Step-by-step process

1. **Inventory what the manuscript actually uses.** Grep the LaTeX for `\input`, `\includegraphics`,
   `\label` and build the real list of tables and figures. Ignore what the scripts claim to make.
2. **Establish the source of truth.** Identify the one results directory whose numbers match the
   intended paper, and confirm what it actually contains — dimensions, conditions, sessions.
   Experiments absent from it cannot be in the paper.
3. **Write the artifact → generator map** (`FIGURE_TABLE_MAP.md` or equivalent) covering every
   artifact from step 1, and record which analyses are being dropped and why.
4. **Build or consolidate the shared data layer**: path resolution from config, loading,
   aggregation, escaping, and `.tex`/figure writing with a provenance comment in each output.
5. **Split monolithic generators** into one script per artifact group, named for the artifacts.
   A 400-line script writing twelve tables cannot be re-run for one of them.
6. **Delete dropped experiments completely** — scripts, configs, generated files, `\input` lines,
   LaTeX sections, and any table that indexed them.
7. **Encode the map as a manifest** with a `check` command, and run it.
8. **Regenerate everything from scratch** and confirm each output file is written and non-empty.
9. **Verify the manuscript compiles** with zero undefined references and citations.

## Rules

- Always name a manuscript-artifact generator for the artifact it produces.
- Always read published numbers from the single configured source-of-truth directory; never from
  a working run directory.
- Always route result loading and aggregation through the shared data layer.
- Always write a provenance comment into each generated `.tex` naming its source and generator.
- Always apply the same aggregation rule to every condition being compared, and state that rule
  in the manifest.
- Always delete a dropped experiment's scripts, configs, generated files, and LaTeX together.
- Always run the manifest check before a submission build.
- Never leave a generator whose output no artifact uses; delete it or wire it in.
- Never trust a script's docstring about its inputs — verify against the actual CSV columns.

## Failure modes this prevents

- **The empty-table bug.** A generator filters on a value that no longer exists in the CSV
  (`selection == "all"` after the column was renamed to `"all_channel"`), producing an empty
  table that compiles without complaint.
- **The overwritten-mapping bug.** A channel-to-region map built by iterating a config where a
  catch-all group appears last silently relabels every entry with the catch-all.
- **The stale-row bug.** A hand-maintained "this work" row in a comparison table keeps numbers
  from an earlier run. Generate such rows from the results like any other.
- **The wrong-column bug.** Two generators load the same CSV independently; one gets a fix and
  the other keeps producing numbers that disagree with it.
- **The ghost experiment.** A section describes an analysis whose data was never carried into the
  final results, leaving undefined references or, worse, a plausible stale table.

## Common mistakes to avoid

- **Renaming scripts without updating the map** — the convention only helps if it stays true.
- **Keeping "just in case" scripts** — they get run by accident and produce contradictory outputs.
- **Documenting the mapping only in prose** — it drifts within weeks; make it executable.
- **Numbering scripts before the manuscript settles** — renumber when the paper renumbers, and
  keep the map as the authority.
- **Fixing a wrong number in the `.tex` by hand** — the generator will overwrite it on the next
  run. Fix the generator.

## Additional guidance

Numbering ties scripts to the manuscript's own figure and table numbers, which is what makes the
convention useful during review ("regenerate Table 6" is unambiguous). Accept that a renumbering
of the paper means renaming scripts; that cost is small next to the ambiguity it removes.

Pair this skill with `manuscript-final-qc` (the rendered-document gate) and
`academic-latex-writer` (which grounds prose in the artifacts this skill keeps trustworthy).
