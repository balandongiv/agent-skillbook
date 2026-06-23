# Tests — Telegram Pipeline Heartbeat

## T1: Token never appears in state.json

**Given** `.env` contains `TELEGRAM=bot123:ABC`  
**When** `set-state` command updates state.json  
**Then** `state.json` contains no occurrence of the token string

**Verify**: `json.loads(state_json)` has no value containing "bot" or the actual token.

---

## T2: Token redacted in error output

**Given** the Telegram API returns a connection error  
**When** the heartbeat script catches the exception  
**Then** the error message printed to stdout does not contain the bot token

**Verify**: stdout captured during error contains `[REDACTED]` in place of the token.

---

## T3: Progress bar renders correctly

**Given** `responses=111`, `batches=264`  
**When** `build_progress_bar(111, 264)` is called  
**Then** output is `[████████░░░░░░░░░░░░] 42.0% (111/264)`

**Verify**: 8 `█` chars, 12 `░` chars, total bar width = 20.

---

## T4: ETA calculated from log history

**Given** progress log has 10 timestamps spanning 30 minutes for 90 batches  
**When** ETA is computed for remaining 174 batches  
**Then** ETA is approximately 58 minutes (within 5 minutes)

---

## T5: Old daemon killed before new daemon starts

**Given** `daemon.pid` contains PID of a running Python process  
**When** `daemon` command is invoked  
**Then** old process is terminated and new PID is written to `daemon.pid`

**Verify**: `psutil.pid_exists(old_pid)` is False after new daemon starts.

---

## T6: Heartbeat auto-updates timestamp

**Given** `state.json.updated_at = "2026-06-01T00:00:00"` (stale)  
**When** `heartbeat` command is invoked  
**Then** the sent message contains today's date in `state_updated`

**Verify**: `state_updated` in message != `"2026-06-01T00:00:00"`.

---

## T7: Chat ID resolved from .env

**Given** `.env` contains `TELEGRAM_CHAT_ID=99999999`  
**When** heartbeat is sent  
**Then** message is sent to chat ID 99999999 without calling `getUpdates`

**Verify**: No HTTP call to `getUpdates` in the request log.
