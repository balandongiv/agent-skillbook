# Changelog: Citation Relevance Audit

All notable changes to this skill are documented here.

## [Unreleased]

### Added
- "Sourcing `actual_text` from a reference library" guidance: read supporting text from a reference-manager
  export (e.g. Zotero CSV "Abstract Note" column keyed by bibtex "Key"); cross-check keys against the bib
  catalogue; set `actual_text=""` and flag unverifiable when no abstract is stored.
- Encoding gotcha: open CSV/JSON sources with explicit `encoding="utf-8"` (platform defaults like cp1252 raise
  `UnicodeDecodeError` mid-file) and write the audit JSON with `ensure_ascii=False`.

## [0.1.0] - 2026-06-17

### Added
- Initial version of the citation-audit skill.
- Core instructions for atomising cited statements, extracting verbatim supporting text from the cited
  source, assessing relevance (Relevant / Partially relevant / Not relevant), and emitting the required
  JSON audit structure.
- Examples for partial-support and irrelevant-citation cases; test prompts for verification.
