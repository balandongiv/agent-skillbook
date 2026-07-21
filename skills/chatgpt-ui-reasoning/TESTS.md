# Test Prompts: ChatGPT UI Reasoning Session

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Use the ChatGPT UI to think through each of these ideas one at a time and tell me which are genuinely new."

Expected behavior: The agent reuses one persistent browser, opens a fresh chat per idea, ends each prompt with a parseable verdict line, and records unique/duplicate decisions in a ledger.

---

## Test Prompt 2

> "Screen these papers through the ChatGPT web UI and keep every response so we have an audit trail."

Expected behavior: The agent saves the raw prompt and response per item before parsing, never discards a raw response, and stores transcripts for audit.

---

## Test Prompt 3

> "The send button keeps failing to fire on ChatGPT — the page is React. Make the automation reliable."

Expected behavior: The agent removes any `is_displayed()` calls, injects text via JavaScript, and adds a JS click fallback for the send button plus a streaming-completion poll with a hard timeout.

---

## Test Prompt 4

> "Don't open a new Chrome for every abstract — that's too slow. Reuse the session."

Expected behavior: The agent keeps one browser alive and opens a new chat per item instead of relaunching the browser, rebuilding the driver only on an actual crash.

---

## Test Prompt 5

> "Run the triage again but skip anything we already evaluated."

Expected behavior: The agent consults the append-only ledger, skips items already decided, and resumes cleanly.

---

## Test Prompt 6

> "The browser won't launch — there's a leftover lock from a crash. Recover and keep going."

Expected behavior: The agent clears the stale lockfile, rebuilds the driver against the same persistent profile (without deleting the profile), and retries the current item once.

---

## Test Prompt 7

> "Have ChatGPT propose citation keys and exact metrics for these methods."

Expected behavior: The agent treats UI output as a hypothesis, refuses to let the model fabricate citation keys or numbers, and grounds factual claims against real artifacts.
