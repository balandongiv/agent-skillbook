# Changelog — Scopus RIS Export Automation

## [Unreleased]

### Added
- Back-filled the canonical `skill.yaml` (slug, title, summary, when_to_use, when_not_to_use,
  tags, invocation, platform_overrides) that was missing from the initial commit.
- "Machine-aware profile and driver resolution" section: a hostname-keyed `MACHINES` registry
  and `resolve_scopus()` helper so the chromedriver (from the shared
  `academic_paper_maker\apm\browser` folder), Chrome binary, and Scopus profile are selected
  automatically per computer. This machine (`rpb`) is filled in; two others are `TODO`
  placeholders. The `Configuration reference` now reads from the resolver instead of hardcoding.
- Regenerated the OpenAI and Gemini exports so the skill passes validation.

### Changed
- Replaced the hardcoded `CHROME_EXE` / `PROFILE_DIR` (previously "BINDING — never change") with
  machine-resolved paths, so the skill works across the fixed set of machines rather than one.

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
