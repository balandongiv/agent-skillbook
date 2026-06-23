---
name: telegram-pipeline-heartbeat
description: Add secret-safe Telegram heartbeat to any long-running pipeline. State file contains no secrets. Sends tqdm-style progress bars, rich multi-section status messages, milestone alerts, and urgent notifications. Daemon is restart-safe with PID management.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Telegram Pipeline Heartbeat

## Overview

Add secret-safe Telegram heartbeat and notification to any long-running research pipeline.
Sends periodic status messages with live pipeline metrics, tqdm-style progress bars,
milestone alerts, and urgent notifications. Secrets are loaded from `.env` only at send time
and never written to state files, logs, or commits.

## Required message format

```
[Farah thesis — pipeline heartbeat]
status: running
current: <current task description>
last: <last completed step>
next: <next planned step>

--- Scopus KF progress ---
  Q001/KF001: download_timeout (688 docs)
  Q002/KF002: done (128 docs)

--- ChatGPT screening ---
  [████████████████░░░░] 84.1% (222/264) ~32m left

--- SQLite ---
  papers: 2120 total, 1317 regex-matched

--- Writing packages ---
  packages: 51 total

--- Files ---
  parent RIS: 7 files

state_updated: <ISO timestamp>
sent_at: <ISO timestamp>
```

**IMPORTANT**: Header must be exactly `[Farah thesis — pipeline heartbeat]` — do not change.

## State file format (no secrets)

```json
{
  "status": "running",
  "current_task": "Stage 7: ChatGPT UI screening",
  "last_step": "Stage 4 complete: 2120 papers in SQLite",
  "next_step": "Import screening decisions → build evidence JSON",
  "updated_at": "2026-06-20T06:30:00"
}
```

State file location: `.codex-tmp/telegram_heartbeat/state.json`

## Progress bar calculation

```python
pct = responses / batches
filled = int(pct * 20)
bar = "█" * filled + "░" * (20 - filled)
# ETA from timestamp history in progress log
```

## Rules

- Never write token or chat ID to `state.json`, logs, or any committed file.
- Always add `.env` and `.codex-tmp/` to `.gitignore`.
- Always kill existing daemon PID before starting a new one.
- Always auto-refresh `updated_at` in the `heartbeat` command.
- Use `disable_notification=True` for periodic heartbeats; omit for `urgent`.
- Always redact token in error messages: `str(exc).replace(token, "[REDACTED]")`.

## Commands

- `heartbeat` — send current state immediately
- `set-state --current X --last Y --next Z` — update state without sending
- `daemon` — start periodic sender (kills existing daemon first)
- `urgent --msg "X"` — send urgent notification with alert sound
- `check` — verify bot token and chat ID work
- `key` — resolve and cache chat ID from `.env` or `getUpdates`
