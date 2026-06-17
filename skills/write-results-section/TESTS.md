# Test Prompts: Write Results Section from Verified Numbers

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Write the results section from these result CSVs — don't invent any numbers.

Expected behavior: Source every value from the artifacts, reference each table/figure, and report
exact statistics with no fabricated numbers.

---

## Test Prompt 2

> Here are the verified statistics; write the main comparison paragraph staying strictly within them.

Expected behavior: Produce number-grounded prose that uses only the supplied values, with the test,
correction, comparison count, and effect size.

---

## Test Prompt 3

> Make sure every table and figure in the results is actually explained in the text.

Expected behavior: Add referencing prose for each visual stating what it shows and what to notice.

---

## Test Prompt 4

> The results mention an experiment we never actually ran — fix it.

Expected behavior: Remove or flag the ghost-analysis claim because no results artifact backs it.

---

## Test Prompt 5

> Check the results prose matches the tables exactly.

Expected behavior: Cross-check each number against its source artifact and each reference against a real
label, correcting any drift.
