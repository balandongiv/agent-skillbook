# Test Prompts: Write Discussion Section with Defensible Claims

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Write the discussion interpreting these results without overclaiming.

Expected behavior: Anchor interpretations to reported results, use hedged causal/novelty language, and
add an honest limitations paragraph.

---

## Test Prompt 2

> Soften the causal and "first study" claims in my discussion.

Expected behavior: Convert "causes/proves/first study" to "may/consistent with/to our knowledge, among
the first" while preserving meaning.

---

## Test Prompt 3

> Add a limitations paragraph grounded in what we actually did.

Expected behavior: Produce specific limitations (dataset scope, method assumptions, missing baselines,
generalisation) rather than a vague disclaimer.

---

## Test Prompt 4

> Make sure the discussion doesn't introduce numbers that aren't in the results.

Expected behavior: Reference only already-reported values; flag any number with no results anchor.

---

## Test Prompt 5

> Does the discussion claim anything the experiments don't support?

Expected behavior: Atomise and check claims, flag unsupported contributions/analyses, and soften or
remove them.
