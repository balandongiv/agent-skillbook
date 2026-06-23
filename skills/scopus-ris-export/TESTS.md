# Tests — Scopus RIS Export Automation

## T1: Modal false-positive detection

**Given** a Scopus page where `data-testid="exportRefinement"` is present but no real export modal exists  
**When** `handle_modal_strict(driver)` is called  
**Then** no click is made and function returns without error

**Verify**: Log shows "No strict export modal detected — skipping modal interaction."

---

## T2: Filesystem snapshot baseline

**Given** `_staging/` contains `old_file.ris` (pre-existing)  
**When** snapshot is taken, then RIS export is triggered, and `new_file.ris` appears  
**Then** `poll_for_new_ris()` returns `new_file.ris`, not `old_file.ris`

**Verify**: Only files newer than snapshot timestamp are returned.

---

## T3: Download detected in fallback directory

**Given** Chrome profile has `Downloads/` as default download dir, not `_staging/`  
**When** RIS export is triggered  
**Then** `poll_for_new_ris()` finds the file in `Downloads/` and moves it to `raw/`

**Verify**: `raw/parent_KF002_*.ris` exists and is non-empty.

---

## T4: Year-split fallback activates on timeout

**Given** full query for KF001 times out after 300s  
**When** `run_query_with_fallback(KF001_QUERY, result_count=688)` is called  
**Then** year-split loop runs for 2019–2024, producing 6 separate `.ris` files

**Verify**: `raw/KF001_2019.ris` through `raw/KF001_2024.ris` all exist.

---

## T5: Dedup merge removes title duplicates

**Given** two `.ris` files share 10 papers with identical titles (first 120 chars)  
**When** `merge_ris_files([f1, f2], output)` is called  
**Then** output contains each duplicate exactly once

**Verify**: `count_records(output) == count_records(f1) + count_records(f2) - 10`

---

## T6: Chrome LOCK file removed before session

**Given** Chrome profile `LOCK` file exists (simulating a previous crash)  
**When** `kill_chrome_and_lock()` is called  
**Then** `PROFILE_DIR/LOCK` is deleted and a new driver session starts without error

---

## T7: Select-all banner clicked

**Given** Scopus search returns 688 results across multiple pages  
**When** `select_all(driver)` is called  
**Then** the secondary "Select all 688 documents" banner is clicked

**Verify**: Export includes 688 records, not just the 25 visible on page 1.
