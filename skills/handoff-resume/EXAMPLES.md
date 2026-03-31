# Examples: Handoff Resume

---

## Example 1: Resuming from a handoff instead of chat history

### Before (without this skill)

```text
Skim the conversation and continue whatever seems unfinished.
```

### After (with this skill applied)

```text
1. Read `planning/Project_Execution_Flowchart.md`.
2. Read `handoff/20260331_subject_performance_handoff.md`.
3. Extract the pending-work table.
4. Execute the unfinished tasks in dependency order.
5. Mark each finished task `Done? = Yes` with the validating artifact or log path.
```

### Why it's better

It resumes from the durable repository artifact instead of from a possibly incomplete conversational reconstruction.

---

## Example 2: Updating the handoff as work completes

### Before (without this skill)

```text
Finish the manuscript task and mention in chat that it was done.
```

### After (with this skill applied)

```text
Update the handoff table:

| Task | Done? | Evidence / Next step |
| --- | --- | --- |
| Rebuild manuscript after result edits | Yes | Rebuilt `writing/out/main.pdf`; compile log `.codex-tmp/live_logs/subject_comparison_latex.log` |
```

### Why it's better

The state of the work now lives in the handoff itself, which makes the next resume point obvious and auditable.

---

## Example 3: Checking process state before relaunching

### Before (without this skill)

```text
The old monitor probably died, so start a new one.
```

### After (with this skill applied)

```text
1. Read the handoff note about the monitor.
2. Verify with `ps` whether `monitor_runbook_live.py` is still active.
3. Start a new monitor only if the old one is confirmed dead or intentionally stopped.
```

### Why it's better

It prevents duplicate background jobs and keeps the resumed run state consistent with reality.
