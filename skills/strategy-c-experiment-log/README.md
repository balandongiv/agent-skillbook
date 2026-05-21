# Strategy C Experiment Log Skill

**Version**: 1.1.0  
**Purpose**: Keep every exploratory experiment tied to Strategy C logged inside `development_strategy/strategy_C/obs/` using the same structure that already lives in the existing approach logs so future agents can read a consistent history.

## What this skill does
- Requires every exploratory run, validation sweep, or experiment-centered analysis of Strategy C to add or update an entry in an existing Strategy C approach log under `development_strategy/strategy_C/obs/`.
- Reinforces the template structure already in that file (steps, metrics, issues, outcome, learnings) so logs stay uniform.
- Prompts agents to describe the experiment's proposal, rationale, implementation details, metrics, implementation-level benefits versus Strategy A and Strategy B, issues encountered, and final learnings.

## Log template recap
Log entries must follow this structure:
`
## Strategy: [strategy name]

**Date**: YYYY-MM-DD  
**Proposal**: ...  
**Rationale**: ...  
**Status**: Proposed / In Progress / Completed / Abandoned

### Implementation

**Files Changed**:
- path (lines X-Y): description

**Commits**:
- hash: message

### Performance & Metrics
**Before**: ...  
**After**: ...  
**Change**: ...

### Implementation Benefits
- why this is or is not a better implementation foundation than Strategy A
- why this is or is not a better implementation foundation than Strategy B
- how the design affects modularity, inspectability, downstream Stage 2 to 6 integration, and future extension work

### Issues Encountered
- **Issue**: description, impact, status

### Outcome
summary

### Learnings
summary
`
Use this snippet as your guide each time.

## Quick start
1. Mention the Strategy C Experiment Log skill explicitly when you ask for an exploratory experiment (see INCLUDE_NOTE.md).
2. Tell the agent what you are exploring, what hypotheses you have, and which datasets or metrics matter.
3. Have the agent append to the matching Strategy C approach log under `development_strategy/strategy_C/obs/`, filling every section even if some fields are “TBD”.

## Reminders
- Do not write the result outside `development_strategy/strategy_C/obs/`; keep the history in the Strategy C approach logs there.
- Cite exact files, commands, or scripts you used when describing implementation and metrics.
- Always include an **Implementation Benefits** section, even if the conclusion is that no real implementation advantage was shown.
- Update **Status** as work progresses and use the suggested statuses.
- Capture issues and learnings even for failed experiments—they teach future agents.

