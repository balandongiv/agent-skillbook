# Codex-Driven Coding with Tiered Intelligence

## Overview

In a multi-agent setup, code changes are delegated to an autonomous coding agent (such as
OpenAI Codex) while a separate model acts as **manager and verifier**: it owns scope, writes
the handoff, provisions the environment, reviews the diff, and confirms the result. "Tiered
intelligence" means the manager does not use one model setting for everything — it **matches
the intelligence tier to the task** (fast/cheap tiers for boilerplate, high-reasoning tiers
for algorithm design and hard debugging) and **escalates** to a stronger tier when a lower
one fails. Almost every failure in this pattern comes from an *under-specified* worker
filling the gap with the wrong thing, so the whole skill is about tight scope, a provisioned
environment, and a defined failure mode.

## Core principles

1. **Separation of duties.** The coding agent writes code; the manager plans, provisions, and
   verifies. The manager does not hand-edit the worker's code (that erases the audit trail and
   defeats the delegation); the worker does not decide scope or merge to the mainline.
2. **Bounded written handoff.** Every delegation names the **exact files** to touch, the
   **exact run/test command**, the **done criteria**, and the explicit **don'ts**. A handoff
   that says "add a registry and run the tests" invites a full-suite run and scope drift; one
   that says "add exactly these two files, run only `pytest tests/test_registry.py -q`, do not
   push or merge" lands first try.
3. **Match the intelligence tier to the task.** Pick the model/reasoning-effort tier from the
   task's difficulty:
   - *Low tier* — mechanical/boilerplate: file moves, docstrings, wiring, format fixes.
   - *Mid tier* — standard feature work with clear contracts and tests.
   - *High tier* — novel algorithms, cross-module refactors, and non-obvious debugging.
   Do not pay for a high tier on boilerplate, and do not starve a hard task on a low tier.
4. **Escalate on failure, do not blind-retry.** If a tier fails or loops, escalate to a
   stronger tier (or tighten the handoff) rather than re-running the same tier repeatedly.
   Blind retries multiply stuck processes and burn budget without new information.
5. **Provision the environment first.** A worker in a fresh worktree or sandbox often lacks
   git-ignored runtime config (data paths, credentials-free config). Copy those in **before**
   launching. A worker that cannot find its real inputs must **stop and report**, never
   fabricate or synthesize data to keep going.
6. **Scope the run command.** Give the worker the minimal command that proves its change
   (one target test), not "run the tests." An unscoped run can hit a slow/expensive suite and
   hang, and its retries can spawn duplicates.
7. **Review every diff and keep provenance.** The manager reads the full diff before it lands,
   git-ignores agent logs/exhaust up front, and keeps the handoff so the change is traceable.

## Step-by-step process

1. **Classify the task** and pick the intelligence tier (low / mid / high) from its difficulty.
2. **Write the handoff** (a short markdown file is ideal): goal, exact files to add/change,
   the single run/test command, done criteria, and the don'ts (don't touch X, don't run the
   full suite, don't push, don't merge to mainline).
3. **Provision the worktree/sandbox**: copy git-ignored runtime config in; confirm the worker
   can resolve real inputs. If it cannot, stop — do not let it synthesize substitutes.
4. **Launch the coding agent** at the chosen tier, pointed at the handoff.
5. **Watch for the defined failure mode**: a sudden collapse in input/output counts (e.g.
   near-zero events, constant features) is a data-resolution red flag, not a result. On
   failure, **escalate the tier or tighten scope** — do not blind-retry the same tier.
6. **Verify**: read the full diff, run the scoped check yourself, confirm done criteria.
7. **Land it**: keep the handoff and logs (git-ignored), commit on the worker's branch; the
   manager, not the worker, decides consolidation into the mainline.

## Rules

- Always delegate with a bounded written handoff (files + run command + done criteria + don'ts).
- Always pick the intelligence tier from task difficulty; escalate on failure instead of
  blind-retrying the same tier.
- Always provision git-ignored runtime config before launching; a worker that can't find real
  inputs must stop, not fabricate.
- Always give the worker a scoped run command, never "run the full suite".
- Always review the full diff and keep the handoff/logs; git-ignore agent exhaust up front.
- Never let the manager hand-edit the worker's code, and never let the worker set scope or
  merge to the mainline.

## Common mistakes to avoid

- **Under-specified handoff.** "Add a registry and run the tests" → scope drift and a
  full-suite run. Enumerate files, the one command, and the don'ts.
- **Worker fabricates data.** With no real inputs, an agent may silently generate synthetic
  data and report meaningless results. Provision inputs; require stop-on-missing.
- **Unscoped test run.** "Run the tests" can trigger a slow/expensive suite that hangs; the
  worker's retries then spawn duplicate stuck processes. Scope to one target.
- **Blind retries.** Re-running the same failing tier multiplies stuck processes and cost.
  Escalate the tier or fix the handoff instead.
- **One tier for everything.** High tier on boilerplate wastes budget; low tier on a novel
  algorithm produces plausible-looking wrong code. Match the tier to the task.
- **Manager patches the worker's code.** It hides what the worker actually produced and breaks
  the audit trail. Send corrective feedback back to the worker instead.
- **Committing agent exhaust.** Log files staged into a commit. Git-ignore them before launch.
