# Examples: Agent Orchestration Manager

---

## Example 1: Delegate-vs-inline judgment

### Before (without this skill)

```text
Goal: rename a function and add a registry module.
Action: spawn a sub-agent for the rename, spawn another sub-agent for the registry,
        spawn a third to "review everything thoroughly."
Result: three cold-start agents re-derive context; the rename took longer to hand off
        than to do; the "thorough" reviewer adds noise.
```

### After (with this skill applied)

```text
1. Rename (small, local)        -> do INLINE; it's a one-file edit.
2. Registry module (bounded,    -> DELEGATE to a coding agent with a task spec:
   testable, self-contained)       files to add, the one test command, done-criteria, don'ts.
3. Review                       -> the MANAGER verifies (reads the diff, runs the test),
                                   not a spawned "thoroughness" agent.
```

### Why it's better

Delegation is used only where it pays (the bounded, testable module), the trivial edit is done
inline, and verification stays with the accountable manager instead of a redundant sub-agent.

---

## Example 2: Verifying instead of trusting the worker's report

### Before (without this skill)

```text
Worker: "Done — added the feature, all tests pass."
Manager: marks the task complete and moves on.
(Later: the worker ran a different/empty test, or fabricated data; nothing actually works.)
```

### After (with this skill applied)

```text
1. Read the full diff the worker produced.
2. Re-run the exact verify command yourself (not the worker's word for it).
3. Exercise the REAL flow end-to-end, not just the worker's unit test.
4. Spot-check inputs: did counts/artifacts stay realistic, or collapse (a fabrication red flag)?
5. Only then accept — or send it back with the specific failure.
```

### Why it's better

The manager is accountable for what lands, so acceptance is based on reproduced evidence, not a
self-report that can be wrong or fabricated.

---

## Example 3: Staying the manager (don't become the worker)

### Before (without this skill)

```text
The worker's code is 90% right but has two wrong lines.
Manager quietly edits those two lines and commits.
(Now the diff no longer reflects what the worker produced; attribution and the audit trail break,
 and the worker never learns the correction.)
```

### After (with this skill applied)

```text
1. Send the worker precise feedback: the two lines, why they're wrong, the expected behavior.
2. If the worker keeps failing, escalate (stronger tier) or tighten the task spec.
3. Let the worker produce the corrected change on its own branch.
4. Verify the new diff; then consolidate.
```

### Why it's better

The worker's output stays attributable and auditable, the correction is captured where it belongs,
and the manager keeps the consolidation gate instead of blurring the roles.
