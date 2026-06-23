---
name: latex-structure-enforcer
description: Migrate flat LaTeX thesis files into the one-paragraph-per-file hierarchy. Every prose paragraph goes in p###/paragraph.tex, tables in tables/tab_NNN.tex, and chapter/section/subsection aggregators wire everything through \input{} chains with writing/-relative paths.
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
    s007_objectives/
      section.tex
      tables/
        tab_001.tex                    # extracted \begin{table}...\end{table}
      p001/paragraph.tex
```

## Naming conventions

| Level | Pattern | Example |
|---|---|---|
| Chapter folder | `ch##_<slug>` | `ch02_literature_review` |
| Section folder | `s###_<slug>` (max 25 chars) | `s005_problem_formulation` |
| Subsection folder | `ss###_<slug>` | `ss001_research_gap` |
| Paragraph folder | `p###` | `p001` |
| Table file | `tab_###.tex` | `tab_001.tex` |
| Figure file | `fig_###.tex` | `fig_001.tex` |

## Step-by-step process

1. **Read `LATEX_STRUCTURE_REQUIREMENTS.md`** in the repository root.
2. **Archive originals** to `writing/obs/` before touching them.
3. **Define the section map** for each chapter.
4. **Parse** each source file: split by `\section{}`, then `\subsection{}`.
5. **Split prose into blocks** on blank lines; extract `table`/`figure` environments separately.
6. **Write paragraph files**: `p001/paragraph.tex`, `p002/paragraph.tex`, …
7. **Write table files**: `tables/tab_001.tex`, `tables/tab_002.tex`, …
8. **Write aggregators**: `section.tex`, `subsection.tex`, `chapter.tex` — structure only, no prose.
9. **Update `main.tex`**: replace `\input{chap1}` with `\input{ch01_introduction/chapter}`.
10. **Validate**: all `.tex` files reachable from `main.tex` via `\input{}` chain; no prose in aggregators.

## Rules

- All `\input{}` paths must be relative to `writing/` (not the file containing the command).
- Always archive originals to `obs/` before restructuring.
- Never put `\chapter`, `\section`, or `\subsection` inside paragraph files.
- Never put prose in `chapter.tex`, `section.tex`, or `subsection.tex`.
- Extract `\begin{table}` and `\begin{figure}` into separate files.
- Keep `\begin{equation}`, `\begin{enumerate}`, `\begin{itemize}` inside their paragraph file.
- Use zero-padded three-digit counters: `p001`, `tab_001`.

## Critical path error

`\input{p001/paragraph}` (relative) silently includes wrong content.
Correct: `\input{ch02_literature_review/s001_introduction_to_chapter/p001/paragraph}`.
