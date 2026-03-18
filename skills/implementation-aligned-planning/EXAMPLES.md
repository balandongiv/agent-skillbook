# Examples: Implementation-Aligned Planning

---

## Example 1: Rewriting a vague stage note into a navigation document

### Before (without this skill)

```text
Phase 2 extracts features from EEG and eye signals, then combines them for later analysis.
```

### After (with this skill applied)

```text
1. Define the stage contract:
   - what it reads
   - what it writes
   - what it does not do
2. Map the real modules and functions.
3. Write the actual execution order with function calls.
4. Document required existence checks and common failures.
5. Add minimal pseudocode and a debugger-oriented file order.
```

### Why it's better

The improved version helps a reader navigate the codebase instead of only repeating a broad idea.

---

## Example 2: Updating docs when code outran the plan

### Before (without this skill)

```text
The plan says the stage writes CSV files into results/.
The code now writes Parquet files into outputs/features/ and experimentation/.
Leave the plan as-is for now.
```

### After (with this skill applied)

```text
1. Verify the real outputs in code and on disk.
2. Update the stage doc to the actual file names and paths.
3. Update folder_structure.md and the execution flowchart as well.
4. If the old path mattered historically, mention it as legacy behavior rather than current behavior.
```

### Why it's better

It preserves truthfulness and stops future readers from navigating to the wrong paths.

---

## Example 3: Handling a half-baked plan with real ambiguity

### Before (without this skill)

```text
We might cluster labels somehow and maybe use metadata filters later.
```

### After (with this skill applied)

```text
1. Inspect the current labeling implementation.
2. Document the implemented strategy exactly.
3. Mark metadata filtering behavior as:
   - implemented
   - skipped gracefully when metadata is missing
   - unresolved if truly not discoverable
4. Keep only the unresolved piece open; make the rest explicit.
```

### Why it's better

The document becomes actionable without pretending every unknown is solved.
