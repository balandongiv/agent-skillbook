---
name: strategy-impact-log
description: Record and track strategy proposals, code changes, performance metrics, issues encountered, and their cumulative effects on final results to maintain a durable audit trail of what was tried, what worked, and what didn't.
---

# Strategy Impact Log

Use this skill to maintain a durable, auditable record of strategies proposed, code changes made, performance observations, issues encountered, and how these decisions have affected final results. The goal is to make it easy for you or anyone reviewing the work later to understand not just what was tried, but why it was tried, whether it worked, and how it shaped the final solution.

Rather than treating strategy decisions as ephemeral conversation, record them as first-class artifacts that can be referenced, compared, and reasoned about later.

---

## Core principles

### 1. Every strategy proposal deserves a record

When you propose a new approach, alternative direction, or significant change in how to solve the problem, create an entry. Do not assume you will remember the reasoning later—document it now.

### 2. Link strategies to their concrete implementations

Do not just describe a strategy in isolation. Record:
- What specific code changes were made in service of this strategy
- Which files, functions, or modules were affected
- Commit hashes or line ranges that implement the strategy

### 3. Measure impact with real data

After a strategy is implemented, capture its effects:
- Performance metrics (latency, accuracy, throughput, memory usage, etc.)
- Specific test results or validation outputs
- Whether the strategy succeeded, failed, or had mixed results
- Exact numbers and sources, not vague assessments

### 4. Record issues and trade-offs honestly

Not every strategy works perfectly. Document:
- Problems encountered during implementation
- Performance trade-offs (e.g., faster but uses more memory)
- Edge cases or limitations discovered
- Why the issue matters or doesn't matter for your use case

### 5. Make strategy comparison easier

When multiple approaches exist, the log enables side-by-side comparison:
- What was the old approach vs. the new one?
- How do the metrics differ?
- Which issues does each approach create or solve?
- Why was one chosen over another?

### 6. Build a timeline of iterations

Document how strategies evolved over time:
- Initial idea → first attempt → problem discovered → refinement → final result
- Decisions that led to dead ends (valuable to know why a path wasn't taken)
- How learnings from one attempt informed the next

---

## Step-by-step process

### Step 1: Create the strategy entry

When you propose or identify a new strategy, create a markdown entry in the strategy log with:

```markdown
## Strategy: [Clear, concise strategy name]

**Date**: YYYY-MM-DD  
**Proposal**: [What is the core idea? Why consider this approach?]  
**Rationale**: [Why might this work? What problem does it solve?]  
**Status**: Proposed / In Progress / Completed / Abandoned  

### Implementation

**Files Changed**:
- `path/to/file.py` (lines X-Y): [brief change description]
- `path/to/module/`: [file or module pattern affected]

**Commits**:
- `abc1234`: [commit message]
- `def5678`: [commit message]

### Performance & Metrics

**Before**: [old metric values with sources]  
**After**: [new metric values with sources]  
**Change**: [+X%, improvement/regression description]

### Issues Encountered

- **Issue 1**: [description and impact]
- **Issue 2**: [description and impact]

### Outcome

[Did it succeed? Fail? Partially? Why?]

### Learnings

[What did we learn from this attempt? What would you do differently next time?]
```

### Step 2: Update as you implement

As you make code changes in service of the strategy:
- Record the specific files and line ranges
- Include commit hashes as you create them
- Note any deviations from the original proposal
- Update the status to "In Progress" once work begins

### Step 3: Capture metrics after execution

Once the strategy is implemented, run the relevant tests, evaluations, or observations:
- Extract before/after numbers
- Source the metrics (which test, which file, exact line where metric was computed)
- Record both successes and any degradations

### Step 4: Document issues and trade-offs

As you implement, issues will emerge. Record them:
- What went wrong or differently than expected?
- How does it affect the solution?
- Is it acceptable? Does it need fixing?
- What alternatives exist for handling the issue?

### Step 5: Conclude and reflect

Once the strategy is fully executed or abandoned:
- State whether it succeeded, failed, or had mixed results
- Summarize the key learnings
- Record what you would do differently next time
- Link to any follow-up strategies that were spawned by this attempt

### Step 6: Use the log for future decisions

When new strategies are proposed, consult the log:
- Have we tried something similar? What happened?
- What trade-offs did other approaches involve?
- Are there patterns in what works or doesn't work?
- Can we avoid repeating failed approaches?

---

## Rules

- Always create a strategy entry **before** implementing, not after.
- Always link strategies to concrete file changes and commits.
- Always measure impact with real metrics and cite sources.
- Always record issues and trade-offs honestly, not just successes.
- Always update the entry as the strategy evolves.
- Never claim a strategy "worked" without citing performance data.
- Never leave a strategy entry unfinished if the work is done.
- Never discard old strategy entries—they are evidence, not clutter.
- Always compare strategies using the same metrics so trade-offs are clear.
- Always note when a strategy was abandoned and why.

---

## Common patterns

### Pattern: A/B Comparison

When testing two approaches:

```markdown
## Strategy: Approach A vs Approach B

**Proposal**: Compare two implementations to determine which is better.

### Approach A: [Name]
- Implementation: [details]
- Metrics: [numbers]
- Trade-offs: [description]

### Approach B: [Name]
- Implementation: [details]
- Metrics: [numbers]
- Trade-offs: [description]

### Decision
[Which won? Why? What clinched it?]
```

### Pattern: Iterative Refinement

When a strategy needs multiple attempts:

```markdown
## Strategy: [Name] — Iteration 1/2/3

**Date**: YYYY-MM-DD  
**Previous Attempt**: [Link to earlier iteration]  
**Change From Last Attempt**: [What specifically did we try differently?]  
**Status**: Completed

### Results
[How did this iteration perform compared to the last?]

### Next Steps
[Do we need iteration 4? Or is this approach done?]
```

### Pattern: Dead End

When a strategy doesn't work out:

```markdown
## Strategy: [Name]

**Proposal**: [What we tried]  
**Status**: Abandoned  
**Reason**: [Why we stopped pursuing this]  

### What We Learned
[Even though it didn't work, what was valuable to discover?]

### Why This Matters
[Could it be useful in the future? What would need to change?]
```

---

## Condensed checklist

- Create an entry when a new strategy is proposed.
- Record the proposal, rationale, and expected benefits.
- Link to specific files and commits as you implement.
- Update status and metrics as work progresses.
- Document issues and trade-offs honestly.
- Measure impact with real data and cite sources.
- Conclude the entry with learnings and next steps.
- Use the log to inform future strategy decisions.
- Never delete old entries; treat them as historical evidence.
- Compare strategies using the same metrics.
