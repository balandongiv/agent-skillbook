# Tests — ChatGPT UI Batch Screener

## T1: is_displayed() replaced with JS check

**Given** a ChatGPT page where the send button is visible  
**When** `is_streaming(driver)` is called  
**Then** it returns a boolean without raising TimeoutException or WebDriverException

**Verify**: No call to `element.is_displayed()` anywhere in the script (`grep -n "is_displayed"` returns nothing).

---

## T2: Raw response always saved before parse attempt

**Given** ChatGPT returns a response  
**When** the batch response is processed  
**Then** `response_042_raw.txt` exists before `json.loads()` is called

**Verify**: Raw file timestamp <= JSON file timestamp.

---

## T3: Markdown fence stripped from JSON

**Given** ChatGPT response is wrapped in ` ```json ... ``` `  
**When** the extraction function processes the raw text  
**Then** `json.loads()` succeeds and produces a list of decision dicts

**Verify**: `payload[0]["paper_id"]` returns an integer, no JSONDecodeError.

---

## T4: Batch resume skips completed batches

**Given** `response_001.json` through `response_100.json` exist  
**When** the screener script starts from batch 1  
**Then** batches 1–100 are skipped and processing begins at batch 101

**Verify**: First `driver.get("https://chat.openai.com/")` call is for batch 101.

---

## T5: 5-paper batch limit respected

**Given** 1317 papers to screen  
**When** `create_batches(papers, batch_size=5)` is called  
**Then** 264 batch files are created (ceil(1317 / 5) = 264), last batch has ≤ 5 papers

**Verify**: `len(batch_264["papers"]) == 2` (1317 % 5 = 2).

---

## T6: Profile never switched or recreated

**Given** the script is configured with `PROFILE_DIR = r"C:\selenium\chrome-profile"`  
**When** the driver is built  
**Then** no other profile path is used, and the profile directory is not created fresh

**Verify**: Chrome options `--user-data-dir` arg equals the configured profile exactly.

---

## T7: Streaming timeout hard cap

**Given** ChatGPT streaming does not complete within 120s  
**When** the polling loop runs  
**Then** the loop exits after 120s and logs a timeout warning (does not hang indefinitely)

**Verify**: Elapsed time between send and next batch start is ≤ 125s in the worst case.
