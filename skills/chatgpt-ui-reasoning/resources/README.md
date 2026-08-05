# Reusable ChatGPT UI code (ship once, import everywhere)

This folder ships the working implementation of the skill so agents **import it instead
of rewriting the Selenium plumbing every session**.

| File | What it is |
|---|---|
| `machine_profiles.py` | Hostname-keyed `MACHINES` registry + `resolve_selenium(task)` / `resolve_scopus()`. Single source for browser/driver/profile paths. Only `rpb` (this computer) is filled in; two machines are `TODO`. |
| `chatgpt_ui_session.py` | `ChatGPTSession` (+ `ChatGPTUIError`): one browser, `new_chat()` per item, JS insert + click fallback, stable-reply poll. Profile resolved per machine; driver via webdriver-manager with the registry chromedriver as fallback. |
| `smoke_chatgpt_ui.py` | The smoke gate. Exit 0 = PASS, non-zero = FAIL. Exposes `smoke() -> bool`. |

## Standing convention: run the smoke test FIRST

At the start of **any new session** that will drive the ChatGPT UI (or any common
Selenium script here), run the smoke gate before doing real work:

```bash
python smoke_chatgpt_ui.py          # exit 0 = allowed to proceed; non-zero = STOP
```

If it fails (login lost, driver/Chrome mismatch, profile locked), **do no
ChatGPT-driven work** until it passes — fix the session first.

## Using the session

```python
import sys
sys.path.insert(0, r"<path to this resources dir>")   # or install the skillbook package

from chatgpt_ui_session import ChatGPTSession, ChatGPTUIError

with ChatGPTSession() as s:          # profile auto-resolved for this machine
    s.new_chat()                     # fresh context per item, same browser
    reply = s.ask("your reasoning / triage prompt")
    # save the raw transcript before parsing; end triage prompts with a VERDICT line
```

## Adding a machine

Copy the `"rpb"` block in `machine_profiles.py`, change the hostname key to the new
machine's `socket.gethostname().lower()`, and set that machine's driver/chrome/profile
paths. An unregistered machine raises rather than guessing.

## Artifacts

Screenshots and the smoke report default to `./chatgpt_ui_artifacts/`; override with the
`CHATGPT_UI_ARTIFACTS` environment variable.
