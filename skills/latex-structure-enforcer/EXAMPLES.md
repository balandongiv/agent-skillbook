# Examples — LaTeX Thesis Structure Enforcer

## Example 1: Single-section migration (no subsections)

### Before (flat file: `writing/chap2.tex`)
```latex
\section{Introduction to the Chapter}
This chapter reviews the literature on thermal and mechanical failure classification.
The review is organised around three themes: feature engineering, machine learning models,
and explainable AI methods applied to predictive maintenance.

A systematic review protocol was followed...
```

### After (structured)

**`writing/ch02_literature_review/s001_introduction_to_chapter/section.tex`**
```latex
\section{Introduction to the Chapter}
\input{ch02_literature_review/s001_introduction_to_chapter/p001/paragraph}
\input{ch02_literature_review/s001_introduction_to_chapter/p002/paragraph}
```

**`writing/ch02_literature_review/s001_introduction_to_chapter/p001/paragraph.tex`**
```latex
This chapter reviews the literature on thermal and mechanical failure classification.
The review is organised around three themes: feature engineering, machine learning models,
and explainable AI methods applied to predictive maintenance.
```

**`writing/ch02_literature_review/s001_introduction_to_chapter/p002/paragraph.tex`**
```latex
A systematic review protocol was followed...
```

### Why it's better
Each paragraph is independently editable, trackable in git, and writable by the evidence-driven
pipeline. The aggregator `section.tex` is a pure structure file — never contains prose.

---

## Example 2: Section with a table

### Before
```latex
\section{Research Objectives}
The objectives of this research are listed in Table~\ref{tab:objectives}.
\begin{table}[h]
\centering
\caption{Research Objectives}
\label{tab:objectives}
\begin{tabular}{cl}
...
\end{tabular}
\end{table}
```

### After

**`writing/ch01_introduction/s007_objectives/section.tex`**
```latex
\section{Research Objectives}
\input{ch01_introduction/s007_objectives/p001/paragraph}
\input{ch01_introduction/s007_objectives/tables/tab_001}
```

**`writing/ch01_introduction/s007_objectives/p001/paragraph.tex`**
```latex
The objectives of this research are listed in Table~\ref{tab:objectives}.
```

**`writing/ch01_introduction/s007_objectives/tables/tab_001.tex`**
```latex
\begin{table}[h]
\centering
\caption{Research Objectives}
\label{tab:objectives}
\begin{tabular}{cl}
...
\end{tabular}
\end{table}
```

---

## Example 3: Wrong `\input` path (common mistake)

### Wrong
```latex
% In writing/ch02_literature_review/s001_intro/section.tex
\input{p001/paragraph}   % ← relative to section.tex location
```
LaTeX resolves `\input` relative to `main.tex`, not the file containing the command.
This silently includes the wrong path or nothing.

### Correct
```latex
\input{ch02_literature_review/s001_introduction_to_chapter/p001/paragraph}
```
All paths are absolute from `writing/` (the directory containing `main.tex`).
