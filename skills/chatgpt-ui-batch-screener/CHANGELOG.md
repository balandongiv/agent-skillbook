# Changelog — ChatGPT UI Batch Screener

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
