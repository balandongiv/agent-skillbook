# Changelog — Telegram Pipeline Heartbeat

## [Unreleased]

### Added
- Back-filled the canonical `skill.yaml` (slug, title, summary, when_to_use, when_not_to_use,
  tags, invocation, platform_overrides) that was missing from the initial commit.
- Regenerated the OpenAI and Gemini exports so the skill passes validation.

## [0.1.0] - 2026-06-20

### Added
- Initial skill creation
- Secret-safe state management: token never in `state.json` or logs
- tqdm-style progress bar with ETA from timestamp history
- Rich message sections: status, Scopus KF progress, ChatGPT screening bar, SQLite counts, file counts
- Commands: `heartbeat`, `set-state`, `daemon`, `check`, `startup`, `key`, `urgent`
- Daemon PID management with kill-before-restart safety
- Auto-refresh of `updated_at` on every `heartbeat` command
- Token redaction in error messages
- `[Farah thesis — pipeline heartbeat]` standard header format
- `.env` and `.codex-tmp/` added to `.gitignore`

### Format lock
- Header must be exactly `[Farah thesis — pipeline heartbeat]` — changing this breaks the user's notification filter
