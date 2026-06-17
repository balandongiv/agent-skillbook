# Changelog: Telegram Agent Heartbeat and Notifications

All notable changes to this skill are documented here.

## [Unreleased]

### Added
- "Start-of-task checklist (do this FIRST)" section: verify credentials, send a startup ping, and launch the
  daemon as the literal first actions of a long task; send start/end pings per sub-task; note that the daemon
  logs only failures (silence = success); stop daemon + send final summary at the end. Captures the recurring
  "no heartbeat received" failure (the notifier was never started, not broken).

## [0.1.0] - 2026-06-17

### Added
- Initial version of the Telegram agent heartbeat and notifications skill.
- Core instructions for secret-safe token handling, chat-id resolution, heartbeat/urgent/key message
  classes, anti-spam rate limiting, retry/backoff, and decoupled state.
- Examples for token safety and heartbeat cadence; test prompts for skill verification.
