---
name: evidence-driven-thesis-writer
description: Write academic thesis prose grounded in a SQLite evidence database. Evidence records must exist before any section is written. Bibtex keys use paper_{id} placeholders until BibTeX is generated. Output follows one-paragraph-per-file LaTeX structure. Target-label columns (TWF, HDF, PWF, OSF, RNF) are never used as model input features.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Evidence-Driven Thesis Writer

## Overview

Write academic thesis prose grounded in a SQLite database of screened papers. Every claim traces
back to a `thesis_sentence_evidence` record. No prose is written until evidence records exist for
that section.

## Pipeline position

```
Stages 1–7:  Scopus → SQLite → ChatGPT screening
Stage 8:     Build evidence JSON  ← this skill starts here
Stages 9–11: Export writing packages → write LaTeX prose
```

## Critical constraint

**Never write prose for a section with zero evidence records:**
```python
count = db.execute(
    "SELECT COUNT(*) FROM thesis_sentence_evidence WHERE chapter_path LIKE '%%2_3%%'"
).fetchone()[0]
if count == 0:
    raise RuntimeError("No evidence for 2_3 — run Stage 8 first")
```

## Evidence record format

```json
{
  "thesis_sentence": "",
  "claim_type": "literature_evidence",
  "chapter_path": "ch02/2_4_explainable_artificial_intelligence",
  "source_paper_id": 317,
  "bibtex_key": "paper_317",
  "extracted_sentence": "SHAP values revealed that cutting speed contributed most...",
  "support_relation": "supports",
  "confidence": 0.9,
  "audit_status": "pending_bibtex"
}
```

## Bibtex key rule

- Draft: use `paper_{id}` placeholder, `audit_status = "pending_bibtex"`
- After BibTeX file exists: verify key against `.bib`, update to real key, set `audit_status = "verified"`
- **Never invent author-year keys**

## LaTeX output rule

Output follows `LATEX_STRUCTURE_REQUIREMENTS.md`:
- Each paragraph → `writing/ch0X_.../s###_<section>/p###/paragraph.tex`
- Cite with `\parencite{paper_317}` or `\textcite{paper_317}`
- No prose in `section.tex` — only `\section{}` and `\input{}`

## Target-label constraint

Never use as model input features: `Machine failure`, `TWF`, `HDF`, `PWF`, `OSF`, `RNF`.
These are target-only columns for constructing the multi-class label.

## Chapter-section labels

```
2_2_thermal_and_mechanical_feature_engineering
2_3_machine_learning_for_failure_classification
2_4_explainable_artificial_intelligence
2_5_research_gap
```

## Rules

- Evidence guard: always check record count before writing.
- Use `paper_{id}` bibtex keys until BibTeX is audited.
- Save evidence per section AND as `evidence_all.json`.
- Follow LaTeX structure: `p###/paragraph.tex` for every paragraph.
- Write only what the source sentence actually says — no extrapolation.
- Never use target label columns as input features.
