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
