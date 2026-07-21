"""Reusable ChatGPT UI session — one browser, many rounds, machine-aware profile.

Ship-once implementation of the `chatgpt-ui-reasoning` skill. Import this instead of
re-writing the Selenium plumbing every session:

    import sys; sys.path.insert(0, "<this resources dir>")
    from chatgpt_ui_session import ChatGPTSession, ChatGPTUIError
    with ChatGPTSession() as s:
        s.new_chat()                       # fresh chat per item, same browser
        reply = s.ask("your reasoning prompt")

Run `smoke_chatgpt_ui.py` FIRST in any new session — if the smoke gate fails
(login lost, driver mismatch), do no ChatGPT-driven work until it passes.

The profile is resolved per machine via `machine_profiles.resolve_selenium("chatgpt")`.
The WebDriver is obtained through webdriver-manager (auto-matches the installed Chrome);
the pinned chromedriver in the machine registry is a fallback if that is unavailable.
"""
from __future__ import annotations

import os
import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from machine_profiles import resolve_selenium

CHATGPT_URL = "https://chatgpt.com"

ASSISTANT_SEL = "[data-message-author-role='assistant']"
STOP_BTN_SEL = "button[data-testid='stop-button']"
SEND_BTN_SEL = "button[data-testid='send-button']"

# Screenshots/artifacts go here; override with the CHATGPT_UI_ARTIFACTS env var.
ARTIFACT_DIR = Path(os.environ.get("CHATGPT_UI_ARTIFACTS", "chatgpt_ui_artifacts"))


def _build_driver(profile: str) -> webdriver.Chrome:
    """Attach Chrome to the persistent profile, preferring webdriver-manager."""
    options = Options()
    options.add_argument(f"--user-data-dir={profile}")
    options.add_argument("--profile-directory=Default")
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
    except Exception:
        # Fall back to the machine's pinned chromedriver from the registry.
        service = Service(resolve_selenium("chatgpt")["chromedriver"])
    return webdriver.Chrome(service=service, options=options)


class ChatGPTUIError(RuntimeError):
    """Raised when the UI is not usable (login lost, no reply, ...)."""


class ChatGPTSession:
    """One browser, one conversation, many rounds; a new_chat() per item."""

    def __init__(self, load_wait: int = 60, reply_wait: int = 300) -> None:
        self.load_wait = load_wait
        self.reply_wait = reply_wait
        self.profile = resolve_selenium("chatgpt")["profile"]
        self.driver = None
        self.rounds: list[dict] = []

    def __enter__(self) -> "ChatGPTSession":
        self.driver = _build_driver(self.profile)
        self.driver.get(CHATGPT_URL)
        title = self.driver.title
        if "log in" in title.lower() or "sign in" in title.lower():
            raise ChatGPTUIError(
                "Login page appeared; session cookie not loaded. Re-authenticate the "
                "persistent profile manually, then re-run the smoke test."
            )
        WebDriverWait(self.driver, self.load_wait).until(
            EC.presence_of_element_located((By.ID, "prompt-textarea"))
        )
        return self

    def __exit__(self, *exc) -> None:
        if self.driver:
            try:
                self.screenshot("final")
            except Exception:
                pass
            self.driver.quit()

    def new_chat(self) -> None:
        """Start a fresh conversation in the SAME browser window.

        Reusing one browser and opening a new chat per item is far cheaper than
        relaunching Chrome each time, and navigating to the base URL resets to an
        empty conversation (also avoids on-load modals that intercept the send button).
        """
        self.driver.get(CHATGPT_URL)
        WebDriverWait(self.driver, self.load_wait).until(
            EC.presence_of_element_located((By.ID, "prompt-textarea"))
        )
        self.rounds.clear()

    def screenshot(self, tag: str) -> Path:
        ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
        p = ARTIFACT_DIR / f"chatgpt_{tag}_{datetime.now():%Y%m%d_%H%M%S}.png"
        self.driver.save_screenshot(str(p))
        return p

    def ask(self, prompt: str, label: str = "") -> str:
        """Send one prompt in the current conversation; return the reply text."""
        driver, wait = self.driver, WebDriverWait(self.driver, self.load_wait)
        n_before = len(driver.find_elements(By.CSS_SELECTOR, ASSISTANT_SEL))

        box = wait.until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", box)
        # insertText keeps newlines as text instead of submitting the prompt early.
        driver.execute_script(
            "arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);",
            box,
            prompt,
        )
        time.sleep(0.5)
        btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SEND_BTN_SEL)))
        try:
            btn.click()
        except Exception:
            # An overlay (modal, banner) can intercept the native click; the JS click
            # bypasses hit-testing and dispatches straight to the element.
            driver.execute_script("arguments[0].click();", btn)

        WebDriverWait(driver, self.reply_wait).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, ASSISTANT_SEL)) > n_before
        )
        reply = self._await_stable_reply()
        self.rounds.append({"label": label, "prompt": prompt, "reply": reply})
        return reply

    def _await_stable_reply(self) -> str:
        """Wait for generation to stop, then for the text to stop changing."""
        driver = self.driver
        deadline = time.time() + self.reply_wait
        last, stable = "", 0
        while time.time() < deadline:
            generating = bool(driver.find_elements(By.CSS_SELECTOR, STOP_BTN_SEL))
            msgs = driver.find_elements(By.CSS_SELECTOR, ASSISTANT_SEL)
            current = msgs[-1].text if msgs else ""
            if not generating and current and current == last:
                stable += 1
                if stable >= 3:
                    return current
            else:
                stable = 0
            last = current
            time.sleep(1.5)
        if last:
            return last
        raise ChatGPTUIError("No reply text captured before timeout.")
