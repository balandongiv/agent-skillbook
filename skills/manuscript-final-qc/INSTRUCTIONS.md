# Manuscript Final Compile QC Gate

## Overview

A finished manuscript can still ship with defects that the writing tools never catch: a stale term the project
banned, a leftover draft note that rendered into the PDF, an undefined citation, or a number that no longer
matches its source CSV. This skill is the **final gate** run on the *rendered* document — it compiles the paper
and mechanically checks the output before submission or hand-off. It changes no content; it verifies and reports.

## Core principles

1. **Check the rendered PDF, not just the source.** A `.tex` comment is invisible, but live text — including
   editorial notes someone forgot to comment out — renders. Grep the `pdftotext` output, not only the sources.
2. **Numbers must trace to artifacts.** Every headline figure in a table/abstract must match the CSV or result
   file that produced it. Spot-check several; a mismatch is a blocking defect, not a rounding nit.
3. **Zero undefined, zero forbidden, zero leaked notes.** These are pass/fail gates, not warnings to triage.
4. **Verify, do not edit (by default).** The gate reports defects. Fix only clear, low-risk leaks (e.g. delete a
   stray draft row) and then re-compile; escalate anything that needs a content decision.

## Step-by-step process

1. **Compile manually and deterministically.** If `latexmk` is unreliable in the environment, run the explicit
   chain from the manuscript dir: `pdflatex -interaction=nonstopmode main` -> `biber main` (or `bibtex`) ->
   `pdflatex` -> `pdflatex`. Use the project's intended TeX/conda environment.
2. **Undefined references/citations:** scan `main.log` for `undefined` (case-insensitive). Report the count and,
   if non-zero, the exact missing labels/keys. Target: 0.
3. **Forbidden domain terms:** `pdftotext main.pdf - | grep -Ei '<project forbidden terms>'` (e.g. excluded
   methods, removed datasets). Target: 0. Maintain the forbidden list per project.
4. **Leaked draft/editorial notes:** grep the PDF text for placeholder/draft patterns —
   `TODO|FIXME|XXX|TBD|pending refresh|placeholder|lorem|we recommend|should be recomputed|draft|do not cite`.
   Any hit in rendered text is a defect (a real one bit a prior run: a "Pending refresh" table row + caption).
   Check both the offending row AND any caption/lead-in that references it.
5. **Numeric spot-checks:** pull 3-5 headline numbers from tables/abstract and confirm each against its source
   CSV/JSON (read the artifact, compare to the stated value at the stated precision). Report pass/fail per number.
6. **Coverage:** confirm every `\input` table/figure resolves and is referenced; flag orphan tables/figures not
   `\input` anywhere and any result discussed without a backing output (or vice versa).
7. **Section-vs-implementation consistency** (when applicable): confirm the Method text matches the actual
   code/config (dataset counts, filters, epoch settings, metrics, statistics) — not an aspirational description.
8. **Report** a single machine-readable verdict line plus a short markdown report. Re-run the full gate after any
   fix so the final PDF is the verified one.

## Rules

- Always grep the rendered PDF text (`pdftotext`), not just the `.tex`, for forbidden terms and draft notes.
- Always re-compile and re-check after fixing a leak — never report on a stale PDF.
- Never "fix" a numeric mismatch by editing the manuscript number to match a guess; trace it to the artifact and,
  if they disagree, flag it for a content decision.
- Never tick a completion checklist item the gate did not actually verify.
- Keep edits minimal and reversible; this is a verification gate, not a rewrite pass.

## Common mistakes to avoid

- **Grepping only the source `.tex`** and missing a draft note that was live (uncommented) text.
- **Trusting "0 forbidden terms" as full QC** — the forbidden-term list rarely includes editorial/draft phrases.
- **Reporting page count and stopping** — a clean compile can still contain wrong numbers or orphan floats.
- **Compiling once** — undefined references often need the full `pdflatex -> biber -> pdflatex x2` cycle to clear.
- **Editing the PDF's stale copy's source then reading the old PDF** — always recompile before the final grep.

## Additional guidance

A reference verdict line: `QC_DONE pages=<n> undefined=<n> forbidden=<n> draft_notes=<n> numbers_ok=<yes/no>`.
This gate composes with `manuscript-results-curation` (which curates the numbers) and `citation-audit` (which
verifies citation support); this skill is the last step that proves the compiled artifact is clean. Keep a
per-project forbidden-term list (excluded methods, removed datasets, deprecated names) alongside the generic
draft-note patterns, and extend the draft-note pattern set whenever a new leak is discovered.
