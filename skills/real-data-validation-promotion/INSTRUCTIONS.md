# Real-Data Validation Promotion

Use this skill when a user cares about whether a pipeline, feature extractor, labeling stage, experiment loop, or reporting path truly works on the real dataset. The point is to validate the real behavior, not only the abstract logic. Synthetic data is still valuable for unit tests, but it does not prove that real folder layouts, annotations, caches, editable dependencies, or naming contracts behave correctly.

---

## Core principles

### 1. Use real data for behavioral claims

If the user wants to know whether a stage or full pipeline works, start from a real dataset scope whenever one is available and safe to use. Keep synthetic data for unit tests, isolated regression tests, and situations where no real sample can be run.

### 2. Start with the smallest representative real scope

Pick the smallest real scope that still exercises the true code path. Usually that means:

- one subject, session, or file
- one epoch size or one experiment
- one serial run with caches forced or refreshed when needed

Do not jump to the full sweep until the smallest real scope is clean.

### 3. Keep the smoke path and the promoted path functionally identical

The smoke run should use the same code path, dependency path, config family, artifact naming, and cache logic as the broader run. Narrow the scope, not the logic.

### 4. Treat editable local dependencies as part of the system under validation

If the runtime uses a package installed in editable mode from a local repo, that package is part of the code under test. If the failure originates there, debug and patch it there, then rerun the real-data smoke scope before promoting.

### 5. Validate outputs, not only process completion

A passing run should be justified by real outputs:

- expected artifact files
- sane row or count summaries
- readable EDA or catalog outputs when relevant
- correct naming or schema patterns
- absence of unexplained fatal mismatches

### 6. Separate summary EDA from heavy plot galleries when both are useful

If a stage benefits from both human-readable summary EDA and a large plot gallery, keep them separate. Summary artifacts should stay fast to open and easy to inspect; heavy galleries can exist alongside them without making the main validation artifact unwieldy.

### 7. Report residual risk honestly

A pipeline can be runnable and still not be publication-ready or fully cleared. Record what passed, what was skipped, what failed, and what remains scientifically or operationally unresolved.

---

## Step-by-step process

### Step 1: Confirm the real-data scope and the claim being tested

Identify:

- the canonical real dataset path
- the specific stage or end-to-end path being validated
- the smallest real unit that can prove the claim
- the pass criteria for promotion

### Step 2: Lock the runtime path

Record the exact entrypoint, key parameters, config files, and editable local dependencies used by the validation run. If a debug helper exists, make sure it enters the same production functions in the same order.

### Step 3: Run the smallest real-data smoke scope first

Prefer:

- one subject or session
- one experiment or model
- `jobs=1` when step-through inspection is helpful
- force rerun or cache refresh when old outputs would hide the current logic

### Step 4: Inspect the generated artifacts immediately

Do not stop at exit code. Check:

- expected files exist
- counts and shapes are plausible
- naming conventions match the docs
- EDA artifacts open and show sensible content
- any warnings or failed units are understood

### Step 5: Fix problems at the true source

If the issue is in:

- the main repo, patch the main repo
- the editable dependency, patch the dependency
- the docs, update the docs so the execution story stays truthful

Then rerun the same smallest real-data smoke scope.

### Step 6: Promote in stages

Only after the smoke scope is clean, promote to:

1. a small batch or cohort
2. a broader sweep
3. a full run

Keep the code path stable across promotions.

### Step 7: Summarize what passed and what still blocks confidence

Close with a concise but honest summary:

- what real-data scope passed
- what larger scope passed
- what artifacts justify that conclusion
- what failures or exclusions remain
- whether the result is operationally ready, debug-ready, or only partially validated

---

## Rules

- Always use the smallest available real-data scope before claiming a pipeline path works.
- Always keep the smoke path functionally aligned with the promoted path.
- Always record editable local dependencies that affect validation.
- Always inspect artifacts and counts, not only process exit.
- Always rerun the smallest real-data smoke after result-affecting fixes.
- Always separate lightweight summary artifacts from heavy plot galleries when both exist.
- Never use synthetic-only smoke to claim real-data pipeline readiness when the user asked for actual dataset validation.
- Never patch around an editable dependency bug downstream if the true fix belongs in the dependency.
- Never promote to a full sweep while the smoke scope still has unexplained failures.

---

## Common mistakes to avoid

- **Confusing unit-test confidence with real-data confidence**: A mocked test can pass while real annotations, file names, or caches still break.
- **Changing the logic between smoke and full run**: If the smoke helper takes a different path, it proves less than you think.
- **Ignoring local editable dependencies**: If the package lives in the repo and is installed editable, it is part of the system you are validating.
- **Packing all validation output into one giant artifact**: Heavy plots should not make the main summary impossible to inspect.
- **Calling the run "done" without residual-risk notes**: Validation should state what is still broken, missing, or only partially understood.

---

## Condensed checklist

- Define the real-data claim being tested.
- Choose the smallest representative real scope.
- Lock the real runtime path and editable dependencies.
- Run the real-data smoke first.
- Inspect artifacts, counts, naming, and EDA outputs.
- Fix problems at the true source.
- Rerun the smoke scope.
- Promote gradually to broader scopes.
- Report residual risk honestly.
