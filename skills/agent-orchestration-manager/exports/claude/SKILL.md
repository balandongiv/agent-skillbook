---
name: agent-orchestration-manager
description: Act as the manager of a multi-agent workflow — route each piece of work to the right kind of agent (reasoning, coding, verifying), decide when to delegate versus do it inline, decompose goals into bounded independent tasks, verify every worker's output yourself, own the mainline and consolidation, and never silently do the worker's job.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Agent Orchestration Manager

## Overview

In a multi-agent workflow, one agent must act as **manager**: it owns the goal, splits it
into work, routes each piece to the right kind of agent, and is accountable for the result.
The failure modes are predictable — spawning sub-agents for trivial work, under-specifying
tasks, trusting a worker's report without verifying, quietly doing the worker's job when it
stumbles (which erases the audit trail), and letting workers touch the mainline. This skill is
the discipline that avoids them. It is the umbrella over the concrete delegation skills: use it
with `codex-driven-coding` (hand off a coding task), `worktree-parallel-agents` (isolate
parallel workers), and `chatgpt-ui-reasoning` (route thinking) — those are the instruments; this
is how you conduct.

## Core principles

1. **Route by kind of work.** Match each piece to the agent best suited to it: reasoning /
   ideation → a reasoning model or UI; code changes → a coding agent; **verification → the
   manager itself.** Don't use a coding agent to make product decisions, or a reasoning agent
   to run code. Keeping verification with the manager is what makes the manager accountable.
2. **Delegate only when it pays.** A sub-agent starts cold and re-derives context you already
   have — that is the expensive path. Do small or local tasks **inline**; delegate when the
   task is large, genuinely parallelizable, or needs an isolated context. "Do it thoroughly"
   or "from multiple angles" is not a reason to spawn — it is a reason to think, then act.
3. **Decompose into bounded, independent tasks.** Split the goal so each sub-task has a clear
   contract (inputs, outputs, done-criteria), can be verified on its own, and does not depend
   on another still-in-flight task. Bounded scope beats one big vague ask every time.
4. **Specify, don't hope.** Every delegation names the exact scope, the run/verify command, the
   done-criteria, and the explicit **don'ts**. Provision the worker's environment first (config,
   data access). A worker that cannot resolve its real inputs must **stop and report**, never
   fabricate substitutes to keep going.
5. **Verify every worker's output yourself — never trust the report.** Reproduce a claimed
   result, exercise the **real** flow (not just the worker's own tests), and read the full diff.
   "It says it passed" is not verification. The manager is accountable for what lands, so the
   manager confirms it.
6. **Stay the manager — don't become the worker.** When a worker stumbles, send corrective
   feedback or escalate (stronger tier, tighter spec); do **not** silently hand-edit its code or
   finish its task. Doing the worker's job hides what the worker produced, breaks attribution,
   and is a management failure dressed up as a rescue.
7. **Own the mainline and consolidation.** Workers commit on their own branches; the manager
   decides what merges and keeps provenance (who did what, and why). Consolidation is a
   deliberate manager step, not an automatic worker push.
8. **Run the loop and report truthfully.** plan → delegate → monitor → verify → consolidate →
   report. Monitor **real progress** (a rising count, a changing artifact), not mere process
   liveness. If a step was skipped or a result failed, say so plainly; never report a status you
   cannot verify.

## Step-by-step process

1. **Frame the goal** and its success criteria in one place.
2. **Decide inline vs delegate** for each piece — small/local → inline; large/parallel/isolated
   → delegate.
3. **Decompose** the delegated work into bounded, independent tasks, each with a contract.
4. **Route** each task to the right kind of agent and **provision its environment**.
5. **Write the task spec**: scope, the run/verify command, done-criteria, and the don'ts.
6. **Launch and monitor real progress**; on failure, escalate or tighten the spec — do not
   blind-retry the same thing.
7. **Verify each result independently** (reproduce / exercise the real flow) before accepting it.
8. **Consolidate** on the mainline with provenance, then **report outcomes truthfully**.

## Rules

- Always route work to the agent kind best suited (reason / code / verify); keep verification
  with the manager.
- Always prefer inline for small or local tasks; delegate only when it genuinely pays (size,
  parallelism, isolation).
- Always give a bounded task spec (scope + run/verify command + done-criteria + don'ts) and
  provision the environment first; a worker that can't find real inputs must stop, not fabricate.
- Always verify a worker's output by reproducing or exercising it; never accept a self-reported
  result as done.
- Never do the worker's job for it (no silent hand-edits); send feedback or escalate instead.
- Never let workers merge to the mainline; consolidation and provenance are the manager's.
- Never report a status you cannot verify; surface skips and failures plainly.

## Common mistakes to avoid

- **Spawn-happiness.** Launching sub-agents for trivial work that is cheaper done inline. Delegate
  for size/parallelism/isolation, not for the appearance of thoroughness.
- **Vague delegation.** "Make it better / be thorough" with no contract → scope drift and rework.
  Name the scope, the command, and the done-criteria.
- **Trusting the report.** Accepting "tests pass" without reproducing it. Verify independently.
- **Rescuing by doing.** Hand-editing the worker's output when it stumbles, erasing attribution.
  Feed back or escalate instead.
- **Workers on the mainline.** Losing the consolidation gate and provenance. Keep workers on their
  own branches.
- **Blind retries.** Re-running the same failing attempt instead of escalating or tightening the
  spec — it multiplies stuck work and adds no information.
- **Liveness mistaken for progress.** "The process is running" reported as "it's working." Track a
  real progress signal.

## Additional guidance

This skill is deliberately platform-neutral: "worker" can be an autonomous coding agent, a
reasoning UI session, a parallel worktree agent, or a human collaborator. Pair it with the
instrument skills — `codex-driven-coding`, `worktree-parallel-agents`, `chatgpt-ui-reasoning` —
which handle the mechanics of each delegation while this skill governs the role.
