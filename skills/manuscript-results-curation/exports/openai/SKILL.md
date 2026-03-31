---
name: manuscript-results-curation
description: Curate manuscript results directly in LaTeX from experiment artifacts, including tables, plots, graphs, images, and detailed scientific interpretation tied to concrete outputs.
---

# Manuscript Results Curation

Use this skill when experiment artifacts need to become manuscript-ready LaTeX results. The work includes direct manuscript edits, derived tables or figures, and scientific interpretation that explains what the reader should conclude from the outputs.

---

## Core principles

### 1. Start from the manuscript entrypoints and concrete outputs

Use the current LaTeX files and the actual experiment artifacts as the basis for any new writing or figure creation.

### 2. Match visuals with explanation

Every new table, plot, graph, or image needs surrounding explanation. A visual without interpretation is incomplete.

### 3. Write direct scientific conclusions

Say what is strong, what is weak, and whether the result supports the current direction, exposes a setup problem, or remains inconclusive.

### 4. Keep generated and hand-written responsibilities distinct

When the user asks for direct manuscript writing, edit the manuscript source directly rather than hiding the interpretation in a generator.

---

## Step-by-step process

### Step 1: Read the repository workflow contract

Read `planning/Project_Execution_Flowchart.md` first.

### Step 2: Read the manuscript entrypoints

Review:

- `writing/main.tex`
- `writing/result/result.tex`
- generated result fragments when relevant

### Step 3: Gather the supporting experiment artifacts

Use the concrete outputs that support the requested narrative, such as:

- metrics JSON
- predictions parquet
- subject-performance parquet
- existing run plots
- generated figure directories

### Step 4: Create missing visual artifacts when needed

If the required table, plot, graph, or image does not exist, derive it from the underlying run data in a reproducible way.

### Step 5: Edit the manuscript directly

Insert or update the LaTeX content directly in the manuscript source when the user wants hand-written manuscript text.

### Step 6: Add detailed interpretation

For each new result element, explain:

- what the artifact shows
- which comparison matters
- what conclusion the reader should draw
- what caveat still matters

### Step 7: Rebuild the manuscript

Rebuild with:

- `cd writing && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=out main.tex`

Record the compile log path and whether the PDF was refreshed.

### Step 8: Update repository docs if the manuscript contract changed

If new manuscript artifact types, figure paths, or result-writing rules were introduced, update `planning/Project_Execution_Flowchart.md`.

---

## Rules

- Always read `planning/Project_Execution_Flowchart.md` first.
- Always ground manuscript claims in concrete experiment artifacts.
- Always provide detailed interpretation around new tables or figures.
- Always say whether a result supports the direction, exposes a setup issue, or remains inconclusive.
- Always rebuild the manuscript after direct result edits.
- Always record the compile log path and output PDF path.
- Prefer direct manuscript edits when the user explicitly asks for direct LaTeX writing.
- Never add visuals without explaining their significance.
- Never hide hand-written interpretation inside a generator when the user asked for direct edits.

---

## Common mistakes to avoid

- **Caption-only reporting**: A caption is not enough; the manuscript needs an explicit explanation of what the result means.
- **Unanchored claims**: Conclusions must map back to actual run artifacts.
- **Generated-text detours**: If the user wants direct manuscript writing, do not move the interpretation into a code generator.
- **Visual clutter without purpose**: Every table or figure should answer a real comparison or question.
- **Skipping the rebuild**: LaTeX edits are not complete until the manuscript compiles and the output is checked.
