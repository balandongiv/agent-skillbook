# Telegram Agent Heartbeat and Notifications

## Overview

Give a long-running or background agent a Telegram "pulse" so a human can follow it without polling.
The layer sends three message classes — periodic **heartbeats**, immediate **urgent alerts**, and
**milestone (key) updates** — through the Telegram Bot API, while treating the bot token as a secret
and never letting a send failure crash the agent.

## Core principles

1. **The token is a secret** — Read it at runtime from a local file (or env var). Never print, log,
   echo, or commit it. Redact any `bot<token>` substring from all logs and error output.
2. **Notifications are best-effort** — A failed send must never crash the main task. Wrap every send in
   error handling with retry/backoff; log failures locally without the token.
3. **Anti-spam by construction** — Heartbeats fire on a fixed interval (default 30 min). Urgent alerts
   send immediately but identical issues are grouped/rate-limited. Milestone updates only for real events.
4. **State is decoupled from the loop** — Keep current task / last step / next step / counters in a small
   state file the heartbeat reads, so the orchestrating agent can update context at any time.
5. **Liveness must be truthful** — Heartbeat status (alive/working/idle/degraded) and any progress block
   must reflect real, verifiable state (e.g., counts derived from artifacts on disk), not guesses.

## Start-of-task checklist (do this FIRST, before the work)

The most common failure is not a bug in the notifier — it is **forgetting to start it**, so the human sees
silence and assumes the agent is dead. Make these the literal first actions of any long/background task:

1. **Verify credentials** (`check`): token loads, chat id resolves. If not, STOP and report.
2. **Send a startup ping** immediately (`startup`) so the human has positive confirmation the run began.
3. **Launch the heartbeat daemon in the background** (`daemon --interval <s>`) — it will not run unless you
   explicitly start it. Treat this as a required step, not optional.
4. **Send a start ping at the beginning of each long sub-task** and an end ping when it finishes.
5. **The daemon typically logs only failures** — an empty/quiet log means heartbeats are succeeding, not
   that nothing happened. Confirm one delivery (`RESULT: SENT_OK`) once, then trust silence.
6. **Stop the daemon and send a final summary** when the task completes.

If the human ever says "no heartbeat received", the cause is almost always a skipped step 2/3 above —
re-run them rather than debugging the transport.

## Step-by-step process

1. **Locate the credential.** Read the bot token from a local file (e.g. `bot_telegram.md`) or env var.
   If missing/invalid, STOP and report clearly — do not proceed silently.
2. **Resolve the chat id.** Check the credential file, then a cached id file, then call `getUpdates`.
   If none is found, instruct the user to open the bot and send `/start`, then retry.
3. **Build the notifier module** exposing: `send_telegram_message(text)`,
   `send_heartbeat(status, current_task, last_step, next_step)`,
   `send_urgent_update(issue, current_task, impact, action_taken, need_from_user)`,
   `send_key_update(event, task, result, next_step)`, and `start_heartbeat_loop()`.
4. **Start on launch.** Send a startup banner (interval + which notification classes are enabled).
5. **Run the heartbeat loop** in the background at the chosen interval (default 1800 s). Each tick reads
   the state file and sends a heartbeat including agent name, status, current task, last/next step,
   uptime, timestamp, and warning/error counts (plus an optional processing-progress block).
6. **Update state as work changes** via a `set-state` entrypoint; call `send_key_update()` on real
   milestones and `send_urgent_update()` inside exception handlers and blocking-failure paths.
7. **On shutdown / fatal error,** send a final message before exiting if possible.

## Rules

- Always read the token at call time and redact it everywhere; never hardcode or commit it; add the
  credential and state files to `.gitignore`.
- Always retry transient/network/`429` errors with exponential backoff and honor `retry_after`; give up
  gracefully on permanent client errors (bad chat, blocked bot).
- Always rate-limit: one heartbeat per interval; group identical urgent issues within a short window.
- Never let a notification path raise into the main agent loop.
- Never report a status or progress number you cannot verify from real state.

## Common mistakes to avoid

- **Capturing a streaming/placeholder reply** when discovering the chat or testing — wait for the real
  response and validate it.
- **Logging the full API URL** (which contains the token). Log the method name only.
- **Heartbeat spam** from putting the send inside the work loop instead of a timed loop.
- **Stale progress** — guard any progress block with a freshness check so a finished run does not keep
  reporting old numbers.

## Additional guidance

A reference implementation pattern: a single `telegram_heartbeat.py` module with a CLI
(`check | startup | heartbeat | key | urgent | set-state | daemon`), a JSON state file (no secrets),
and a separate progress probe that derives counts from artifacts on disk and writes a small JSON the
heartbeat renders. Run the daemon in the background; drive `set-state`/`key`/`urgent` from the
orchestrator. The transport is swappable — the same structure works for Slack/Discord webhooks.
