# Examples — Scopus RIS Export Automation

## Example 1: Full query export (< 2000 results)

### Scenario
KF002 has 128 results. Single batch export.

### What worked
```python
kill_chrome_and_lock()
driver = build_driver(profile_dir=PROFILE_DIR, staging_dir=STAGING_DIR)
driver.get("https://www.scopus.com/search/form.uri?display=advanced")
enter_query(driver, KF002_QUERY)
submit_search(driver)
wait_for_results(driver)    # polls "128 documents" in page_source
select_all(driver)          # primary checkbox + banner
snapshot = snapshot_dirs(POLL_DIRS)
open_export_dropdown(driver)
click_ris(driver)
handle_modal_strict(driver) # no strict modal → skipped (not an error)
new_file = poll_for_new_ris(POLL_DIRS, snapshot, timeout=300)
move_to_raw(new_file, "KF002")
update_query_log("KF002", "done", 128)
```

### Why it's better than the naive approach
The naive approach used `driver.find_element(By.CSS_SELECTOR, "[data-testid*='export']")` 
which matched the "Export filter counts" button (exportRefinement), not the export modal.
This approach takes a filesystem snapshot and polls directories directly, so it succeeds
even if the modal never appears.

---

## Example 2: Year-split fallback for > 2000 results

### Scenario
KF001 has 688 results within limit but Scopus session cap was hit after 7 earlier exports.
The full export stalls. Year-split fallback downloads 2019–2024 separately.

### What worked
```python
for year in range(2019, 2025):
    query = f"{KF001_BASE_QUERY} AND PUBYEAR = {year}"
    # ... same flow as Example 1 ...
    move_to_raw(new_file, f"KF001_{year}")
# Merge and dedup by title (first 120 chars, lowercase)
merge_ris_files(glob("literature/scopus/raw/KF001_*.ris"), "KF001_merged.ris")
```

### Why it's better
Full-batch download fails silently when Scopus session cap is hit. Per-year splits keep each
batch well under the cap limit and make partial resume possible (skip years already downloaded).

---

## Example 3: Distinguishing false-positive modal from real modal

### What fails
```python
# BAD — matches exportRefinement button, not the real export modal
modal = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid*='export']"))
)
# This is actually a filter-counts export button, not the download modal
modal.click()  # opens wrong dialog, download never starts
```

### What works
```python
# GOOD — strict check: requires count input AND export/download button inside
def handle_modal_strict(driver, timeout=10):
    try:
        modal = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='exportModal'], [role='dialog']")
            )
        )
        has_count_input = bool(modal.find_elements(By.CSS_SELECTOR, "input[type='number']"))
        has_export_btn  = bool(modal.find_elements(By.CSS_SELECTOR, "button[data-testid='export-button']"))
        if has_count_input and has_export_btn:
            modal.find_element(By.CSS_SELECTOR, "button[data-testid='export-button']").click()
    except TimeoutException:
        pass  # No modal is fine — download may proceed without one
```
