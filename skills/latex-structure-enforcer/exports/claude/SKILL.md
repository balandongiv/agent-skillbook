---
name: latex-structure-enforcer
description: Migrate flat or semi-flat LaTeX thesis files into the one-paragraph-per-file hierarchy. Every prose paragraph goes in p###/paragraph.tex, tables in tables/tab_NNN.tex, figures in figures/fig_NNN.tex, and chapter/section/subsection aggregators wire everything through \input{} chains with writing/-relative paths. Originals are archived, never deleted.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# LaTeX Thesis Structure Enforcer

## Overview

Migrate flat or semi-flat LaTeX thesis files into the one-paragraph-per-file hierarchy required by
`LATEX_STRUCTURE_REQUIREMENTS.md`. Every prose paragraph lives in its own `p001/paragraph.tex`,
tables go in `tables/tab_NNN.tex`, figures in `figures/fig_NNN.tex`, and `chapter.tex`,
`section.tex`, `subsection.tex` aggregators wire everything through `\input{}` chains.

## Core principles

1. **One paragraph, one file** — Every prose block separated by a blank line becomes its own
   `p###/paragraph.tex`. Environments (`enumerate`, `equation`, `align`, `itemize`) that are
   logically attached to the preceding paragraph stay in that paragraph file.
2. **Tables and figures are separate** — `\begin{table}` and `\begin{figure}` environments are
   extracted into `tables/tab_NNN.tex` and `figures/fig_NNN.tex` within the section or subsection
   folder. They are referenced from the aggregator with `\input{}`.
3. **All `\input{}` paths are relative to `writing/`** — LaTeX resolves `\input` relative to
   the main file directory, not the current file. Use full paths from `writing/` root everywhere.
4. **Aggregators own only structure** — `chapter.tex` contains one `\chapter{}` and `\input{}` calls.
   `section.tex` contains one `\section{}` and `\input{}` calls. No prose in aggregators.
5. **Archive originals, never delete** — Move old flat files to `writing/obs/` before restructuring.

## Required output structure

```
writing/
  main.tex                             # updated to \input{ch01_introduction/chapter}
  obs/                                 # archived original flat files

  ch01_introduction/
    chapter.tex                        # \chapter{...} + \input{s001_.../section} × N
    s001_overview/
      section.tex                      # \section{...} + \input{p001/paragraph} × N
      p001/paragraph.tex
      p002/paragraph.tex
    s005_problem_formulation/
      section.tex                      # \section{...} + \input{ss001_.../subsection} × N
      ss001_research_gap/
        subsection.tex                 # \subsection{...} + \input{p001/paragraph} × N
        p001/paragraph.tex
      ss002_problem_statement/
        subsection.tex
        p001/paragraph.tex
    s007_objectives/
      section.tex
      tables/
        tab_001.tex                    # extracted \begin{table}...\end{table}
      p001/paragraph.tex
```

## Step-by-step process

1. **Read `LATEX_STRUCTURE_REQUIREMENTS.md`** in the repository root to confirm the exact naming rules.
2. **Archive originals** — copy existing flat files to `writing/obs/` before touching them.
3. **Define the section map** — for each chapter, list `(section_title, s###_slug)` pairs in order.
4. **Parse each source file** by splitting on `\section{}` markers, then `\subsection{}` markers.
5. **Split body text into blocks** — scan line by line; blank lines are paragraph boundaries.
   Extract `table` and `figure` environments as separate blocks.
6. **Write paragraph files** — number sequentially `p001`, `p002`, … within each section/subsection.
7. **Write table files** — number sequentially `tab_001`, `tab_002`, … in `tables/` subfolder.
8. **Write aggregators** — `section.tex` gets `\section{Title}` + `\input{}` for each child.
   `subsection.tex` gets `\subsection{Title}` + `\input{}` for each child.
   `chapter.tex` gets `\chapter{Title}` + `\input{}` for each section.
9. **Update `main.tex`** — replace `\input{chap1}` with `\input{ch01_introduction/chapter}` etc.
10. **Validate** — every `.tex` file under `writing/ch*/` is reachable from `main.tex` through the
    `\input{}` chain. No prose in `chapter.tex`, `section.tex`, or `subsection.tex`.

## Naming conventions

| Level | Pattern | Example |
|---|---|---|
| Chapter folder | `ch##_<slug>` | `ch02_literature_review` |
| Section folder | `s###_<slug>` (max 25 chars) | `s005_problem_formulation` |
| Subsection folder | `ss###_<slug>` | `ss001_research_gap` |
| Paragraph folder | `p###` | `p001` |
| Table file | `tab_###.tex` | `tab_001.tex` |
| Figure file | `fig_###.tex` | `fig_001.tex` |
| Disabled content | under `obs/` | `writing/obs/chap1.tex` |

## Rules

- Always use paths relative to `writing/` in all `\input{}` commands.
- Always archive originals to `obs/` before restructuring.
- Never put `\chapter`, `\section`, or `\subsection` inside paragraph files.
- Never put prose paragraphs inside `chapter.tex`, `section.tex`, or `subsection.tex`.
- Always extract `\begin{table}` and `\begin{figure}` into separate files.
- Keep `\begin{equation}`, `\begin{enumerate}`, `\begin{itemize}`, `\begin{align}` inside
  the paragraph file they belong to.
- Number paragraph, table, and figure files with zero-padded three-digit counters.

## Common mistakes to avoid

- **Wrong `\input` path base**: Paths must be from `writing/`, not relative to the file containing
  the `\input` command.
- **Stray prose in aggregators**: `section.tex` should contain only `\section{}` and `\input{}` lines.
- **Merge of adjacent environments**: An `\begin{enumerate}` list should stay attached to its
  preceding paragraph if it is logically a continuation. Split only at true paragraph breaks.
- **Losing table labels**: `\label{tab:...}` must stay inside the extracted `tab_NNN.tex`, not be
  dropped during extraction.
