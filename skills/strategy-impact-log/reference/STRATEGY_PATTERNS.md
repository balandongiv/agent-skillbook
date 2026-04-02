# Strategy Patterns Guide

Quick reference for common strategy scenarios and how to handle them in your entry.

---

## Pattern 1: Simple Optimization

**What**: You optimize existing code for better performance without changing functionality.

**When to use**: Performance improvements, refactoring for speed/memory, removing bottlenecks.

**Entry Template**:

```markdown
## Strategy: [Optimization Name]

**Date**: YYYY-MM-DD
**Proposal**: [What optimization?] to improve [metric]
**Rationale**: [Current bottleneck]. Expected improvement: [X%]
**Status**: Completed

### Implementation
**Files Changed**:
- `path/to/file.py` (lines X-Y): Changed [what] from [old] to [new]

**Commits**:
- `hash1`: Optimization commit

### Performance & Metrics
**Before**: [Old metric] (measured via `test/bench_script.py`)
**After**: [New metric] (measured via `test/bench_script.py`)
**Change**: [+X% improvement]

### Issues Encountered
None. Simple refactor.

### Outcome
Success. Optimization achieved expected improvement.

### Learnings
[What surprised you? What would you do differently?]
```

**Example Metrics**:
- Latency: 45s → 12s (-73%)
- Memory: 512MB → 480MB (-6%)
- Throughput: 100/min → 250/min (+150%)

---

## Pattern 2: A/B Strategy Comparison

**What**: You evaluate two different approaches and pick the better one.

**When to use**: Choosing between algorithms, implementations, or architectures; trade-off analysis.

**Entry Template**:

```markdown
## Strategy: [What are you comparing?]

**Date**: YYYY-MM-DD
**Proposal**: Compare two approaches to [problem]: [Approach A] vs [Approach B]
**Rationale**: [Why compare? What's the trade-off?]
**Status**: Completed

### Approach A: [Name]

**Implementation**:
- Files: `path/to/a.py` (lines X-Y)
- Commits: `hash1`, `hash2`

**Metrics**:
- Metric 1: [value]
- Metric 2: [value]
- Trade-off: [pro] but [con]

### Approach B: [Name]

**Implementation**:
- Files: `path/to/b.py` (lines X-Y)
- Commits: `hash3`, `hash4`

**Metrics**:
- Metric 1: [value]
- Metric 2: [value]
- Trade-off: [pro] but [con]

### Decision: [Winner]

**Why**: [Which metrics mattered most? Why did winner win?]

### Issues Encountered
- **Issue A**: [from approach A]
- **Issue B**: [from approach B]

### Outcome
Success. Approach [X] selected based on [metric/rationale].

### Learnings
- Approach [A] excels at [metric], [B] excels at [metric]
- Trade-off was between [X] and [Y]
- [Winner] is better for [use case]
```

**Metrics Must Be Identical Across Both**:
```
✅ Both approaches measured on same dataset
✅ Both approaches use same test suite
✅ Metrics are F1, latency, memory (same for both)
❌ A measures accuracy, B measures precision (different metrics)
❌ A on 100 samples, B on 1000 samples (different scope)
```

---

## Pattern 3: Iterative Refinement

**What**: First attempt → discover issue → iterate → refine → success.

**When to use**: When strategy needs multiple attempts, or when learnings from one attempt inform the next.

**Entry Structure**:

```markdown
## Strategy: [Name] — Iteration 1

**Date**: 2026-04-01
**Proposal**: [Original idea]
**Status**: Completed → Proceed to Iteration 2

### Implementation
[What you tried]

### Metrics
[Initial results]

### Issues Encountered
- **Issue X**: [Problem discovered]
  - *Resolution*: Not fixed; proceed to iteration 2
  - *Status*: Deferred to next iteration

### Outcome
Partial. [What worked, what didn't.]

---

## Strategy: [Name] — Iteration 2

**Date**: 2026-04-02
**Proposal**: [Based on Iteration 1 learnings, try: ...]
**Previous Attempt**: See Iteration 1 above
**Change From Last Attempt**: [Specifically what changed?]
**Status**: Completed

### Implementation
[What you changed]

### Metrics
- Iteration 1: [metric] = X
- Iteration 2: [metric] = Y
- Change: [Y vs X]

### Issues Encountered
[New issues? Better? Worse?]

### Outcome
Success. Iteration 2 resolved the issue from iteration 1.

### Learnings
[Did multiple iterations help? Why? What pattern worked?]
```

**Key for Iterations**:
- Link each iteration to the previous
- Explicitly state what changed ("Changed from X to Y because...")
- Show metric progression across iterations
- Explain why each refinement was necessary

