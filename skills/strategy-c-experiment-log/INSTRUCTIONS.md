# Strategy C Experiment Log Instructions

This skill exists so that every exploratory experiment, validation pass, or investigative task that touches Strategy C also generates a structured entry in a log file under `development_strategy/strategy_C/obs/`. Use the active Strategy C approach log for the current experiment and mirror the same headings, sections, and tone already established there.

## Step 1: Confirm the request is exploratory
Ask yourself (and the user) whether the work is:
- trying an alternate implementation, dataset, or parameter setting for Strategy C
- running a validation, benchmark, or comparison of Strategy C components
- building intuition about what a future Strategy C change should do
If yes, activate this skill and remind the user that the log entry will live in the template file. If the user explicitly says “no logging,” skip this skill.

## Step 2: Collect the facts before writing
Before writing the entry gather:
- a concise experiment or hypothesis name (Strategy name)
- the current date (YYYY-MM-DD) for the **Date** field
- a clear **Proposal** (“What are we trying?”) and **Rationale** (“Why might this work?”)
- the current **Status** (Proposed, In Progress, Completed, Abandoned)
- the code paths, files, or commands that will change or be exercised
- initial metrics you expect to track
- the implementation-level benefit hypothesis versus Strategy A and Strategy B,
  not just the expected metric movement

## Step 3: Append to the template log
Add a ## Strategy: … section to the selected Strategy C log file under `development_strategy/strategy_C/obs/` with the following subsections exactly as the template uses:
1. **Date**, **Proposal**, **Rationale**, **Status**
2. ### Implementation covering **Files Changed** and **Commits**
3. ### Performance & Metrics with **Before**, **After**, and **Change** (include sources)
4. ### Implementation Benefits explaining why the approach is or is not a better implementation foundation than Strategy A and Strategy B, apart from raw metrics
5. ### Issues Encountered listing each issue, impact, and resolution status
6. ### Outcome stating success/failure/mixed verdict
7. ### Learnings summarizing what next time should heed

The **Implementation Benefits** section should answer questions like:
- Is the approach more modular than Strategy A?
- Is it easier to inspect, debug, or evolve than Strategy B?
- Does it keep a cleaner candidate-region contract for downstream Stages 2 to 6?
- Does it support targeted rescue logic or later long-closure extension without rewriting Stage 1?

If no implementation benefit was demonstrated, say that explicitly instead of leaving the section vague.

If you are not ready to report metrics, mark them as TBD and promise to update the entry later, but still add placeholders for the required sections.

## Step 4: Keep the log consistent
- Always write to a Strategy C log under `development_strategy/strategy_C/obs/`.
- Prefer the existing approach log that matches the experiment you are extending, for example `log_strategy_c_approach3.md` when continuing Approach 3 work.
- Keep entries in chronological order (append to the bottom).
- Mirror the tone and formatting (two spaces for line breaks after bold labels, bullet lists for items, etc.).
- When experiments run multiple stages, consider writing ## Strategy: [Name] — Iteration X sections to track iterations.

## Step 5: Notify the user
After updating the log, tell the user where the entry lives, which sections you filled, and what (if anything) remains pending. Encourage them to keep the **Status** accurate as the work evolves.
