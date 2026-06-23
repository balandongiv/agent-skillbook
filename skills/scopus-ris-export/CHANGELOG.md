# Changelog — Scopus RIS Export Automation

## [0.1.0] - 2026-06-20

### Added
- Initial skill creation
- Core export flow: query entry via JS, Select-all with banner, RIS click, filesystem polling
- Strict modal check (requires count input + Export button — rejects `exportRefinement` false positive)
- Poll across three directories: `_staging/`, `Downloads/`, `Desktop/`
- Per-year sub-query fallback for queries > 2000 docs or session-cap failures
- Chrome LOCK file removal before each new session
- Title-based dedup merge for multi-batch RIS files
- Configuration reference with `POLL_TIMEOUT`, `BETWEEN_SLEEP`, `BATCH_THRESHOLD`

### Known issues
- Scopus daily export cap (~7–8 sessions) not automatically detected; must be tracked manually
- `BATCH_THRESHOLD` tuned for Scopus 2026 UI; may need adjustment if UI changes
