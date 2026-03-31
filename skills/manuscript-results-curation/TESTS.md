# Test Prompts: Manuscript Results Curation

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Edit the LaTeX results section directly and add a detailed conclusion from the completed experiments."

Expected behavior: The agent edits the manuscript source directly, grounds the text in experiment outputs, and writes a conclusion with concrete interpretation.

---

## Test Prompt 2

> "Add a table or graph to the manuscript and explain what it means."

Expected behavior: The agent creates or inserts the visual artifact, adds explanatory text, and ties the interpretation to the actual result.

---

## Test Prompt 3

> "Write up the result in the paper, not in the generator."

Expected behavior: The agent avoids generator-based narrative insertion and edits the LaTeX manuscript directly.

---

## Test Prompt 4

> "Turn these run artifacts into manuscript-ready figures and discussion."

Expected behavior: The agent derives reproducible tables or figures from the artifacts and adds detailed scientific interpretation around them.

---

## Test Prompt 5

> "Update `writing/result/result.tex`, rebuild the PDF, and tell me whether the result suggests we are on the right track."

Expected behavior: The agent performs direct manuscript edits, rebuilds the manuscript, and explains whether the results support the current direction or reveal setup problems.
