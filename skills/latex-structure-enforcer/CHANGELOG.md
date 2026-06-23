# Changelog — LaTeX Thesis Structure Enforcer

## [0.1.0] - 2026-06-20

### Added
- Initial skill creation
- One-paragraph-per-file restructuring for flat `.tex` chapters
- Table and figure environment extraction to `tables/tab_NNN.tex` and `figures/fig_NNN.tex`
- Aggregator generation: `chapter.tex`, `section.tex`, `subsection.tex`
- `writing/`-relative path enforcement for all `\input{}` commands
- Archive-first safety: originals moved to `writing/obs/` before restructuring
- `main.tex` update: `\input{chap1}` → `\input{ch01_introduction/chapter}`
- Naming conventions: `ch##`, `s###`, `ss###`, `p###`, `tab_###`, `fig_###`
- Implemented and tested via `scripts/restructure_latex.py` (228 files generated)

### Applied to
- Ch1: 9 sections, Ch2: 5 sections, Ch3: 11 sections (25 total sections, 228 `.tex` files)
