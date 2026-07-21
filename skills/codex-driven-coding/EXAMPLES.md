# Examples: Codex-Driven Coding with Tiered Intelligence

---

## Example 1: Bounded handoff vs vague delegation

### Before (without this skill)

```text
"Add an algorithm registry and run the tests, then push it."
```

Result: the worker invents extra files, runs the whole suite (hitting a slow real-data test),
loops on the hang, and pushes to the mainline.

### After (with this skill applied)

```text
Handoff (mid tier):
- Add exactly two files:
  - src/pkg/registry.py : pure-data name -> metadata; no heavy imports at load.
  - tests/test_registry.py : asserts names registered, unique, docs exist, modules importable.
- Do NOT change any algorithm/runner/evaluation code.
- Run ONLY: pytest tests/test_registry.py -q
- Commit on branch feature/registry. Do NOT push. Do NOT merge to main.
```

### Why it's better

The scope, the single run command, and the don'ts are explicit, so the worker delivers exactly
the change and nothing else — and the manager can verify it in one diff and one command.

---

## Example 2: Matching the intelligence tier and escalating on failure

### Before (without this skill)

```text
Use the same default model for every task.
When it fails, run it again. And again.
```

### After (with this skill applied)

```text
1. Docstring + file-rename pass          -> LOW tier (mechanical).
2. Add feature with a clear contract     -> MID tier.
3. New signal-decomposition algorithm    -> HIGH tier (novel reasoning).
4. HIGH-tier attempt still fails a falsifier
   -> tighten the handoff (add the failing case) OR escalate reasoning effort;
      do NOT re-run the identical attempt a third time.
```

### Why it's better

Budget goes where the difficulty is, and a failure produces a *new* attempt (stronger tier or
tighter scope) instead of the same attempt repeated, which never adds information.

---

## Example 3: Provisioning the environment so the worker can't fabricate data

### Before (without this skill)

```text
Launch the worker in a fresh worktree.
The git-ignored data-paths config isn't there.
The worker generates synthetic data to "keep going" and reports results on ~4 fake records.
```

### After (with this skill applied)

```text
1. cp paths.yaml <new-worktree>/           # provide the git-ignored runtime config
2. Confirm the worker resolves the REAL dataset (spot-check counts).
3. Handoff states: "If real inputs cannot be resolved, STOP and report — never synthesize."
4. Treat a sudden collapse in event/record counts as a data-resolution red flag, not a result.
```

### Why it's better

The worker runs on real inputs, and if it ever can't, it halts loudly instead of silently
fabricating substitutes that produce meaningless numbers.
