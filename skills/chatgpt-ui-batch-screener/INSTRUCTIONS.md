# ChatGPT UI Batch Screener

## Overview

Automate ChatGPT web UI (chat.openai.com) via Selenium to screen academic papers in batches.
Submits structured prompts with paper metadata (title, abstract, year, source), extracts JSON
decisions (include / exclude / maybe / needs_full_text), and saves per-batch response files.
Works with the existing browser session — no API key required.

## Core principles

1. **Pure JS for all element checks** — Never call `is_displayed()` on ChatGPT pages. It causes
   `TimeoutException` on heavy React/JS pages. Use `driver.execute_script("return arguments[0].offsetParent !== null", el)` for visibility.
2. **5 papers per batch** — Submitting 1 paper is too slow (264 batches); submitting 10+ risks
   mixing papers in the response. 5 is the reliable optimum.
3. **Poll for streaming completion** — After submitting a prompt, detect streaming end by checking
   for the stop-button disappearance or the send-button becoming active again (JS only).
4. **Extract response as `innerText`** — Use `driver.execute_script("return el.innerText")` on
   the last response container. Never use `innerHTML` (tags corrupt the JSON).
5. **Save raw fallback** — If JSON parse fails, save the raw text as `response_NNN_raw.txt`.
   Never discard a raw response; it can be manually recovered later.

## Batch file format (input)

```json
{
  "batch_id": 42,
  "papers": [
    {
      "paper_id": 317,
      "title": "SHAP-based Interpretability for Predictive Maintenance",
      "abstract": "This study applies SHAP...",
      "year": 2024,
      "source_title": "Journal of Manufacturing Systems"
    }
  ]
}
```

## Response file format (output)

```json
{
  "batch_id": 42,
  "decisions": [
    {
      "paper_id": 317,
      "decision": "include",
      "relevance_score": 0.9,
      "reason": "Directly relevant to XAI in predictive maintenance",
      "chapter_section": "2_4_explainable_artificial_intelligence",
      "mapped_objective": "3",
      "theme_label": "SHAP interpretability",
      "key_source_sentence": "SHAP assigns importance values to features..."
    }
  ]
}
```

## Step-by-step process

1. **Export batches** — Create `batch_NNN.json` files (N papers each) in `reports/screening/`.
2. **Open ChatGPT** — Navigate to `https://chat.openai.com/` using the persistent Chrome profile.
   Wait for the session to be active (JS check for prompt textarea presence).
3. **For each batch**:
   a. Build the prompt: system instructions + formatted paper list.
   b. Find the prompt textarea via JS (never `find_element` with `is_displayed()`).
   c. Inject text: `element.value = prompt; element.dispatchEvent(new Event('input'))`.
   d. Click the send button via JS.
   e. Poll for streaming completion (stop-button gone AND send-button active).
   f. Extract last response container text via `innerText`.
   g. Parse JSON from the response (strip markdown code fences first).
   h. Save to `response_NNN.json`; save raw to `response_NNN_raw.txt` if parse fails.
4. **Track progress** in `screening_progress.json` with `{batch_id: {status, at}}`.
5. **Resume support** — Skip batches already present in `response_*.json` on restart.

## Streaming completion detection

```python
def is_streaming(driver) -> bool:
    return driver.execute_script("""
        // Stop button visible = still streaming
        var stop = document.querySelector('[data-testid="stop-button"]');
        if (stop && stop.offsetParent !== null) return true;
        // Send button disabled = still streaming
        var send = document.querySelector('[data-testid="send-button"]');
        if (send && send.disabled) return true;
        return false;
    """)

# Poll until not streaming (max 120s)
deadline = time.monotonic() + 120
while time.monotonic() < deadline:
    if not is_streaming(driver):
        break
    time.sleep(2)
```

## Response extraction

```python
def extract_last_response(driver) -> str:
    return driver.execute_script("""
        var msgs = document.querySelectorAll('[data-message-author-role="assistant"]');
        if (!msgs.length) return '';
        return msgs[msgs.length - 1].innerText || msgs[msgs.length - 1].textContent || '';
    """) or ""
```

## Rules

- Never use `is_displayed()`, `element.is_displayed()`, or any Selenium visibility method.
- Always use the same Chrome profile as Scopus — never create a new profile.
- Never run ChatGPT and Scopus automation simultaneously (shared Chrome profile).
- Always start a new conversation for each batch (navigate to `https://chat.openai.com/`).
- Always save the raw response before attempting JSON parse.
- Always include `paper_id` in the prompt so the response can be matched back to the paper.
- Never invent citation keys, paper titles, or methodology details in prompts or responses.

## Common mistakes to avoid

- **`is_displayed()` hangs**: ChatGPT's React page causes `TimeoutException` on any Selenium
  visibility check. Replace every such call with the JS `offsetParent` check.
- **Mixed papers in response**: Batches > 5 papers risk the model conflating papers. Keep to 5.
- **Streaming not detected**: If stop/send button selectors change, the poller never exits.
  Add a hard timeout fallback (120s) and log the selector failure.
- **JSON buried in markdown**: ChatGPT often wraps JSON in ` ```json ... ``` `. Strip fences
  with regex before `json.loads()`.
- **Profile lock blocks launch**: If a previous session crashed, remove the LOCK file from the
  Chrome profile before building the driver.
