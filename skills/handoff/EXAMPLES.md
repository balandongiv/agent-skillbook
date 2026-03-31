# Examples: Handoff

---

## Example 1: Turning a loose recap into an operational handoff

### Before (without this skill)

```text
I fixed the report stage and stopped the monitor.
There are still a few things left.
Next time, check the manuscript and maybe rerun something.
```

### After (with this skill applied)

```text
Create handoff/20260331_report_followup.md with:

- Scope
- What Has Been Done
- What Is Stopped
- Current Working State
- Pending Work
- Suggested Next Commands
- Open Risks

Pending Work:

| Task | Done? | Evidence / Next step |
| --- | --- | --- |
| Rebuild manuscript after subject-performance edits | No | Run `cd writing && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=out main.tex` |
| Review whether S11 exclusion is justified | No | Inspect `05_models/subject_performance.parquet` and data-quality evidence before any filtered rerun |
```

### Why it's better

The improved version creates a durable note with exact next actions, evidence paths, and an explicit unfinished state instead of an informal recap.

---

## Example 2: Recording stopped background work accurately

### Before (without this skill)

```text
The run is done.
```

### After (with this skill applied)

```text
What Is Stopped:

- `scripts/monitor_runbook_live.py` was manually stopped after report completion.
- No `src.pipeline.runbook_runner` process is currently active.

Current Working State:

- Final runbook status: `Overall status: done`
- Report log: `.codex-tmp/live_logs/stage3_to_stage5_smoke_hashroot_report_retry2.log`
```

### Why it's better

It distinguishes manual process shutdown from actual pipeline completion and gives the next agent the exact evidence to verify both claims.

---

## Example 3: Capturing dirty-tree and artifact state for the next agent

### Before (without this skill)

```text
Some files changed. Please continue from here.
```

### After (with this skill applied)

```text
Current Working State:

- Dirty worktree includes `writing/result/result.tex`, `planning/Project_Execution_Flowchart.md`, and `handoff/20260331_subject_performance_handoff.md`.
- Rebuilt artifact: `writing/out/main.pdf`
- Compile log: `.codex-tmp/live_logs/subject_comparison_latex.log`
```

### Why it's better

The next agent can resume safely because the modified files, generated outputs, and validation log are explicit.
