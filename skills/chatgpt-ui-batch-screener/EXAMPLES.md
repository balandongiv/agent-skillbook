# Examples — ChatGPT UI Batch Screener

## Example 1: Batch 42 prompt and response

### Input prompt (submitted to ChatGPT)
```
You are a systematic literature review assistant. Screen the following 5 papers for relevance
to a thesis on thermal and mechanical failure classification using machine learning.

For each paper, respond with a JSON array (no markdown). Fields:
  paper_id, decision (include/exclude/maybe/needs_full_text), relevance_score (0.0-1.0),
  reason (one sentence), chapter_section, mapped_objective, theme_label, key_source_sentence

Chapter sections available:
  2_2_thermal_and_mechanical_feature_engineering
  2_3_machine_learning_for_failure_classification
  2_4_explainable_artificial_intelligence
  2_5_research_gap

--- PAPER 317 ---
Title: SHAP-based Interpretability for Predictive Maintenance
Abstract: This study applies SHAP values to random forest models trained on vibration signals...
Year: 2024 | Source: Journal of Manufacturing Systems
```

### ChatGPT response (raw)
```json
[
  {
    "paper_id": 317,
    "decision": "include",
    "relevance_score": 0.9,
    "reason": "Directly applies SHAP to predictive maintenance ML — core XAI evidence.",
    "chapter_section": "2_4_explainable_artificial_intelligence",
    "mapped_objective": "3",
    "theme_label": "SHAP interpretability",
    "key_source_sentence": "SHAP values revealed that cutting speed contributed most to wear prediction accuracy across all tested classifiers."
  }
]
```

---

## Example 2: Streaming detection — wrong vs correct

### Wrong (causes TimeoutException)
```python
# is_displayed() hangs on React SPA
send_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="send-button"]')
if send_btn.is_displayed() and not send_btn.get_attribute("disabled"):
    # hangs here or throws TimeoutException
    pass
```

### Correct (pure JS)
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

---

## Example 3: JSON extraction from markdown-wrapped response

### What ChatGPT returns
````
```json
[{"paper_id": 317, "decision": "include", ...}]
```
````

### Extraction code
```python
import re, json

raw = extract_last_response(driver)
# Strip ```json ... ``` fences
m = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", raw, re.DOTALL)
if m:
    payload = json.loads(m.group(1))
else:
    payload = json.loads(raw)   # try bare JSON
```

Always save the raw text before parsing:
```python
(batch_dir / f"response_{batch_id:03d}_raw.txt").write_text(raw, encoding="utf-8")
```

---

## Example 4: Resuming after interruption

### What the progress tracker looks like mid-run
```json
{
  "222": {"status": "done", "at": "2026-06-20T08:32:11"},
  "223": {"status": "done", "at": "2026-06-20T08:33:07"},
  "224": {"status": "in_progress", "at": "2026-06-20T08:34:01"}
}
```

### Resume logic
```python
for batch_id in range(1, total_batches + 1):
    resp_file = batch_dir / f"response_{batch_id:03d}.json"
    if resp_file.exists():
        continue   # already done, skip
    # ... process batch ...
```
