# Tests — LaTeX Thesis Structure Enforcer

## T1: Paragraph count matches source

**Given** `chap1.tex` has 23 prose paragraphs (blank-line separated)  
**When** `restructure_latex.py` processes it  
**Then** exactly 23 `p###/paragraph.tex` files are created across all sections

**Verify**: `glob("writing/ch01_introduction/**/paragraph.tex")` returns 23 files.

---

## T2: Tables extracted to `tables/` subfolder

**Given** a section contains two `\begin{table}` environments  
**When** the section is processed  
**Then** `tab_001.tex` and `tab_002.tex` exist in `tables/` and are referenced in `section.tex`

**Verify**: `section.tex` contains `\input{...tables/tab_001}` and `\input{...tables/tab_002}`.

---

## T3: Aggregators contain no prose

**Given** restructuring is complete  
**When** all `chapter.tex`, `section.tex`, `subsection.tex` files are read  
**Then** none contain any line that is not `\chapter{}`, `\section{}`, `\subsection{}`, or `\input{}`

**Verify**: Regex `^(?!\\(chapter|section|subsection|input)\{).+\S` matches no lines in aggregators.

---

## T4: All `\input{}` paths use `writing/`-relative format

**Given** restructuring is complete  
**When** all `.tex` files are scanned for `\input{}` commands  
**Then** every `\input{}` path starts with `ch0` (relative to `writing/`)

**Verify**: No `\input{p001/paragraph}` (relative) — only `\input{ch01_introduction/s001_.../p001/paragraph}`.

---

## T5: Originals archived, not deleted

**Given** `writing/chap1.tex` exists  
**When** restructuring runs  
**Then** `writing/obs/chap1.tex` exists and `writing/chap1.tex` is gone (or moved)

**Verify**: `os.path.exists("writing/obs/chap1.tex")` is True.

---

## T6: main.tex updated correctly

**Given** `main.tex` contains `\input{chap1}`  
**When** restructuring runs  
**Then** `main.tex` contains `\input{ch01_introduction/chapter}` and no `\input{chap1}`

**Verify**: `grep -n 'input{chap' writing/main.tex` returns no results.

---

## T7: No content lost

**Given** a section with 3 paragraphs and 1 table  
**When** restructuring and reassembly is done  
**Then** concatenating all `p###/paragraph.tex` + `tables/tab_001.tex` for that section
   reproduces the same text content as the original section body (whitespace-normalised)
