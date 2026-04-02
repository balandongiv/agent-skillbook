# Strategy Impact Log - Design Notes

## Motivation

The Strategy Impact Log skill addresses a gap in development workflows: the loss of context around why decisions were made. When looking back at code history, git logs and commit messages answer "what changed?" and "when?", but they often don't capture "why was this approach chosen over alternatives?" or "what was learned from failed attempts?"

This skill makes that lost knowledge durable and retrievable.

## Key Design Decisions

### 1. Structured but Flexible Format

The skill defines a template with key sections (proposal, implementation, metrics, issues, outcome, learnings) but doesn't enforce rigid structure. This allows:
- Natural progression from proposal to completion
- Flexibility for different types of strategies (simple changes, A/B tests, iterative refinement, dead ends)
- Room for additional context or diagrams as needed

### 2. Metrics-First Thinking

The skill emphasizes capturing actual performance data rather than subjective assessments. This is important because:
- "Faster" is ambiguous; "72.8% latency reduction from 45.2s to 12.3s" is concrete
- Metrics enable comparison across strategies
- Real data prevents hindsight bias ("it worked great" vs "F1 improved from 0.79 to 0.83")

### 3. Honest Documentation of Failures

Unlike commit messages that tend to emphasize successes, this skill treats failures as equally valuable learning opportunities. The goal is to build a log that future agents/humans can learn from, which requires honesty about what didn't work.

### 4. Link to Implementation

By recording specific file paths, line ranges, and commit hashes, the strategy log becomes a companion to the codebase. Anyone can trace from a strategic decision back to the code that implements it, and vice versa.

### 5. Historical Preservation

The log is append-only. Old strategies are never deleted, even if they're superseded. This creates a trail that shows evolution:
- How did the solution improve over time?
- Why was approach A abandoned in favor of approach B?
- What conditions would need to change for approach A to become viable again?

## Relationship to Other Skills

### Experiment Runbook Discipline vs Strategy Impact Log

**Experiment Runbook Discipline** is about *how to execute* long-running experiments:
- Scope, prefixes, monitoring, validation
- Rolling logs, live status artifacts
- Promotion from smoke scopes to full runs
- Reproducibility and auditability of execution

**Strategy Impact Log** is about *what was tried* and *why*, with emphasis on:
- Decision rationale before execution
- Alternative approaches considered
- Trade-offs and their justification
- Learnings that inform future decisions

They complement each other: Runbook ensures experiments are executed rigorously; Strategy Log ensures decisions are documented thoroughly.

### Integration with Handoff/Resume Skills

The Strategy Log is a natural handoff artifact. When handing off work to another agent or person:
- The log provides context on what was tried and why
- It documents known pitfalls and dead ends
- It makes past decisions transparent, not opaque

## Common Use Cases

1. **Performance Optimization**: "We tried three approaches. Here are the metrics for each."
2. **Feature Implementation**: "We chose approach A because approach B had this trade-off."
3. **Bug Investigation**: "We considered three root causes. Here's why we ruled out X and Y."
4. **Refactoring Decisions**: "We evaluated refactoring vs leaving it. Here's the trade-off analysis."
5. **Technical Debt**: "We documented this as technical debt because [reason]. Here's what would need to change to address it."

## Potential Extensions

### Metrics Dashboard

A future tool could parse the strategy log and build a dashboard showing:
- Which strategies resulted in metrics improvements
- Trade-off analysis across multiple dimensions
- Time series of how metrics evolved across iterations

### Decision Pattern Analysis

Another tool could identify patterns:
- "Adaptive approaches consistently outperform fixed approaches"
- "Regex-based solutions have higher complexity but more flexibility"
- "Cache-based approaches trade memory for latency"

### Integration with Version Control

The log could be indexed by commit hash, enabling:
- "What strategies were implemented in commit ABC?"
- "When did we try approach X? What happened?"
- Blame/git log that includes strategy context

## Best Practices

1. **Create the entry before implementing**, not after. The act of writing down the proposal clarifies thinking.

2. **Update the entry as work progresses**, not as a final retrospective. This captures details that might be forgotten later.

3. **Include multiple perspectives**:
   - Technical metrics (latency, memory, accuracy)
   - Maintenance burden (complexity, test coverage)
   - User impact (features enabled, problems solved)
   - Time cost (estimation vs actual)

4. **Use consistent metrics across comparisons** so strategies can be compared fairly.

5. **Link back to code** with specific paths and commit hashes so decisions are traceable.

6. **Celebrate failures** as learning opportunities, not shortcomings. This encourages experimentation.

## Examples of Entry Maturity Levels

### Level 1: Minimal (Underspecified)
```
## Strategy: Optimize Performance
Status: Completed
Outcome: It works faster now.
```

This is too vague. Avoid.

### Level 2: Adequate (Acceptable)
```
## Strategy: Cache Blink Results
Status: Completed
Metrics: 72% faster on repeated analyses (12s vs 45s)
Issues: None
Outcome: Success
```

This answers the basic questions but lacks depth. Acceptable for simple changes.

### Level 3: Comprehensive (Ideal)
```
## Strategy: Cache Blink Results

**Proposal**: Implement LRU cache for blink detection to speed repeated analyses
**Rationale**: Iterative development requires reprocessing same epochs

### Implementation
**Files**: pyblinker/blink_detector.py (lines 45-90)
**Commits**: a7f3e8c, b2d1f4e

### Metrics
**Before**: 45.2s (1000 epochs, no cache)
**After**: 12.3s (1000 epochs, 90% cache hits)
**Source**: scripts/benchmark_cache.py on sample_data/seed_exp01.pkl

### Issues
- Cache key normalization (float precision)
  *Resolution*: Use 3 decimal place precision
  *Impact*: Acceptable trade-off for correctness

### Outcome
Success. Repeated analyses dramatically faster. Transparent to callers.

### Learnings
- Cache key design is critical
- LRU eviction is simple and effective
- Consider persistence layer for cross-session caching
```

This level is ideal: specific, traceable, actionable, and useful for future decisions.

## Avoiding Common Pitfalls

**Pitfall 1: Vague metrics**
- ❌ "It's much faster now"
- ✅ "Latency improved from 45.2s to 12.3s (72.8% reduction)"

**Pitfall 2: Unsourced claims**
- ❌ "The F1 score improved"
- ✅ "F1 improved from 0.79 to 0.83 (source: validation_results.json, line 45)"

**Pitfall 3: Hidden failures**
- ❌ "It mostly works great, just a minor edge case issue"
- ✅ "Regex approach misses annotations with special characters. Trade-off: 3% false negatives vs 1% with global approach. Acceptable because..."

**Pitfall 4: Disconnected from code**
- ❌ "We optimized the detection pipeline"
- ✅ "pyblinker/blink_detector.py (lines 45-90): Added caching logic. See commit a7f3e8c."

**Pitfall 5: Forgetting to reflect**
- ❌ Entry ends after describing what was done
- ✅ Entry includes "Learnings" section: what would we do differently? What does this enable? What patterns did we discover?
