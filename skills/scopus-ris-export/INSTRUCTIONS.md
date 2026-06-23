# Scopus RIS Export Automation

## Overview

Automate Scopus Advanced Search and bulk RIS export using Selenium on a persistent Chrome profile.
Handles query entry, Select-all banner, Export dropdown, RIS selection, and download polling across
multiple directories. Includes per-year sub-query fallback when the full result set exceeds 2000 docs,
and a Chrome restart between batches to prevent session-level export cap failures.

## Core principles

1. **No modal assumptions** — After clicking RIS, poll the filesystem directly. Only interact with
   a count modal if it contains both a numeric input field AND an Export button (strict check).
   Never treat a partial `data-testid*="export"` match as the real modal.
2. **Poll three directories** — Check `_staging/`, `Downloads/`, and `Desktop/` for new `.ris` files.
   Scopus may route downloads to any of these depending on browser settings.
3. **Restart Chrome between batches** — Scopus enforces a per-session export cap (~7–8 per day).
   Kill `chrome.exe`, remove the profile LOCK file, and rebuild the driver before each batch.
4. **Use a persistent profile** — Always use the same pre-logged-in Chrome profile. Never create a new
   profile or switch profiles mid-pipeline.
5. **Year-split fallback** — If the full query returns > 2000 docs or times out, split by
   `AND PUBYEAR = YYYY` for each active year and merge results with title-based dedup.

## Step-by-step process

1. **Kill any existing Chrome session** and remove the profile LOCK file.
2. **Build the Chrome driver** with download prefs pointing to `_staging/`.
3. **Navigate** to `https://www.scopus.com/search/form.uri?display=advanced`.
4. **Enter the query** via JS `execCommand('insertText')` (works on Scopus's contenteditable div).
5. **Submit** and wait for result count (poll `page_source` for `N documents`).
6. **Select all** — click the primary Select-all control, then click the secondary
   "Select all N documents" banner if it appears.
7. **Take a filesystem snapshot** of all poll directories (name → mtime).
8. **Open Export dropdown** via ActionChains click on the Export button.
9. **Wait for RIS** button to appear in dropdown (`data-testid="export-to-ris"`).
10. **Click RIS** via ActionChains.
11. **Handle modal strictly** — only click Export if the modal contains both a count input
    and an Export/Download button. If no strict modal is detected, skip.
12. **Poll filesystem** every 3 seconds for up to 5 minutes for any new `.ris` file.
13. **Move** the downloaded file to `literature/scopus/raw/parent_{batch_id}_{date}.ris`.
14. **Update** `scopus_query_log.csv` status to `done`.
15. **Merge** if multiple batch files exist, deduplicating by title (first 120 chars, lowercased).

## Rules

- Always kill Chrome and remove the LOCK file before building a new driver session.
- Always snapshot poll directories before triggering the export, using the snapshot as baseline.
- Never match `data-testid*="export"` as the export modal — require a count input inside the element.
- Never use `is_displayed()` on Scopus pages — use JS `offsetParent !== null` instead.
- Never skip the secondary "Select all N documents" banner — without it, only the visible page is selected.
- Always check Downloads, staging, and Desktop — do not assume the staging dir.
- Always restart Chrome between export batches on long sessions.
- Never run Scopus and ChatGPT automation simultaneously if they share a Chrome profile.

## Common mistakes to avoid

- **False-positive modal**: `data-testid="exportRefinement"` ("Export filter counts" button) matches
  `[data-testid*="export"]`. This causes the script to click the wrong element and stall.
- **Daily cap hit silently**: Scopus stops delivering files without error after ~7–8 exports. The modal
  still appears and looks normal. Track export session count.
- **Download goes to wrong dir**: If the Chrome profile was previously used with a different download path,
  the file lands in `Downloads/` not `_staging/`. Always poll all three.
- **LOCK file blocking new session**: If a previous Chrome crashed, the LOCK file remains. Always remove it.
- **Select-all only selects the page**: The primary checkbox selects only visible results. The secondary
  banner "Select all N documents" must also be clicked for full export.

## Configuration reference

```python
CHROME_EXE  = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_DIR = r"C:\selenium\chrome-profile"   # BINDING — never change

POLL_DIRS = [
    RAW_DIR / "_staging",
    Path(r"C:\Users\<user>\Downloads"),
    Path(r"C:\Users\<user>\Desktop"),
]
POLL_TIMEOUT    = 300    # seconds per batch
BETWEEN_SLEEP   = 3      # seconds between filesystem polls
BATCH_THRESHOLD = 1100   # split if result count exceeds this
```
