"""ChatGPT UI smoke gate — RUN THIS FIRST in any new session before ChatGPT work.

Opens the persistent Selenium profile, sends one trivial prompt, and confirms the
expected reply, with no human login interaction. Writes a JSON report to the artifact
dir. Exit code 0 = PASS (ChatGPT-driven work allowed), non-zero = FAIL (STOP).

    python smoke_chatgpt_ui.py            # -> prints PASS/FAIL, sets exit code
    from smoke_chatgpt_ui import smoke     # -> smoke() returns True/False
"""
from __future__ import annotations

import json
import sys
from datetime import datetime

from chatgpt_ui_session import ChatGPTSession, ChatGPTUIError, ARTIFACT_DIR

PROMPT = "Reply with exactly: SESSION OK"
EXPECTED = "SESSION OK"


def _write_report(status: str, detail: str, response: str = "") -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACT_DIR / "chatgpt_ui_smoke.json").write_text(
        json.dumps(
            {
                "status": status,
                "timestamp": datetime.now().isoformat(),
                "prompt": PROMPT,
                "response": response,
                "detail": detail,
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def smoke() -> bool:
    """Return True if the ChatGPT UI session is usable, else False (and report why)."""
    try:
        with ChatGPTSession(load_wait=60, reply_wait=90) as s:
            s.new_chat()
            reply = s.ask(PROMPT, label="smoke")
    except ChatGPTUIError as e:
        print(f"FAIL — {e}")
        _write_report("failed", str(e))
        return False
    except Exception as e:  # driver/version/profile problems
        print(f"FAIL — could not drive the ChatGPT UI: {e}")
        _write_report("failed", f"{type(e).__name__}: {e}")
        return False

    ok = EXPECTED in (reply or "")
    print(f"Response: {reply!r}")
    if ok:
        print("PASS — ChatGPT UI session is working from Selenium.")
        _write_report("passed", "Assistant replied with the expected text.", reply)
    else:
        print("FAIL — reply did not contain the expected text.")
        _write_report("failed", "Assistant reply did not contain the expected text.", reply)
    return ok


if __name__ == "__main__":
    sys.exit(0 if smoke() else 1)
