# Changelog — Evidence-Driven Thesis Writer

## [0.1.0] - 2026-06-20

### Added
- Initial skill creation
- Evidence-first guard: blocks writing if zero `thesis_sentence_evidence` records for the target section
- `paper_{id}` placeholder bibtex key format with `audit_status = "pending_bibtex"`
- BibTeX audit function to update keys to real author-year format
- Writing package format: 20 papers per batch, structured for AI-assisted prose generation
- Per-section and combined `evidence_all.json` output
- SQLite schema documentation for `screening_decisions`, `source_sentences`, `thesis_sentence_evidence`
- Chapter-section label reference list
- No-target-label constraint: failure type columns (TWF, HDF, PWF, OSF, RNF) are target-only
- LaTeX output follows `LATEX_STRUCTURE_REQUIREMENTS.md` (one paragraph per `p###/paragraph.tex`)
- Pipeline stage map: Stages 1–4 → SQLite, Stage 5 snowball, Stage 6 regex, Stage 7 ChatGPT, Stages 8–11 evidence → writing
