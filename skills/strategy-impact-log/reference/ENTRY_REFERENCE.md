# Strategy Entry Reference Guide

This is a quick reference for agents creating or updating strategy entries. Use this when you need to remember the format, what to include, or how to fill out each section.

---

## Entry Template

Copy and paste this template when creating a new strategy entry:

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

**Data Source**: [Which test/file/script produced these numbers?]

### Issues Encountered

- **Issue 1**: [description and impact]
  - *Resolution*: [How was it resolved or why accepted as trade-off?]
  - *Status*: Resolved / Ongoing / Accepted Trade-off

- **Issue 2**: [description and impact]
  - *Resolution*: [How was it resolved?]
  - *Status*: Resolved / Ongoing / Accepted Trade-off

### Outcome

[Did it succeed? Fail? Partially? Why? Reference the metrics.]

### Learnings

[What did we learn from this attempt? What would you do differently next time? How does this apply to future work?]
```

---

## Field-by-Field Guide

### Header: `## Strategy: [Name]`
- **What**: The name of the strategy or approach being documented
- **How**: Use clear, descriptive language that identifies the core idea
- **Examples**:
  - ✅ `## Strategy: Cache Blink Detection Results`
  - ✅ `## Strategy: Epoch-Aware Pipeline with Bad Epoch Exclusion`
  - ✅ `## Strategy: GPU Acceleration for Batch Processing`
  - ❌ `## Strategy: Optimization` (too vague)
  - ❌ `## Strategy: Fix Performance` (not descriptive)

### **Date**: YYYY-MM-DD
- **What**: When the strategy was proposed or created
- **How**: Use ISO format (2026-04-02)
- **Why**: Creates a timeline of decisions and enables tracking evolution
- **Example**: `**Date**: 2026-04-02`

### **Proposal**: [What and Why]
- **What**: The core idea—what is the strategy?
- **How**: 1-3 sentences explaining what you're proposing to try
- **Examples**:
  - "Implement in-memory LRU cache for blink detection results"
  - "Use adaptive per-subject threshold instead of global fixed threshold"
  - "Parallelize epoch processing with GPU acceleration"
- **What to avoid**:
  - ❌ Don't describe implementation details yet
  - ❌ Don't assume the reader knows the context

### **Rationale**: [Why]
- **What**: Why should we try this? What problem does it solve?
- **How**: Explain expected benefits and motivation
- **Examples**:
  - "Iterative development reprocesses the same epochs repeatedly. Caching could reduce computation time by 70%+"
  - "Signal quality varies across subjects. Adaptive thresholds could improve F1 by matching local signal characteristics"
  - "Current processing is CPU-bound on large batches. GPU could enable 10x speedup"
- **What to avoid**:
  - ❌ Don't claim it will work (that's for testing)
  - ❌ Don't oversell ("this will revolutionize everything")

### **Status**: Proposed / In Progress / Completed / Abandoned
- **What**: Current state of the strategy
- **How**: Use one of the four states
- **Timeline**:
  1. Start: **Status**: Proposed
  2. During work: **Status**: In Progress
  3. After work: **Status**: Completed (if it worked) or Abandoned (if you stopped)
- **Examples**:
  - Proposed: Initial idea, no implementation yet
  - In Progress: Currently implementing or testing
  - Completed: Fully tested, documented, ready to use
  - Abandoned: You tried it but stopped pursuing it

### **Files Changed**: [Specific paths and line numbers]
- **What**: Which files did the strategy affect?
- **How**: Include file path and line range if applicable
- **Format**:
  ```
  **Files Changed**:
  - `pyblinker/blink_detector.py` (lines 45-90): Added _CacheManager class
  - `tests/test_cache.py` (lines 1-50): New cache validation tests
  - `pyblinker/__init__.py`: Added import for cache module
  ```
- **What to include**:
  - ✅ Absolute or relative paths
  - ✅ Line ranges if modifying specific sections
  - ✅ Brief description of what changed
- **What to avoid**:
  - ❌ Don't list every file touched (just the significant ones)
  - ❌ Don't be vague ("multiple files modified")

