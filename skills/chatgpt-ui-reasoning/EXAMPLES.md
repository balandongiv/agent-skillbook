# Examples: ChatGPT UI Reasoning Session

---

## Example 1: Per-paper triage against a dedup ledger

### Before (without this skill)

```text
Open a new Chrome window.
Paste all 30 abstracts into one chat.
Ask "which of these are novel?"
Copy the prose answer into notes.
Close Chrome. Repeat tomorrow from scratch.
```

### After (with this skill applied)

```text
1. Attach to the persistent profile (clear a stale lockfile if present); reuse one window.
2. For each paper, one at a time:
   a. Open a fresh chat (verify the composer reset).
   b. Prompt = fixed preamble + this single abstract + the verdict contract line.
   c. Inject text via JS; send with native click, JS-click fallback.
   d. Poll for streaming end (JS state check, 120s hard cap); read innerText.
   e. Save prompt+response to reports/triage/transcripts/paper_<id>.md.
   f. Parse "VERDICT: UNIQUE | IDEA: ..." with regex; append to ledger.csv.
3. On the next run, skip papers already in ledger.csv (resumable).
```

### Why it's better

Each paper gets clean context, the decision is a parseable verdict (not prose), every
response is preserved for audit, and the run is resumable and deduplicated instead of a
one-shot bulk prompt that conflates papers and leaves no trail.

---

## Example 2: Robust send on the React composer

### Before (without this skill)

```python
box = driver.find_element(By.CSS_SELECTOR, "textarea")
if box.is_displayed():          # hangs on ChatGPT's React page
    box.send_keys(prompt)
driver.find_element(By.CSS_SELECTOR, '[data-testid="send-button"]').click()  # silently misses
```

### After (with this skill applied)

```python
# Inject via JS (no is_displayed, no send_keys races)
driver.execute_script(
    "arguments[0].value = arguments[1];"
    "arguments[0].dispatchEvent(new Event('input', {bubbles:true}));",
    box, prompt,
)
send = driver.find_element(By.CSS_SELECTOR, '[data-testid="send-button"]')
try:
    send.click()
except Exception:
    driver.execute_script("arguments[0].click();", send)   # JS click fallback
```

### Why it's better

It never calls the visibility method that hangs the React page, and it guarantees the send
actually fires by falling back to a JS click when the native click is intercepted.

---

## Example 3: New chat per item without relaunching the browser

### Before (without this skill)

```text
driver.quit()
driver = build_driver(profile)   # cold start every item — slow, re-auth risk
driver.get("https://chatgpt.com/")
```

### After (with this skill applied)

```text
1. Keep the single driver alive for the whole run.
2. Per item: driver.get(BASE_URL)  (or click the "new chat" control),
   then JS-verify the composer is empty and no prior messages are present.
3. Only rebuild the driver if the browser actually crashed.
```

### Why it's better

Reusing one window keeps the logged-in session warm and is far faster across many items,
while a fresh chat per item still guarantees clean per-item context.
