# Test Prompts: MNE Blink Report HTML

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Make an HTML report that plots each detected blink window one by one.

Expected behavior: Generate a saved MNE HTML report with per-blink figures from the epoch data.

---

## Test Prompt 2

> Show me only the false negatives as plots so I can see what we missed.

Expected behavior: Build the report filtered to the false-negative subset with padding and the chosen
channels.

---

## Test Prompt 3

> Plot true positives and false positives separately for comparison.

Expected behavior: Produce two reports (or subsets) for TP and FP windows.

---

## Test Prompt 4

> Add padding around each blink window and restrict to the frontal channels.

Expected behavior: Apply configurable padding and channel selection in the report.

---

## Test Prompt 5

> I want a blink-by-blink sanity check in HTML rather than just a metrics table.

Expected behavior: Generate the HTML blink report as a visual QA artifact.