### **Commits**: [Git hashes and messages]
- **What**: Which commits implemented this strategy?
- **How**: Include commit hash and brief message
- **Format**:
  ```
  **Commits**:
  - `a7f3e8c`: feat: Add LRU cache for blink detection results
  - `b2d1f4e`: test: Add cache hit/miss test cases
  - `c5e2a9f`: docs: Document cache behavior
  ```
- **How to find**:
  ```bash
  git log --oneline | grep cache  # Find commits related to your strategy
  ```
- **What to include**:
  - ✅ Full commit hash (7+ characters) or full SHA
  - ✅ Commit message
  - ✅ All commits that implement the strategy
- **What to avoid**:
  - ❌ Don't list unrelated commits
  - ❌ Don't use abbreviated hashes (use at least 7 characters)

### **Before**: [Old metric values with sources]
- **What**: What was the baseline before your changes?
- **How**: Include specific, quantitative measurements
- **Format**:
  ```
  **Before**: 1000 epochs processed in 45.2 seconds (no cache)
  ```
- **Be specific**:
  - ✅ "45.2 seconds" (specific number with unit)
  - ✅ "F1 score: 0.79" (exact value)
  - ✅ "Memory: 256 MB" (quantifiable)
  - ❌ "slow" (vague)
  - ❌ "not great performance" (subjective)
- **Include context**:
  - How many items? How many runs?
  - What hardware/environment?
  - Any special conditions?

### **After**: [New metric values with sources]
- **What**: What are the metrics after your changes?
- **How**: Use the same metrics as "Before" for fair comparison
- **Format**:
  ```
  **After**: 1000 epochs processed in 12.3 seconds (with 90% cache hits)
  ```
- **Important**: **Use identical metrics as "Before"**
  - ❌ Don't use different measurements ("time" before, "throughput" after)
  - ✅ Use consistent metrics to enable comparison

### **Change**: [Quantitative improvement/regression]
- **What**: How much did the metric change?
- **How**: Calculate the percentage change and describe direction
- **Format**:
  ```
  **Change**: -72.8% latency (improvement)
  **Change**: +1.2% memory overhead (acceptable trade-off)
  **Change**: -5% accuracy (regression, concern)
  ```
- **Calculate**:
  ```
  percentage_change = ((after - before) / before) * 100
  ```
- **Direction**:
  - Minus sign = improvement for latency/time/errors
  - Plus sign = improvement for accuracy/throughput/success
  - Be explicit about direction

### **Data Source**: [Which test, file, script produced the numbers?]
- **What**: How can someone verify these metrics?
- **How**: Cite the exact source (test file, script, output location)
- **Format**:
  ```
  **Data Source**: `scripts/benchmark_cache.py` on `sample_data/seed_exp01_pyblinker_results_1.pkl`
  **Data Source**: `tests/test_cache.py::test_cache_performance` (line 45)
  **Data Source**: Console output from `python -m pytest tests/test_cache.py -v`
  ```
- **Why this matters**:
  - Someone should be able to reproduce the measurement
  - They should be able to find the code that generated the metric
  - They should be able to verify the number themselves
