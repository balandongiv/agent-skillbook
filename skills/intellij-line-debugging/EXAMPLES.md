# Examples: IntelliJ Line Debugging

---

## Example 1: Debugging a data pipeline stage from load to merge

### Before (without this skill)

```text
Run the full pipeline and add a few breakpoints somewhere in the code.
```

### After (with this skill applied)

```text
1. Narrow the scope to one real subject/session and one epoch size.
2. Set `jobs=1` and `force=True`.
3. Add `debug_feature_extraction_sequence.py` near the production stage.
4. Keep the debug helper sequence identical to production:
   - resolve paths
   - load EEG file
   - extract EEG features
   - load multimodal file
   - extract EAR/EOG features
   - merge the feature tables
5. Tell the user to debug that helper in IntelliJ.
6. Give the breakpoint order:
   - target resolution
   - first `read_*` call
   - first library feature call
   - merge boundary
   - final write
```

### Why it's better

The improved version reduces noise, removes parallelism, preserves the real execution order, and gives the user a repeatable IntelliJ entrypoint instead of a vague suggestion.

---

## Example 2: Using the existing code without a new helper

### Before (without this skill)

```text
Open the pipeline module and try stepping around until you understand it.
```

### After (with this skill applied)

```text
1. Keep the existing stage entrypoint.
2. Run it in IntelliJ with one file and `jobs=1`.
3. Use `--force` so the cached output does not short-circuit the run.
4. Set breakpoints in this order:
   - path resolution
   - file load
   - transform step
   - write step
5. Step Into the third-party call only at the exact library boundary that matters.
```

### Why it's better

The user gets a concrete path through the existing code without unnecessary refactoring.

---

## Example 3: Debugging through a third-party library

### Before (without this skill)

```text
The model library seems wrong. Can you inspect it?
```

### After (with this skill applied)

```text
1. Identify the exact call site where the project enters the third-party library.
2. Tell the user to set a breakpoint immediately before that call.
3. In IntelliJ, use Step Into at that line.
4. Remind the user to disable settings that skip library scripts if IntelliJ jumps over the call.
5. After returning from the library, inspect the transformed object and continue to the next project boundary.
```

### Why it's better

The improved version makes library debugging deliberate instead of leaving the user to fight the IDE.
