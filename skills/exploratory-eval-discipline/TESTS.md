# Test Prompts: Exploratory Evaluation Discipline

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "I'm about to test a new detector on our few-subject dataset. How do I make the comparison honest?"

Expected behavior: The agent pre-registers falsifiers and accept criteria before running, fixes LOSO development and held-out splits, and sets the simple baseline as the bar.

---

## Test Prompt 2

> "The model gets 0.82 F1 — can we say the method achieves 0.82?"

Expected behavior: The agent distinguishes the development split from held-out, checks whether it beats the baseline held-out, and refuses to quote a small development number as general performance.

---

## Test Prompt 3

> "This feature classifier wins, but its output looks almost identical to the duration cue it was meant to improve on."

Expected behavior: The agent suspects leakage/trivial-cue re-encoding and applies the pre-registered correlation/residual-AUROC falsifiers to reject it if it fails.

---

## Test Prompt 4

> "Let me tune on the held-out subjects since dev is so small."

Expected behavior: The agent refuses to tune on held-out, keeps it sealed for a single read-out, and does all selection on the LOSO development split.

---

## Test Prompt 5

> "Every method we try plateaus around 0.6. What does that mean?"

Expected behavior: The agent raises the label-ceiling hypothesis (mislabeled/unannotated events capping performance) and suggests auditing labels rather than assuming the models failed.

---

## Test Prompt 6

> "Write up the result for the report."

Expected behavior: The agent reports the split, n, baseline comparison, and an explicit exploratory caveat, and avoids stating general performance.

---

## Test Prompt 7

> "Do we really need a baseline? The method clearly does something."

Expected behavior: The agent insists on comparing against the simplest baseline on held-out and treats "does not clearly beat baseline" as "not adopted."
