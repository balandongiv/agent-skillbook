# Examples — Telegram Pipeline Heartbeat

## Example 1: Stage transition update

### Scenario
Pipeline just finished Stage 4 (2120 papers in SQLite) and is starting Stage 7 (ChatGPT screening).

### Command
```bash
python scripts/telegram_heartbeat.py set-state \
  --status running \
  --current "Stage 7: ChatGPT UI screening — 264 batches × 5 papers" \
  --last "Stage 4 complete: 2120 papers in SQLite (1317 regex-matched)" \
  --next "Import screening decisions → build evidence JSON"
python scripts/telegram_heartbeat.py heartbeat
```

### Expected Telegram message
```
[Farah thesis — pipeline heartbeat]
status: running
current: Stage 7: ChatGPT UI screening — 264 batches × 5 papers via Selenium
last: Stage 4 complete: 2120 papers in SQLite (1317 regex-matched)
next: Import screening decisions → build evidence JSON → writing packages

--- ChatGPT screening ---
  [░░░░░░░░░░░░░░░░░░░░] 0.0% (0/264) estimating...

--- SQLite ---
  papers: 2120 total, 1317 regex-matched

state_updated: 2026-06-20T08:00:00
sent_at: 2026-06-20T08:00:05
```

---

## Example 2: Mid-run heartbeat with progress bar

### Scenario
222 of 264 ChatGPT batches completed; rate ≈ 8 batches/min.

### Expected section
```
--- ChatGPT screening ---
  [████████████████░░░░] 84.1% (222/264) ~32m left
```

### Why it's better than a plain percentage
The tqdm-style bar is readable at a glance without calculating in your head. ETA is derived from
actual timestamps in the progress log, not a theoretical rate.

---

## Example 3: Secret leakage prevention

### Wrong (leaks token)
```python
try:
    requests.get(url)
except Exception as e:
    print(f"Error: {e}")   # prints full URL with bot token
```

### Correct
```python
token = os.getenv("TELEGRAM")
try:
    requests.get(url)
except Exception as e:
    safe_msg = str(e).replace(token, "[REDACTED]")
    print(f"Error: {safe_msg}")
```

And `.env` is never committed:
```
# .gitignore
.env
.codex-tmp/
```

---

## Example 4: Daemon restart without stale processes

### Wrong
```bash
python scripts/telegram_heartbeat.py daemon  # if old daemon still running, two daemons now exist
```

### Correct
```bash
python scripts/telegram_heartbeat.py daemon
# Script internally does:
#   1. Read PID from .codex-tmp/telegram_heartbeat/daemon.pid
#   2. taskkill /PID <old_pid> /F  (Windows) or kill <old_pid>
#   3. Fork new daemon, write new PID
```
