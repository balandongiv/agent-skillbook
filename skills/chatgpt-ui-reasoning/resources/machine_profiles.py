"""Machine-aware Selenium layout — single source for browser/driver/profile paths.

Selenium automation runs on a small, fixed set of machines. Resolve by hostname
(`socket.gethostname()`); an unregistered machine raises rather than falling back to
another machine's profile. Shared by every Selenium skill (ChatGPT UI, Scopus, ...).

Only this computer ("rpb") is filled in. Add the other two machines when they are set
up — copy the "rpb" block, change the hostname key, and set that machine's paths.
"""
from __future__ import annotations

import os
import socket

# Shared WebDrivers (chromedriver.exe / geckodriver.exe). Referenced in place — the
# binaries are NOT vendored into this repo. `ChatGPTSession` uses webdriver-manager by
# default (auto-matches the installed Chrome); this path is the pinned fallback.
_APM_BROWSER = r"C:\Users\balan\IdeaProjects\academic_paper_maker\apm\browser"

MACHINES: dict[str, dict] = {
    "rpb": {  # this computer
        "chromedriver": rf"{_APM_BROWSER}\chromedriver.exe",
        "geckodriver": rf"{_APM_BROWSER}\geckodriver.exe",
        "chrome_exe": r"C:\Users\balan\AppData\Local\Google\Chrome\Application\chrome.exe",
        "profiles": {
            "chatgpt": r"C:\selenium\chatgpt-profile",
            "scopus": r"%LOCALAPPDATA%\Google\Chrome\User Data",  # profile name: "Default"
        },
    },
    # "MACHINE-2": { ... TODO: fill drivers, chrome_exe, profiles ... },
    # "MACHINE-3": { ... TODO ... },
}


def current_machine() -> dict:
    """Return this machine's layout, or raise if the machine is not registered."""
    host = socket.gethostname().lower()
    if host not in MACHINES:
        raise RuntimeError(
            f"Unknown machine '{host}': register its Selenium layout in MACHINES before "
            f"running. Never fall back to another machine's paths."
        )
    return MACHINES[host]


def resolve_selenium(task: str) -> dict:
    """Resolve driver / chrome / profile paths for a task ('chatgpt' | 'scopus')."""
    machine = current_machine()
    if task not in machine["profiles"]:
        host = socket.gethostname().lower()
        raise KeyError(f"No '{task}' profile configured for machine '{host}'.")
    return {
        "chromedriver": machine["chromedriver"],
        "geckodriver": machine.get("geckodriver", ""),
        "chrome_exe": machine["chrome_exe"],
        "profile": os.path.expandvars(machine["profiles"][task]),
    }


def resolve_scopus() -> tuple[str, str, str]:
    """Convenience for the Scopus skill: (chromedriver, chrome_exe, profile)."""
    r = resolve_selenium("scopus")
    return r["chromedriver"], r["chrome_exe"], r["profile"]