---

## Pattern 4: Abandoned Strategy

**What**: You tried something, discovered it doesn't work or isn't viable, and stopped.

**When to use**: When a strategy fails, costs too much, or gets deprioritized.

**Entry Template**:

```markdown
## Strategy: [Name]

**Date**: YYYY-MM-DD
**Proposal**: [What you tried]
**Rationale**: [Why it seemed promising]
**Status**: Abandoned

### Implementation
[What you actually built before realizing it won't work]

### Performance & Metrics
**Attempted**: [What you measured]
**Result**: [Why it failed]

**Data Source**: [Script or test that showed failure]

### Issues Encountered
- **Critical Issue**: [Why this doesn't work]
  - [Explanation of the blocker]
  - *Status*: Unfixable / Too costly to fix / Deprioritized

### Outcome
Abandoned. [Clear explanation of why, not blame or guilt.]

Examples:
- "GPU approach was abandoned because transfer overhead (4-5ms) outweighed computation benefit"
- "Custom binary format abandoned in favor of pickle + gzip, which achieved same size reduction with 90% less code"
- "Multiprocessing approach abandoned due to IPC overhead on lightweight operations"

### What We Learned
[Even though it didn't work, what was valuable?]

Examples:
- "Learned that our bottleneck is I/O, not computation. GPU won't help unless we rearchitect the data pipeline"
- "Confirmed that compression is better investment than custom format for our access patterns"
- "Discovered that lightweight operations have minimum latency floor; parallelization only viable for >100ms operations"

### Why This Matters
[Under what conditions might this become viable in the future?]

Examples:
- "If we move to truly massive batches (10k+ epochs), GPU might become viable"
- "If codebase grows significantly, custom format might be worth revisiting for maintainability"
- "If workload becomes CPU-bound instead of I/O-bound, parallelization could help"
```

**Tone Guidelines**:
- ✅ Neutral and factual: "GPU transfer overhead dominated, making overall latency worse"
- ❌ Defensive: "We tried GPU but it was a disaster" 
- ❌ Dismissive: "GPU is stupid for this use case"
- ✅ Learning-oriented: "Revealed that I/O is our true bottleneck, not computation"

---

## Pattern 5: Comparison Table

**What**: Compare multiple strategies side-by-side with all metrics visible at once.

**When to use**: When you have 3+ approaches or need clear side-by-side comparison.

**Entry Template**:

```markdown
## Strategy: [Comparison Name]

**Date**: YYYY-MM-DD
**Proposal**: Compare [count] approaches to [problem]
**Status**: Completed

### Approaches

| Aspect | Approach A | Approach B | Approach C |
|--------|-----------|-----------|-----------|
| **Description** | [Brief] | [Brief] | [Brief] |
| **Complexity** | Low | Medium | High |
| **Latency** | 45s | 12s ⭐ | 50s |
| **Memory** | 256MB | 576MB | 128MB ⭐ |
| **Accuracy** | 92% | 94% ⭐ | 91% |
| **Implementation** | Easy | Medium | Hard |
| **Maintainability** | High ⭐ | Low | Medium |
| **Trade-offs** | Slow but simple | Balanced | Complex but efficient |

### Decision: Approach B

**Why**: B balances latency and accuracy well. While C uses less memory, the implementation complexity isn't justified for marginal gains.

### Issues Encountered
[Any issues with chosen approach]

### Outcome
Success. B selected and deployed.

### Learnings
[Insights about trade-offs and when each approach is best]
```

---

## Pattern 6: Feature Implementation

**What**: Add new functionality (not just optimize existing code).

**When to use**: New features, new algorithms, new modules.

**Entry Template**:

```markdown
## Strategy: [Feature Name]

**Date**: YYYY-MM-DD
**Proposal**: Implement [feature] to enable [capability/benefit]
**Rationale**: Users need [capability]. Without it, [limitation]. With it, [enablement]
**Status**: Completed

### Implementation
**Files Changed**:
- `new_module/feature.py` (new file): [Description]
- `existing_file.py` (lines X-Y): Integration hooks

**Commits**:
- `hash1`: feat: Implement [feature]
- `hash2`: test: Add [feature] test suite
- `hash3`: docs: Document [feature]

### Validation
**Tested on**: [Dataset/scenario]
**Test Results**:
- ✅ Functional correctness: [verification]
- ✅ Performance: [metrics]
- ✅ Edge cases: [coverage]
- ✅ Integration: [system works with new feature]

### Issues Encountered
[Any bugs/limitations found during implementation?]

### Outcome
Success. Feature implemented and validated. Ready for production/deployment.

### Learnings
[What surprised you? What was harder/easier than expected?]
```

