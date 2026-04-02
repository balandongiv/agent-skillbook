# Strategy Impact Log - Setup for Gemini

## Overview

The Strategy Impact Log skill provides a structured approach to recording and tracking strategies, code changes, and their performance impacts. This setup guide explains how to integrate this skill into your Gemini-based workflow.

## Installation

1. Copy the Strategy Impact Log skill directory to your agent skillbook
2. Ensure the skill manifest includes entries for:
   - `slug: strategy-impact-log`
   - `title: Strategy Impact Log`
   - `when_to_use`: Strategy proposal and tracking scenarios

## Basic Usage

### Creating a New Strategy Entry

When you identify a strategy worth pursuing:

1. Create or update your project's `STRATEGY_LOG.md` file
2. Add a new section with the strategy name and timestamp
3. Fill in: Proposal, Rationale, Status
4. Update as work progresses with Implementation, Metrics, Issues
5. Conclude with Outcome and Learnings

### Template

```markdown
## Strategy: [Name]

**Date**: YYYY-MM-DD
**Proposal**: [What and why]
**Rationale**: [Expected benefits]
**Status**: Proposed / In Progress / Completed / Abandoned

### Implementation
[Files and commits as work happens]

### Performance & Metrics
[Before/after numbers with sources]

### Issues Encountered
[Problems and how they were resolved]

### Outcome
[Did it work? Why or why not?]

### Learnings
[What did we learn? What would we do differently?]
```

## Configuration

### Enable Auto-Invocation

If your system supports auto-invocation, enable this skill to activate when:
- A new strategy or approach is being discussed
- Multiple approaches are being compared
- Implementation results need to be evaluated
- Historical decisions need to be understood

### Link to Code Repository

For maximum usefulness, ensure your strategy log is stored in the same repository as your code:
- Location: `development_strategy/STRATEGY_LOG.md` (or similar)
- Shared with all team members/agents working on the project
- Updated along with code commits

## Integration Points

### With Version Control

Record commit hashes that implement each strategy:
```markdown
**Commits**:
- `abc1234`: Initial implementation of cache logic
- `def5678`: Fix edge case handling
```

This creates a bidirectional link between strategy decisions and code changes.

### With Testing/Validation

Include references to test files or validation scripts that measure impact:
```markdown
**Metrics Source**: scripts/benchmark.py on sample_data/dev_epo.fif
```

### With Documentation

Link strategy decisions to design documents or architecture notes that explain the reasoning in more detail.

## Workflow Integration

### Before Implementation

1. Propose strategy in strategy log
2. Document rationale and expected benefits
3. Set status to "Proposed"
4. Get feedback/approval

### During Implementation

1. Update implementation section with file changes
2. Add commit hashes as commits are made
3. Update status to "In Progress"
4. Note any deviations from proposal

### After Implementation

1. Run metrics/tests
2. Document performance impact
3. Record any issues encountered
4. Update status to "Completed" or "Abandoned"
5. Extract and document learnings

## Best Practices

- **Timing**: Create entries before implementing, not after
- **Specificity**: Include file paths, line ranges, and commit hashes
- **Metrics**: Always measure impact with real data
- **Honesty**: Document failures and trade-offs, not just successes
- **Traceability**: Link every strategy to code changes
- **Reflection**: End each entry with learnings and future application
- **History**: Keep old entries; they document the solution's evolution

## Examples

See the full `EXAMPLES.md` file for detailed examples of:
- Simple performance improvement
- Failed strategy with learnings
- A/B strategy comparison
- Iterative refinement
- Abandoned ideas with reasoning

## Troubleshooting

**Issue**: Strategy entries become too verbose
- **Solution**: Use structured format; keep entries focused on what matters

**Issue**: Metrics are hard to interpret later
- **Solution**: Always cite data sources (which file, which test, exact path)

**Issue**: Comparing strategies is difficult
- **Solution**: Use identical metrics across all strategies being compared

**Issue**: Old entries seem irrelevant
- **Solution**: They document why certain paths weren't taken; preserve them as evidence

## Next Steps

1. Set up your first strategy log file in the project repository
2. Create an entry for a strategy currently under consideration
3. Update it as work progresses
4. Use it to inform future strategy decisions
