# Changelog: ChatGPT UI Reasoning Session

All notable changes to this skill are documented here.

## [Unreleased]

### Added
- "Machine-aware profile and driver resolution" section: a hostname-keyed `MACHINES` registry
  and `resolve_selenium(task)` helper so the browser binary, WebDrivers (chromedriver.exe /
  geckodriver.exe from the shared `academic_paper_maker\apm\browser` folder), and the per-task
  profile (`chatgpt` vs `scopus`) are selected automatically per computer. This machine (`rpb`)
  is filled in; two other machines are explicit `TODO` placeholders. An unregistered machine
  stops loudly instead of guessing.
- Shipped the reusable implementation under `resources/`: `machine_profiles.py` (hostname-keyed
  registry + resolver), `chatgpt_ui_session.py` (`ChatGPTSession` with `new_chat()`, JS insert +
  click fallback, stable-reply poll; profile resolved per machine, webdriver-manager with a pinned
  chromedriver fallback), and `smoke_chatgpt_ui.py` (smoke gate; exit 0/1, `smoke()` helper), plus
  a `resources/README.md`. Agents import these instead of re-writing the Selenium plumbing.
- Standing convention: run `resources/smoke_chatgpt_ui.py` as the first action of any new session
  that will drive the ChatGPT UI; if it fails, do no ChatGPT-driven work until it passes.

## [0.1.0] - 2026-07-21

### Added
- Initial version of chatgpt-ui-reasoning.
- Core instructions for driving the ChatGPT web UI via a persistent Selenium session for
  reasoning, ideation, and per-item triage: reuse one browser, new chat per item,
  JavaScript-only interaction with a click fallback, machine-parseable verdict contract,
  and preserved transcripts for audit.
- Examples covering per-paper triage against a dedup ledger, robust send on the React
  composer, and new-chat-per-item without relaunching the browser.
- Test prompts for triage, audit-trail keeping, React reliability, session reuse, resume,
  crash recovery, and refusing fabricated facts.