---

## Pattern 7: Bug Fix with Root Cause Analysis

**What**: Fix a bug by understanding and addressing the root cause.

**When to use**: When you're not just patching a symptom, but investigating and fixing the underlying cause.

**Entry Template**:

```markdown
## Strategy: [Bug] Root Cause Fix

**Date**: YYYY-MM-DD
**Proposal**: Fix [bug description]. Expected cause: [hypothesis]
**Rationale**: [Why this bug matters; impact on users/tests]
**Status**: Completed

### Investigation
**Symptoms**: [What went wrong? Which tests failed?]
**Root Cause**: [What was actually wrong, not just the symptom?]
**Why It Happened**: [Explanation of the underlying issue]

### Implementation
**Files Changed**:
- `problematic_file.py` (lines X-Y): Changed [what] from [wrong] to [correct]

**Commits**:
- `hash1`: fix: Address root cause of [bug]

### Validation
**Tests**:
- ✅ Previously failing test now passes: [test name]
- ✅ No regression on existing tests
- ✅ Edge case validation: [case]

### Issues Encountered
None. Clean fix.

### Outcome
Success. Root cause identified and fixed. Bug resolved.

### Learnings
- Root cause was [X], not [initial hypothesis]
- This reveals [pattern/design issue/testing gap]
- Future prevention: [How to prevent this type of bug]
```

---

## Pattern 8: Trade-off Decision

**What**: Choose between two approaches knowing each has pros/cons; document the trade-off.

**When to use**: When neither approach is clearly superior; decision depends on priorities.

**Entry Template**:

```markdown
## Strategy: [Choice Name] - Trade-off Decision

**Date**: YYYY-MM-DD
**Proposal**: Choose between [Option A] and [Option B] for [context]
**Rationale**: Both viable; trade-off is between [X] and [Y]
**Status**: Completed

### Option A: [Name]
- **Pros**: [List benefits]
- **Cons**: [List drawbacks]
- **Metrics**: [Key numbers]
- **Best for**: [When to use this]

### Option B: [Name]
- **Pros**: [List benefits]
- **Cons**: [List drawbacks]
- **Metrics**: [Key numbers]
- **Best for**: [When to use this]

### Decision: [Option X]

**Reasoning**: We chose [X] because [primary factor] was more important than [secondary factor] for our use case.

**Trade-off Accepted**: We're accepting [con from X] in exchange for [pro from X].

**Future Reconsideration**: If [condition changes], we might revisit this decision.

### Outcome
Decision made and implemented. Team aligned on trade-off.

### Learnings
- Trade-off between [X] and [Y] is fundamental; can't have both
- Current priorities favor [X]; could change in future
- [Similar decisions elsewhere] might want consistency in approach
```

---

## Quick Pattern Selector

**When you see this situation... use this pattern:**

| Situation | Pattern | Status |
|-----------|---------|--------|
| Code is slow, you make it faster | Simple Optimization | Completed |
| Testing two algorithms | A/B Comparison | Completed |
| First attempt doesn't work, refine | Iterative Refinement | Completed |
| Tried something, doesn't work, stop | Abandoned Strategy | Abandoned |
| Comparing 3+ approaches | Comparison Table | Completed |
| Adding new feature | Feature Implementation | Completed |
| Bug happened, fix root cause | Bug Fix with RCA | Completed |
| Neither option is clearly better | Trade-off Decision | Completed |
| Performance gets worse | Abandoned Strategy | Abandoned |
| Approach is viable but deprioritized | Abandoned Strategy | Abandoned |
| Refining an approach over iterations | Iterative Refinement | Completed |

---

## Cross-Pattern Tips

### Metrics Consistency
- Use **identical metrics** when comparing approaches
- If comparing A and B, both should measure: latency, memory, accuracy
- Don't measure A by throughput and B by latency

### Documentation Currency
- Update the entry **as work progresses**, not in retrospect
- Add commits as they're made, not all at the end
- Record issues when discovered, not after they're fixed
- This captures details that might be forgotten

### Future-Proofing
- Every entry should answer: "When would we revisit this decision?"
- Examples: "If data grows 10x", "If requirements change", "If team capacity increases"
- This helps future developers know when to reconsider

### Specificity Checklist
- ✅ Exact numbers with units (not "much faster")
- ✅ File paths and line ranges (not "modified code")
- ✅ Commit hashes (not "committed it")
- ✅ Test file sources (not "validated it")
- ✅ Clear outcomes (not "worked well")

---

**Pattern Guide Version**: 1.0.0  
**Last Updated**: 2026-04-02
