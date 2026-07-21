# ChatGPT UI Reasoning Session

## Overview

Some workflows deliberately route **reasoning** — ideation, triage, synthesis, "think
harder about X" — to the ChatGPT web UI rather than an API, because a logged-in browser
session gives access to the latest reasoning model with no key management. This skill
covers driving that session **reliably and efficiently** through Selenium: one persistent
browser, a fresh chat per item, JavaScript-only element interaction, a machine-parseable
verdict contract, and a preserved transcript for every response. It is the *thinking*
counterpart to a coding agent — the UI proposes and evaluates ideas; it never becomes the
source of ground truth.

## Core principles

1. **Reuse one browser, open a new chat per item.** Do not launch a fresh browser for every
   item — that is slow and wastes the logged-in session. Keep one window open and start a
   new conversation per item (navigate to the base URL, or use the "new chat" control) so
   each item gets clean context without conflating with the previous one.
2. **Interact through JavaScript, with a click fallback.** The page is a heavy React app.
   Native Selenium `is_displayed()` and `.click()` intermittently hang or miss. Set the
   textarea value and dispatch an `input` event via `execute_script`, and if the native
   send `.click()` fails, fall back to a JS click on the send button.
3. **One item at a time for triage, against a dedup ledger.** For screening/triage, feed a
   single item per chat, record the verdict in an append-only ledger, and skip items whose
   idea/method already appears. Do not bulk many items into one prompt when the goal is a
   per-item unique/duplicate decision.
4. **Emit a machine-parseable verdict.** End each triage prompt with a fixed one-line
   contract (e.g. `VERDICT: <UNIQUE|EXTEND|DUPLICATE|NONE> | DUP_OF: ... | IDEA: ...`) and
   parse it with a regex. Free-form prose is not reliably reusable downstream.
5. **Keep every transcript.** Save the raw response (and the prompt) to a per-item file
   before parsing. Never discard a raw response — it is the audit record and can be
   recovered manually if parsing fails.
6. **Use only the designated profile.** Reuse the existing persistent Selenium profile
   directory. Never create, delete, or reset a profile, and never run two automations
   against the same profile concurrently.
7. **Be crash-resilient.** If the browser dies or a stale lockfile blocks launch, clear the
   lockfile, restart the browser, and retry the current item once before failing loudly.
8. **The UI reasons; it does not fabricate facts.** Do not let the model invent citation
   keys, dataset facts, or numbers. Ground factual claims in your own artifacts and treat
   the model output as a hypothesis to verify.

## Step-by-step process

1. **Build/attach the driver** against the persistent profile. If a lockfile from a crashed
   session exists, remove it first. Wait (JS check) until the prompt textarea exists.
2. **For each item:**
   a. Open a fresh chat (navigate base URL or click "new chat"; verify the composer reset).
   b. Compose the prompt: fixed preamble/rules + the single item + the verdict contract.
   c. Inject the text via JS (`el.value = prompt; el.dispatchEvent(new Event('input', {bubbles:true}))`).
   d. Send: try the native send button `.click()`; on failure, JS-click it.
   e. Poll for streaming completion (JS check on the stop/send button state) with a hard
      timeout fallback.
   f. Extract the last assistant message via `innerText`.
   g. **Save the raw transcript** (prompt + response) to a per-item file.
   h. Parse the verdict line with a regex; update the ledger.
3. **Skip duplicates** on subsequent runs by consulting the ledger, so reruns are resumable.
4. **On crash,** clear the lockfile, rebuild the driver, and retry the current item once.

## Machine-aware profile and driver resolution

Selenium automation in this project runs on a **small, fixed set of machines**, each with its
own browser binary, WebDrivers, and profile directories. The agent must **detect the current
machine at runtime and select that machine's paths automatically** — never hardcode one
machine's path into a run. This same registry is shared by every Selenium skill in the project
(ChatGPT-UI reasoning, ChatGPT-UI batch screening, Scopus export), so the driver binaries and
profiles are defined once.

Resolve by hostname (`socket.gethostname()`). Fill each machine's entry once; an **unknown
machine must fail loudly (stop)** rather than fall back to another machine's path.

```python
import os, socket

# WebDrivers live in the academic_paper_maker browser folder and are reused by all Selenium
# skills. Do NOT commit these binaries into a repo — reference them in place.
_APM_BROWSER = r"C:\Users\balan\IdeaProjects\academic_paper_maker\apm\browser"

# Per-machine Selenium layout, keyed by hostname (lowercased). Three machines are in rotation;
# only "rpb" (this computer) is filled in — add the other two when those machines are set up.
MACHINES = {
    "rpb": {  # this computer
        "chromedriver": rf"{_APM_BROWSER}\chromedriver.exe",
        "geckodriver":  rf"{_APM_BROWSER}\geckodriver.exe",
        "chrome_exe":   r"C:\Users\balan\AppData\Local\Google\Chrome\Application\chrome.exe",
        "profiles": {
            "chatgpt": r"C:\selenium\chatgpt-profile",
            "scopus":  r"%LOCALAPPDATA%\Google\Chrome\User Data",  # profile name: "Default"
        },
    },
    # "MACHINE-2": { ... TODO: fill drivers, chrome_exe, profiles when this machine is set up ... },
    # "MACHINE-3": { ... TODO ... },
}

def resolve_selenium(task: str) -> dict:
    """Return this machine's driver / chrome / profile paths for a task ('chatgpt' | 'scopus')."""
    host = socket.gethostname().lower()
    if host not in MACHINES:
        raise RuntimeError(
            f"Unknown machine '{host}': register its Selenium layout in MACHINES before running. "
            f"Never fall back to another machine's paths."
        )
    machine = MACHINES[host]
    if task not in machine["profiles"]:
        raise KeyError(f"No '{task}' profile configured for machine '{host}'.")
    return {
        "chromedriver": machine["chromedriver"],
        "geckodriver":  machine["geckodriver"],
        "chrome_exe":   machine["chrome_exe"],
        "profile":      os.path.expandvars(machine["profiles"][task]),
    }
```

Notes:
- The `chatgpt` and `scopus` profiles are deliberately separate so their sessions never collide.
- Only the current machine's values are known and verified; the other two entries are explicit
  `TODO` placeholders to be filled later — an unregistered machine stops rather than guesses.

## Rules

- Always resolve the browser, drivers, and profile from the machine registry by hostname; never
  hardcode a single machine's paths, and stop loudly on an unregistered machine.
- Always reuse one browser and open a new chat per item; never relaunch the browser per item.
- Never call `is_displayed()` on the ChatGPT page; use a JS `offsetParent`/state check.
- Always provide a JS click fallback for the send button.
- Always save the raw transcript before parsing, and keep all transcripts for audit.
- Always end triage prompts with the fixed, regex-parseable verdict line.
- Use only the designated persistent profile; never create/delete a profile; never run two
  UI automations against it at once.
- Never treat model output as ground truth; verify facts against your own artifacts.

## Common mistakes to avoid

- **Relaunching Chrome per item.** Wastes the session and time; keep one window, new chat.
- **Native visibility/click on React.** `is_displayed()` hangs; a native `.click()` silently
  misses. Use JS and a click fallback.
- **Bulk items in one triage chat.** The model conflates them and the per-item unique/dup
  decision degrades. One item per chat for triage.
- **Discarding the raw response** when parsing fails. Save raw first; parse second.
- **Stale lockfile / orphaned Chrome** blocking launch. Detect, clear the lockfile, retry —
  but never delete the user's other Chrome data or the profile itself.
- **Free-form verdicts.** Without the fixed contract line, downstream code cannot reliably
  reduce responses to decisions.
