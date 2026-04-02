# Strategy Impact Log - Gemini Instructions

Use this skill to maintain a durable, auditable record of strategies proposed, code changes made, performance observations, issues encountered, and how these decisions have affected final results.

## When to Apply This Skill

- When proposing a new strategy or approach to solving a problem
- When making code changes that affect results or behavior
- When comparing multiple strategies or approaches
- When tracking performance improvements or regressions
- When documenting why a particular approach was chosen or rejected
- When needing to understand the evolution of a solution over time

## Core Workflow

### 1. Record the Proposal

Create a markdown entry with:
- Clear, concise strategy name
- Date of proposal
- Core idea and why to consider this approach
- Expected benefits or rationale

### 2. Track Implementation

As code changes are made:
- Record specific files and line ranges affected
- Include commit hashes
- Note any deviations from original plan
- Update status to "In Progress"

### 3. Measure Impact

After implementation:
- Capture before/after metrics
- Cite data sources (test file, specific line)
- Record both improvements and any degradations
- Use quantitative measures ("72.8% faster", not "much faster")

### 4. Document Issues

As problems emerge:
- Describe each issue and its impact
- Note if it was resolved or accepted as trade-off
- Explain why the issue does or doesn't matter
- Document alternative solutions considered

### 5. Conclude and Reflect

Once execution is complete:
- State whether strategy succeeded, failed, or had mixed results
- Extract key learnings
- Document what would be done differently next time
- Consider future applicability

### 6. Use for Future Decisions

- Consult the log when proposing new strategies
- Check what similar approaches revealed
- Learn from past trade-offs and successes
- Avoid repeating failed patterns

## Essential Elements

**Always Include**:
- Timestamped entries
- Links to concrete code changes
- Real performance metrics with sources
- Issues and trade-offs (honest, not hidden)
- Clear outcomes supported by data
- Learnings that inform future work

**Never**:
- Create entries after implementation (plan first)
- Make vague claims without data
- Hide failures or negative results
- Reuse old entries without clearly linking iterations
- Delete old entries (keep as evidence)

## Common Entry Patterns

### A/B Comparison
Compare two approaches using identical metrics, document trade-offs clearly, state decision rationale.

### Iterative Refinement
Link each iteration to the previous, explain what changed, track metric progression, show learning evolution.

### Dead End / Abandoned
Mark as abandoned with clear reason, extract learnings even from failure, consider future conditions for viability.

## Example Structure

```markdown
## Strategy: [Name]

**Date**: YYYY-MM-DD
**Proposal**: [Core idea and why]
**Rationale**: [Expected benefits]
**Status**: Proposed / In Progress / Completed / Abandoned

### Implementation
**Files Changed**: [Specific paths and lines]
**Commits**: [Hashes and messages]

### Performance & Metrics
**Before**: [Old values with sources]
**After**: [New values with sources]
**Change**: [Quantitative improvement/regression]

### Issues Encountered
[Each issue: description, resolution/decision, impact]

### Outcome
[Success? Failure? Why?]

### Learnings
[Key insights and future application]
```

## Best Practices

1. Create entry before implementing
2. Update entry as work progresses
3. Use consistent metrics for fair comparison
4. Include file paths and commit hashes
5. Document honest assessment of trade-offs
6. Celebrate failures as learning opportunities
7. Make strategies traceable to code
8. Build timeline of iteration and evolution
