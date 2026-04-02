# Strategy Impact Log Skill

**Version**: 1.0.0  
**Purpose**: Record and track strategy proposals, code changes, performance metrics, and their effects on final results

## What This Skill Does

The Strategy Impact Log skill helps you maintain a durable, auditable record of:
- **What** strategies were proposed and why
- **How** each strategy was implemented (specific file changes and commits)
- **What** performance impact each strategy had (measured with real data)
- **What** issues were encountered and how they were resolved
- **What** was learned from each attempt
- **How** strategies evolved through iterations

## Directory Structure

```
strategy-impact-log/
├── skill.yaml                          # Skill metadata
├── INSTRUCTIONS.md                    # Detailed guide (7 sections)
├── EXAMPLES.md                        # 5 worked examples
├── CHANGELOG.md                       # Version history
├── TESTS.md                           # Test cases for validation
├── README.md                          # This file
├── exports/
│   ├── claude/
│   │   └── SKILL.md                  # Claude-compatible skill definition
│   ├── openai/
│   │   └── SKILL.md                  # OpenAI-compatible skill definition
│   └── gemini/
│       ├── GEM_INSTRUCTIONS.md       # Gemini-specific instructions
│       └── SETUP.md                  # Gemini setup guide
└── resources/
    └── notes.md                      # Design notes and best practices
```

## Quick Start

### 1. Create Your Project's Strategy Log

Create a `STRATEGY_LOG.md` file in your project's development documentation directory:

```markdown
# Strategy Impact Log

This document records all strategies and their effects.

## Strategy: [Your Strategy Name]

**Date**: YYYY-MM-DD
**Proposal**: [What is the core idea?]
**Rationale**: [Why try this approach?]
**Status**: Proposed / In Progress / Completed / Abandoned

### Implementation
[File changes and commits as you implement]

### Performance & Metrics
[Before/after measurements with sources]

### Issues Encountered
[Problems and how you resolved them]

### Outcome
[Did it work? Why or why not?]

### Learnings
[What did you learn?]
```

### 2. Create Entry Before Implementing

When you propose a new strategy:
- Create an entry with Proposal and Rationale
- Set Status to "Proposed"
- Share the reasoning with the team

### 3. Update as You Implement

As you make code changes:
- Update Implementation section with file paths and commits
- Set Status to "In Progress"
- Keep the entry up to date with your work

### 4. Measure and Document Results

After implementation:
- Capture before/after metrics
- Cite data sources (test files, exact paths)
- Document issues and trade-offs
- Set Status to "Completed" or "Abandoned"

### 5. Extract Learnings

Conclude each entry with:
- What succeeded or failed and why
- What you learned
- How this informs future decisions

## Example Entry (Complete)

```markdown
## Strategy: Cache Blink Detection Results

**Date**: 2026-04-02
**Proposal**: Cache epoch-level blink results to speed up repeated analyses
**Rationale**: Iterative development reprocesses same epochs multiple times
**Status**: Completed

### Implementation

**Files Changed**:
- `pyblinker/blink_detector.py` (lines 45-90): Added _CacheManager class with LRU eviction
- `tests/test_cache.py`: New test file with cache hit/miss scenarios

**Commits**:
- `a7f3e8c`: feat: Add LRU cache for blink detection results
- `b2d1f4e`: test: Add cache hit/miss test cases

### Performance & Metrics

**Before**: 1000 epochs in 45.2 seconds (no cache)
**After**: 1000 epochs in 12.3 seconds (with 90% cache hits)
**Change**: **-72.8% latency**

**Data Source**: `scripts/benchmark_cache.py` on `sample_data/seed_exp01_pyblinker_results_1.pkl`

### Issues Encountered

- **Cache key normalization**: Float precision variations prevented hits
  - *Resolution*: Normalize to 3 decimal places
  - *Impact*: Minimal; correctness trade-off worth it

- **Memory growth**: Cache unbounded on long sessions
  - *Resolution*: Implement LRU eviction (keep 1000 entries)
  - *Impact*: Memory stays < 200MB, acceptable

### Outcome

**Success**. Caching works as intended. Repeated analyses dramatically faster. Backward compatible.

### Learnings

- Cache key design is critical—too narrow misses opportunities, too broad risks correctness
- LRU is simple and effective for this use case
- Consider persistence layer (SQLite) for cross-session caching in future
```