- **Examples**:
  - ✅ "scripts/benchmark.py on sample_data/dev_epo.fif"
  - ✅ "test/test_performance.py::test_throughput (lines 80-120)"
  - ✅ "Console output, validation_results.json, key 'f1_score'"
  - ❌ "Some benchmark I ran" (can't be verified)
  - ❌ "Local testing" (too vague)

### **Issue 1/2/3**: [Description]
- **What**: Problems or trade-offs discovered during implementation
- **How**: Describe each issue clearly
- **Format**:
  ```
  - **Cache key normalization**: Float precision variations prevented cache hits
  - **Memory growth**: Cache unbounded on long sessions
  ```
- **Include for each issue**:
  - What went wrong or differently than expected?
  - How does it affect the solution?
  - Is it a blocker or acceptable?

### **Resolution**: [How was it fixed?]
- **What**: How did you address the issue?
- **Format**:
  ```
  - *Resolution*: Normalize all float parameters to 3 decimal places
  - *Resolution*: Implemented LRU eviction (keep 1000 entries)
  ```
- **Include**:
  - ✅ Technical solution or decision made
  - ✅ Why it's acceptable or necessary
- **Avoid**:
  - ❌ "Fixed it" (vague)
  - ❌ "Workaround" (explain the workaround)

### **Status**: [Resolved / Ongoing / Accepted Trade-off]
- **What**: Current state of the issue
- **Options**:
  - **Resolved**: Issue fixed, no longer a concern
  - **Ongoing**: Still being worked on
  - **Accepted Trade-off**: Accepted as a limitation; not fixing because trade-off is worth it

### **Outcome**: [Success/Failure/Mixed result?]
- **What**: Overall assessment of whether the strategy worked
- **How**: State clearly and support with metrics
- **Format**:
  ```
  **Outcome**: Success. Caching worked as intended. Repeated analyses are 72.8% faster.
  **Outcome**: Failed. GPU transfer overhead outweighed computation benefits (regression of 107%).
  **Outcome**: Mixed. Adaptive threshold improved F1 but increased implementation complexity.
  ```
- **Essential**: Reference the metrics from the Performance & Metrics section
- **Never**:
  - ❌ Claim success without data ("it worked great")
  - ❌ Hide negative results ("mostly works fine")
  - ❌ Make vague assessments ("seems better")

### **Learnings**: [What did we learn?]
- **What**: Key insights and implications for future work
- **How**: Reflect on what the strategy taught you
- **Examples**:
  ```
  Cache key design is critical. Too narrow keys miss opportunities, too broad keys risk correctness.
  Signal quality varies significantly across subjects; adaptive approaches capture that variation.
  Transfer overhead dominated on lightweight operations. GPU only viable for heavy computation batches.
  ```
- **Include**:
  - ✅ What succeeded or failed and why
  - ✅ Patterns or insights discovered
  - ✅ What you'd do differently next time
  - ✅ How this applies to future work
- **Avoid**:
  - ❌ Generic conclusions ("always test before deploying")
  - ❌ Obvious statements ("code changes affected results")
  - ❌ No reflection at all

---

## Common Metric Patterns

### Performance Metrics
```
Latency (time):
  Before: 45.2 seconds
  After: 12.3 seconds
  Change: -72.8% (improvement)

Throughput:
  Before: 100 epochs/minute
  After: 250 epochs/minute
  Change: +150% (improvement)

Memory Usage:
  Before: 512 MB
  After: 576 MB
  Change: +12.5% (acceptable trade-off)
```

### Quality Metrics
```
Accuracy:
  Before: 92%
  After: 94%
  Change: +2 percentage points

F1 Score:
  Before: 0.79
  After: 0.83
  Change: +5.1% (improvement)

False Positive Rate:
  Before: 8%
  After: 5%
  Change: -3 percentage points (improvement)
```

### Coverage Metrics
```
Data Coverage:
  Before: 1000/1000 epochs (100%)
  After: 950/1000 epochs (95%, bad epochs excluded)
  Change: -5% coverage but +8% signal quality

Test Coverage:
  Before: 82%
  After: 95%
  Change: +13 percentage points
```

---

## Strategy Status Checklist

### When Status = **Proposed**
- [ ] Clear proposal statement
- [ ] Rationale explained
- [ ] No implementation yet

### When Status = **In Progress**
- [ ] Implementation section started
- [ ] File changes documented
- [ ] Commits recorded as made
- [ ] Issues being encountered and documented
- [ ] On track or blocked? Note anything blocking progress

### When Status = **Completed**
- [ ] All files changed documented
- [ ] All commits recorded
- [ ] Before/after metrics captured
- [ ] Issues resolved or documented as trade-offs
- [ ] Clear outcome statement supported by data
- [ ] Learnings extracted and recorded

### When Status = **Abandoned**
- [ ] Clear reason for abandonment
- [ ] What was learned despite not completing
- [ ] When (if ever) might this become viable
- [ ] Why this approach was deprioritized

---

## Quick Reference: What Data Should I Include?

| Section | Always Include | Sometimes Include | Never Forget |
|---------|----------------|-------------------|-------------|
| Date | ✅ | | YYYY-MM-DD format |
| Proposal | ✅ | | Core idea, 1-3 sentences |
| Rationale | ✅ | | Expected benefits |
| Status | ✅ | | One of four states |
| Files Changed | ✅ | Line ranges | Relative paths |
| Commits | ✅ | | At least 7-char hash |
| Before Metrics | ✅ | | Specific numbers, not vague |
| After Metrics | ✅ | | Same metrics as "Before" |
| Data Source | ✅ | | Test file, script, output |
| Issues | ✅ if any | | Impact and resolution |
| Outcome | ✅ | | Data-supported assessment |
| Learnings | ✅ | | Specific to this strategy |

---

## Common Mistakes to Avoid

### ❌ Vague Metrics
```
Before: It was slow
After: It's faster now
```
**Fix:**
```
Before: 45.2 seconds for 1000 epochs
After: 12.3 seconds for 1000 epochs
```

### ❌ Unsourced Claims
```
The F1 score improved significantly.
```
**Fix:**
```
F1 improved from 0.79 to 0.83 (source: tests/test_validation.py::test_f1_score, validation_results.json)
```

### ❌ Hidden Failures
```
Works great, just a minor edge case where it crashes on empty inputs.
```
**Fix:**
```
Crashes on empty inputs (Issue 1). Resolution: Added guard condition at line X. Status: Resolved.
Strategy improved performance 72% but reveals hidden edge case. Acceptable because this edge case is rare in production.
```

### ❌ Disconnected from Code
```
We optimized the pipeline.
```
**Fix:**
```
pyblinker/blink_detector.py (lines 45-90): Added caching logic.
Commits: a7f3e8c (feat: Add cache), b2d1f4e (test: Add cache tests)
```

### ❌ No Reflection
```
We implemented the cache. It works.
```
**Fix:**
```
Learnings:
- Cache key design is critical (too narrow misses, too broad risks correctness)
- LRU eviction is simple and effective for this access pattern
- Consider persistence layer (SQLite) for cross-session caching in future
```

---

## When to Update Your Entry

| Event | Action |
|-------|--------|
| You have a new idea | Create new entry with status=Proposed |
| You start implementing | Update status → In Progress, add Files/Commits |
| You make a commit | Add commit hash to Commits section |
| You encounter an issue | Add to Issues Encountered section |
| You resolve an issue | Update issue status → Resolved |
| You decide to abandon | Update status → Abandoned, explain why |
| You finish implementation | Run metrics, update Performance & Metrics |
| You complete the work | Set status → Completed, write Outcome & Learnings |

---

## Examples of Different Entry Types

### Simple Completed Entry (Success)
See: `EXAMPLES.md` → Example 1: Cache Blink Detection Results

### Failed Entry (Abandoned)
See: `EXAMPLES.md` → Example 2: GPU Acceleration Attempt

### A/B Comparison Entry
See: `EXAMPLES.md` → Example 3: Threshold Tuning

### Iterative Refinement Entry
See: `EXAMPLES.md` → Example 4: Epoch Exclusion Logic (Iterations 1 & 2)

---

## Final Checklist

Before marking a strategy as **Completed**, verify:

- [ ] Date is present in YYYY-MM-DD format
- [ ] Proposal is clear and concise
- [ ] Rationale explains why this approach matters
- [ ] Status is set to "Completed" or appropriate final state
- [ ] Files Changed lists actual files with line ranges
- [ ] Commits includes at least hash and message
- [ ] Before metrics are specific numbers (not vague)
- [ ] After metrics use same units as Before
- [ ] Change shows percentage improvement/regression
- [ ] Data Source is traceable (can someone verify it?)
- [ ] Issues (if any) are documented with resolution
- [ ] Outcome clearly states success/failure/mixed with supporting data
- [ ] Learnings are specific to this strategy (not generic)
- [ ] Entry is updated as work progressed (not written in retrospect)

---

**Reference Version**: 1.0.0  
**Last Updated**: 2026-04-02
