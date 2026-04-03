---
name: mne-blink-report-html
description: Generate an MNE Report HTML that plots blink windows one by one from epoch-based blink data, including true positives, false negatives, false positives, or all blinks, with configurable padding before and after each blink. Use when the user wants the same kind of per-blink sanity-check plotting as the Strategy C Approach 3 report or asks for reusable blink-report plotting from MNE epoch files and blink tables.
---

# MNE Blink Report HTML

Use this skill to generate a saved MNE HTML report that plots blink windows one by one from epoch data.

## Workflow

1. Identify the epoch file, predicted blink table, and reference blink table if matching is needed.
2. Normalize blink-table columns to `epoch_index`, `blink_onset`, and `blink_duration`.
3. Choose the subset to plot: true positives, false negatives, false positives, all predicted, or all reference.
4. Start from `scripts/report_blink_windows_template.py`.
5. Plot each blink with `0.5 s` before and after by default.
6. Save the output with `mne.Report` and report the exact HTML path.

## Rules

- Always match predicted and reference blinks by interval overlap within the same epoch.
- Always include a summary section, a table of plotted rows, and one figure per blink.
- Prefer the frontal plotting set unless the user explicitly asks for a broader montage.
- Keep reference and predicted intervals visually distinct in every figure.

## Bundled resources

- Template script: `scripts/report_blink_windows_template.py`
- Notes: `resources/notes.md`