## Key Principles

1. **Document First**: Create entry before implementing
2. **Be Specific**: Link to exact file paths, line ranges, commit hashes
3. **Measure Impact**: Use real metrics with sources, not vague claims
4. **Be Honest**: Record failures, trade-offs, and issues openly
5. **Reflect**: Every entry should include learnings
6. **Preserve History**: Never delete old entries—they document the solution's evolution

## Common Patterns

### A/B Strategy Comparison
Compare two approaches using identical metrics. Document trade-offs. State decision rationale.

### Iterative Refinement
Link each iteration to the previous. Explain what changed. Track metric progression.

### Abandoned Strategy
Mark as abandoned with clear reason. Extract learnings even from failures. Consider future viability.

## Integration with Your Workflow

### With Git
Include commit hashes that implement each strategy:
```bash
git log --oneline | grep -i "cache"
```

### With Tests
Reference test files that validate strategies:
```
Data Source: tests/test_cache.py::test_cache_hit_performance
```

### With Metrics
Link to benchmark scripts or output files:
```
Data Source: scripts/benchmark_cache.py on sample_data/seed_exp01.pkl
```

## What Gets Better Over Time

As you build up your strategy log:
- **Decision Making**: You can reference past strategies instead of repeating them
- **Onboarding**: New team members understand why certain choices were made
- **Pattern Recognition**: You start to see what approaches work for your problem domain
- **Confidence**: Every decision has documented rationale and measured outcomes

## Common Mistakes to Avoid

❌ **Vague metrics**: "It's faster now"  
✅ **Specific metrics**: "72.8% latency reduction from 45.2s to 12.3s"

❌ **Unsourced claims**: "The F1 score improved"  
✅ **Sourced metrics**: "F1 improved from 0.79 to 0.83 (source: validation_results.json, line 45)"

❌ **Hidden failures**: "Works great, just a minor issue"  
✅ **Honest assessment**: "Approach improved precision but increased false negatives. Trade-off acceptable because..."

❌ **Disconnected from code**: "We optimized the pipeline"  
✅ **Linked to code**: "pyblinker/blink_detector.py (lines 45-90). See commit a7f3e8c."

❌ **No reflection**: Entry ends after describing implementation  
✅ **With learnings**: Entry includes "What would we do differently? What does this enable?"

## Documentation

- **INSTRUCTIONS.md**: Complete guide with 6-step process and detailed rules
- **EXAMPLES.md**: 5 worked examples (success, failure, comparison, iteration, dead end)
- **TESTS.md**: Test cases to validate strategy entries
- **resources/notes.md**: Design notes, best practices, common pitfalls

## Platform-Specific Exports

- **Claude** (`exports/claude/SKILL.md`): Ready to use with Claude Code
- **OpenAI** (`exports/openai/SKILL.md`): Compatible with OpenAI implementations
- **Gemini** (`exports/gemini/`): Setup guide and instructions for Gemini

## Using This Skill in Projects

### For Claude Code Users
The skill is available in your agent skillbook. When proposing strategies or evaluating approaches, consult the skill for the structured format.

### For Team Documentation
Use the skill as a template for your project's strategy documentation. Create a `STRATEGY_LOG.md` in your project and follow the patterns.

### For Decision-Making
Before proposing a new strategy, check your project's log:
- What similar approaches have been tried?
- What trade-offs did they involve?
- What patterns work or don't work?
- Can you avoid repeating failed approaches?

## Next Steps

1. **Create a strategy log**: Set up `STRATEGY_LOG.md` in your project
2. **Record existing decisions**: Document strategies already implemented
3. **Start with new proposals**: Create entries for strategies currently under consideration
4. **Update regularly**: Maintain entries as work progresses
5. **Use for decisions**: Consult the log when making strategy choices

## Support

For questions about:
- **How to use the skill**: See INSTRUCTIONS.md
- **What to write**: See EXAMPLES.md
- **Design philosophy**: See resources/notes.md
- **Validation**: See TESTS.md

---

*Strategy Impact Log v1.0.0 | Created 2026-04-02*
