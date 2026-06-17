# Test Prompts: Manuscript Final Compile QC Gate

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.
Use them to verify that the skill is correctly configured and the description is accurate.

---

## Test Prompt 1

> The paper is done — run a final QC pass before I submit it.

Expected behavior: Compile the manuscript (pdflatex -> biber -> pdflatex x2), then check undefined
cites/refs, forbidden terms, leaked draft notes in the PDF, and numeric spot-checks; report a verdict line.

---

## Test Prompt 2

> Make sure no TODO or draft notes ended up in the compiled PDF.

Expected behavior: Run `pdftotext` and grep the rendered text for draft/placeholder patterns; report and, if
a clear leak is found, remove it and recompile before reporting clean.

---

## Test Prompt 3

> Confirm the numbers in the results tables match the CSVs and that there are zero undefined references.

Expected behavior: Spot-check several headline numbers against their source artifacts and scan main.log for
`undefined`; report pass/fail per number and the undefined count.

---

## Test Prompt 4

> Final gate on the manuscript: clean compile, no Murat/DBO terms, no leftover editorial text.

Expected behavior: Compile, grep the rendered PDF for the project's forbidden terms and draft-note patterns,
and report a machine-readable verdict (pages/undefined/forbidden/draft_notes/numbers_ok).

---

## Test Prompt 5

> Verify the paper is submission-ready and every figure/table is actually referenced.

Expected behavior: Compile, run the undefined/forbidden/draft checks, and perform the coverage check for orphan
or unreferenced floats; report defects without rewriting content.
