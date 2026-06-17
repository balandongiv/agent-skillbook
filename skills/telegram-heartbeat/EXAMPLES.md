# Examples: Telegram Agent Heartbeat and Notifications

## Example 1: Heartbeat that leaks the token vs. secret-safe

### Before (without this skill)

```python
TOKEN = "8869143068:AAF...redacted..."  # hardcoded, committed
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
print("calling", url)            # leaks the token into logs
requests.post(url, ...)          # if this raises, the agent crashes
```

### After (with this skill applied)

```python
def send_telegram_message(text: str) -> bool:
    try:
        token = _load_token()            # read from gitignored file at call time
        chat = _resolve_chat_id(token)   # file -> cache -> getUpdates
    except CredentialError as e:
        _log(f"cred error: {e}")         # message never contains the token
        return False
    for attempt in range(4):
        data = _api_call(token, "sendMessage", {"chat_id": chat, "text": text})
        if data and data.get("ok"):
            return True
        time.sleep(2 ** attempt)         # backoff; honor 429 retry_after
    return False                          # never raises into the agent loop
```

### Why it's better

The token is never printed or committed, logs are redacted, and a send failure returns `False`
instead of crashing the long-running task.

---

## Example 2: One heartbeat per interval vs. accidental spam

### Before (without this skill)

```python
for session in sessions:          # 400 sessions
    process(session)
    send_telegram_message("still working...")   # 400 messages
```

### After (with this skill applied)

```python
# background daemon, fixed cadence; state updated cheaply in the work loop
start_heartbeat_loop(interval_s=1800)   # one heartbeat / 30 min
for session in sessions:
    process(session)
    update_state(current_task=f"processing {session}")   # no message sent
# milestones only:
send_key_update("Batch complete", "session processing", "400/400 done", "run analysis")
```

### Why it's better

The human gets a steady 30-minute pulse plus real milestones, instead of hundreds of redundant
messages, and the heartbeat always reflects the latest state.
