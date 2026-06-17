# Test Prompts: Telegram Agent Heartbeat and Notifications

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Set up a Telegram heartbeat for this long-running agent so I get a status update every 30 minutes.

Expected behavior: Read the bot token from a local file without printing it, resolve the chat id
(falling back to `getUpdates` / asking the user to `/start`), and build a notifier with a 30-minute
heartbeat loop.

---

## Test Prompt 2

> Send me an urgent Telegram alert whenever the agent hits a blocking failure or needs my input.

Expected behavior: Add `send_urgent_update(...)` calls in exception/blocking-failure paths with the
issue/impact/action/need-from-user fields, sent immediately and de-duplicated for identical issues.

---

## Test Prompt 3

> The heartbeat should also show how many files are processed and which step finished.

Expected behavior: Add a progress block derived from real artifacts (with a freshness guard) to the
heartbeat, and a `set-state` mechanism to update current/last/next step.

---

## Test Prompt 4

> Make sure the bot token never ends up in logs or git.

Expected behavior: Read the token at runtime, redact `bot<token>` from logs, and add the credential
and state files to `.gitignore`; flag if the token was already staged/committed.

---

## Test Prompt 5

> Notify me on Telegram when the agent starts, finishes a major task, and stops.

Expected behavior: Send a startup banner, `send_key_update(...)` on milestones, and a shutdown message
before exit, while avoiding spam for routine work.
