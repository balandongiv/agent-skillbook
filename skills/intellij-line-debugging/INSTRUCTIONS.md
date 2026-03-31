# IntelliJ Line Debugging

Use this skill when the user wants to understand execution step by step inside IntelliJ IDEA or PyCharm. The goal is not only to "make debugging possible," but to make the path easy to follow from a real input through the real production call order, with minimal branching, minimal hidden cache skips, clear breakpoint placement, and deliberate stepping into repo-local editable dependencies when the library code is part of the question.

---

## Core principles

### 1. Debug the real path, not a toy rewrite

Prefer the smallest real input that still exercises the real behavior. If the bug or question depends on real file layout, sampling, annotations, feature selection, model configuration, or merge logic, use a small real scope instead of replacing the workflow with synthetic stand-ins.

### 2. Prefer a thin serial debug path

If the production entrypoint is too parallel, too broad, or too cache-heavy, create a thin debug harness near the production module. The harness should call the same underlying functions in the same order, but with:

- one subject, session, file, or experiment
- one parameter set
- `jobs=1` or equivalent serial execution
- explicit `force` or cache-bypass settings when needed

Do not create alternate business logic just for debugging.

### 3. Freeze scope aggressively

Reduce the debug scope until a human can keep the whole run in working memory. That usually means:

- one stage
- one subject or session
- one epoch size or one model
- one configuration branch

### 4. Remove invisible skips

Caching, background workers, and discovery across many files make step-through debugging harder. When the user wants line-by-line debugging, prefer:

- `jobs=1`
- one explicit target record
- `--force` or equivalent when cache reuse would skip the code path
- optional `stop_after` or stage gates to stop before later steps

### 5. Give the breakpoint order before the user starts

Do not just say "debug this file." Tell the user the exact order of breakpoints or "step into" points, starting from the first file read and continuing through the important transforms, library calls, merges, and writes.

### 6. Make library stepping intentional

If the user wants to see what happens inside third-party code, point them to the exact call sites where they should use Step Into. Also tell them what IntelliJ setting may block library stepping.

### 7. Step into editable local dependencies intentionally

If the runtime uses a local editable package, treat that package as part of the debuggable codebase. Tell the user:

- which wrapper or import boundary enters the dependency
- which function call is the best Step Into point
- which local repo path contains the dependency code

If the bug lives in the editable dependency, prefer fixing it at the dependency source instead of piling on project-local workarounds.

### 8. Leave behind a reusable debug entrypoint

If you add a helper such as `debug_<stage>_sequence.py`, keep it:

- in `tutorials/` or another clearly human-facing learning/debug folder when the helper is meant to be opened and debugged directly in the IDE
- close to the production stage in naming and documentation, even if the file itself lives in `tutorials/`
- easy to right-click and debug
- configurable through a small settings block or CLI args
- faithful to the production call order

---

## Step-by-step process

### Step 1: Define the smallest real debug scope

Pick one real unit of execution:

- one file
- one subject/session
- one segment
- one experiment/model pair

Use the smallest representative scope that still reproduces the behavior or teaches the execution path.

### Step 2: Choose the simplest debug strategy

Use one of these, in order:

1. Existing production entrypoint with a narrow scope and `jobs=1`
2. Existing module plus precise breakpoint instructions
3. A thin serial debug helper that calls the same production functions in the same order

Only refactor when the existing path is too hard to follow directly.

### Step 3: Mirror the production call order exactly

If you add a debug helper, make its sequence match production:

1. resolve config and paths
2. resolve the target input record
3. load the input file(s)
4. call the real processing functions in the same order
5. cross the editable-dependency boundary at the same point as production when library stepping matters
6. stop before later stages when requested

The helper should explain the production code, not replace it.

### Step 4: Expose the key debug controls

A good debug helper usually exposes or hardcodes a small settings block with:

- target identifiers such as subject, session, or file name
- the key parameter set such as epoch size
- `force` or cache-bypass behavior
- an optional `stop_after` gate such as `resolve`, `load`, `extract`, `merge`, or `write`

### Step 5: Prepare the IntelliJ run configuration

Make sure the user can run the path directly in IntelliJ IDEA or PyCharm with:

- the correct interpreter
- the correct working directory
- any required environment variables
- the intended script path or module path

If library stepping matters, remind the user to disable settings that skip library scripts.

### Step 6: Give an explicit breakpoint plan

Breakpoints should usually follow this order:

1. input and path resolution
2. first file load
3. first major transform
4. editable local dependency or third-party library call boundary
5. merge or join boundary
6. final write boundary

Also call out which breakpoints are best for "inspect state" versus "step into library code."

### Step 7: Inspect the right state at each stop

At each breakpoint, tell the user what to inspect:

- resolved paths
- shape, columns, or channel list
- epoch indices or join keys
- config values
- selected feature names
- local dependency path and function name when library stepping is relevant
- alignment or mismatch summary
- output path and row count

### Step 8: Keep the helper after the immediate fix

If the helper teaches the execution path or is likely to help again, keep it in the repo and document when to use it. If it is truly one-off, remove it before finishing.

---

## Rules

- Prefer the smallest real input over synthetic stand-ins when behavior depends on real artifacts.
- Prefer `jobs=1` when the user wants line-by-line debugging.
- Prefer `--force` or equivalent when cache reuse would skip important code.
- Prefer a thin serial debug harness over a heavy refactor.
- Put reusable human-facing debug helpers in `tutorials/` or an equally obvious IDE-facing folder.
- Keep the helper tied clearly to the production stage it explains through naming and docs.
- Keep the helper faithful to the production call order.
- Provide the exact breakpoint order, not just the file name.
- Point to exact library call sites when stepping into third-party code matters.
- Point to the actual repo-local path when the dependency is installed in editable mode.
- Preserve production behavior if refactoring for debug readability.

---

## Common mistakes to avoid

- **Debugging the full pipeline first**: A full multi-stage run hides the flow. Reduce to one unit.
- **Letting caches short-circuit the path**: If a file already exists, the debugger may never enter the interesting code.
- **Refactoring into a fake path**: A debug helper that uses different logic teaches the wrong thing.
- **Keeping parallel workers enabled**: Multiple workers make breakpoints noisy and hard to reason about.
- **Starting with vague instructions**: "Set some breakpoints" is not enough. Give the breakpoint order.
- **Skipping library settings**: IntelliJ may skip library stepping unless the debugger settings allow it.
- **Hiding the helper in a deep package**: If the helper is meant for humans to open and debug directly, put it somewhere obvious like `tutorials/`.
- **Treating editable dependencies like remote black boxes**: If the code is in the repo and installed editable, show where to step into it.
- **Using a helper with too many knobs**: A debug helper should reduce choices, not recreate the full CLI surface.

---

## Condensed checklist

- Narrow the run to one real unit of work.
- Use the real production functions in serial order.
- Set `jobs=1`.
- Force rerun or bypass cache if needed.
- Add a thin debug helper only if the production entrypoint is too broad.
- Put reusable IDE helpers where a human will look first.
- Give the user the exact breakpoint order.
- Point to the local editable dependency boundary when relevant.
- Point out the best step-into boundaries for third-party libraries.
- Tell the user what state to inspect at each stop.
- Keep the helper reusable if it adds long-term value.
