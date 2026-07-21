# Changelog — ChatGPT UI Batch Screener

## [Unreleased]

### Added
- Back-filled the canonical `skill.yaml` (slug, title, summary, when_to_use, when_not_to_use,
  tags, invocation, platform_overrides) that was missing from the initial commit.
- "Machine-aware profile and driver resolution" note: resolve the Chrome binary, chromedriver
  (from the shared `academic_paper_maker\apm\browser` folder), and ChatGPT profile per machine
  via the shared hostname-keyed registry, instead of hardcoding one machine's `chrome-profile`.
- Regenerated the OpenAI and Gemini exports so the skill passes validation.

## [0.1.0] - 2026-06-20

### Added
- Initial skill creation
- Pure-JS element interaction: no `is_displayed()` anywhere
- 5-papers-per-batch limit as the validated optimum
- Streaming completion detection via JS stop/send button polling
- `innerText` response extraction (not `innerHTML`)
- Raw response saved before JSON parse attempt
- Markdown code fence stripping (`json` and bare fences)
- `screening_progress.json` for resume support
- Batch file format (input) and response file format (output) specifications
- Hard 120-second timeout fallback for streaming detection
- Persistent Chrome profile enforcement: `C:\selenium\chrome-profile`
- Mutual exclusion note with Scopus automation (shared profile)
