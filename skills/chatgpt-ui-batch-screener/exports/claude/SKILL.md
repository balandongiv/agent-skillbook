---
name: chatgpt-ui-batch-screener
description: Automate ChatGPT web UI via Selenium to screen academic papers in batches of 5. Uses pure JS for all element checks (never is_displayed()), polls for streaming completion, extracts decisions as JSON, and saves raw fallbacks. Shares Chrome profile with Scopus — never run simultaneously.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# ChatGPT UI Batch Screener

## Overview

Automate ChatGPT web UI (chat.openai.com) via Selenium to screen academic papers in batches.
Submits structured prompts with paper metadata (title, abstract, year, source), extracts JSON
decisions, and saves per-batch response files. Works with existing browser session — no API key.

## Critical rule

**Never use `is_displayed()`** — it causes `TimeoutException` on ChatGPT's React page.
Replace every visibility check with JS: `driver.execute_script("return arguments[0].offsetParent !== null", el)`

## Batch size

Always 5 papers per batch. 1 paper = too slow; 10+ = model conflates papers.

## Streaming completion detection

```python
def is_streaming(driver) -> bool:
    return driver.execute_script("""
        var stop = document.querySelector('[data-testid="stop-button"]');
        if (stop && stop.offsetParent !== null) return true;
        var send = document.querySelector('[data-testid="send-button"]');
        if (send && send.disabled) return true;
        return false;
    """)

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

## JSON extraction (strip markdown fences)

```python
import re, json
m = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", raw, re.DOTALL)
payload = json.loads(m.group(1) if m else raw)
```

## Response file format

```json
{
  "batch_id": 42,
  "decisions": [{
    "paper_id": 317,
    "decision": "include",
    "relevance_score": 0.9,
    "reason": "...",
    "chapter_section": "2_4_explainable_artificial_intelligence",
    "mapped_objective": "3",
    "theme_label": "SHAP interpretability",
    "key_source_sentence": "..."
  }]
}
```

## Rules

- Never use `is_displayed()` — JS `offsetParent` only.
- Use Chrome profile `C:\selenium\chrome-profile` — never create new profile.
- Never run simultaneously with Scopus (shared profile).
- Always save raw response before JSON parse.
- Always include `paper_id` in prompt so response maps back to the paper.
- Start a new conversation for each batch (navigate to `https://chat.openai.com/`).
- Hard 120-second timeout fallback for streaming poll.
