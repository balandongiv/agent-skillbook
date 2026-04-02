# Strategy Impact Log - Test Cases

## Test 1: Basic Strategy Entry Creation

**Scenario**: Agent proposes a new optimization strategy.

**Expected behavior**:
- Agent creates a new section in the strategy log with title, date, and proposal
- Entry includes rationale for why the strategy should work
- Status is marked as "Proposed"
- Implementation section is populated as work begins

**Success criteria**:
- ✓ Entry is timestamped
- ✓ Proposal is clear and concise
- ✓ Rationale explains the expected benefit

---

## Test 2: Implementation Tracking

**Scenario**: Code changes are made to implement a strategy.

**Expected behavior**:
- Agent records specific files modified with line ranges
- Agent includes commit hashes as changes are committed
- Agent notes any deviations from the original proposal
- Status is updated to "In Progress"

**Success criteria**:
- ✓ File paths and line ranges are specific and verifiable
- ✓ Commit hashes are real and match the work done
- ✓ Changes accurately describe the implementation

---

## Test 3: Metric Capture

**Scenario**: Strategy is fully implemented and metrics are measured.

**Expected behavior**:
- Agent captures before/after metrics
- Agent cites data sources (which test, which file, exact location)
- Agent records both improvements and any degradations
- Numbers are specific, not vague ("72.8% faster", not "much faster")

**Success criteria**:
- ✓ Metrics are quantitative with units
- ✓ Sources are traceable and specific
- ✓ Both successes and trade-offs are recorded

---

## Test 4: Issue and Trade-off Documentation

**Scenario**: Problems are encountered during implementation.

**Expected behavior**:
- Agent records each issue with description and impact
- Agent notes whether the issue was resolved or accepted as a trade-off
- Agent explains why the issue does or doesn't matter for the use case
- Agent documents alternative solutions considered

**Success criteria**:
- ✓ Issues are specific, not vague
- ✓ Impact is clear and quantifiable when possible
- ✓ Resolution or decision is documented

---

## Test 5: Honest Outcome Assessment

**Scenario**: Strategy execution is complete.

**Expected behavior**:
- Agent states clearly whether the strategy succeeded, failed, or had mixed results
- Agent cites performance data to justify the assessment
- Agent doesn't claim success without evidence
- Agent doesn't hide failures or negative results

**Success criteria**:
- ✓ Outcome matches the metrics reported
- ✓ No unsupported claims (e.g., "worked great" without numbers)
- ✓ Failures are noted as learning opportunities, not hidden

---

## Test 6: Learning Extraction

**Scenario**: Strategy entry is complete.

**Expected behavior**:
- Agent reflects on what was learned
- Agent articulates what would be done differently next time
- Agent considers applicability to future work
- Learnings are specific to the strategy, not generic

**Success criteria**:
- ✓ Learnings are actionable and specific
- ✓ Future actions are clear (e.g., "always measure X before optimizing Y")
- ✓ Learnings connect back to the strategy's outcome

---

## Test 7: A/B Strategy Comparison

**Scenario**: Two approaches are tested and compared.

**Expected behavior**:
- Agent creates a comparison entry with separate sections for each approach
- Agent uses the same metrics for both approaches
- Agent documents trade-offs for each approach
- Agent clearly states which approach was chosen and why

**Success criteria**:
- ✓ Both approaches use identical metrics
- ✓ Trade-offs are honestly presented
- ✓ Decision rationale is clear

---

## Test 8: Iterative Refinement Tracking

**Scenario**: A strategy requires multiple attempts or refinements.

**Expected behavior**:
- Agent creates separate entries for each iteration
- Agent links each iteration to the previous one
- Agent clearly states what changed between iterations
- Agent tracks how metrics evolved across iterations

**Success criteria**:
- ✓ Each iteration is timestamped
- ✓ Previous attempt is referenced
- ✓ Changes from prior attempt are explicit
- ✓ Metrics show progression (or regression) across iterations

---

## Test 9: Abandoned Strategy Documentation

**Scenario**: A strategy is attempted but ultimately not used.

**Expected behavior**:
- Agent marks status as "Abandoned"
- Agent clearly explains why the strategy was abandoned
- Agent documents valuable learnings even though it didn't work
- Agent considers future conditions where the strategy might become viable

**Success criteria**:
- ✓ Reason for abandonment is specific
- ✓ Learnings extract value from the attempt
- ✓ No blame or dismissiveness in the writeup
- ✓ Future utility is considered

---

## Test 10: Using Historical Log for Future Decisions

**Scenario**: Agent proposes a new strategy, checks the log first.

**Expected behavior**:
- Agent reviews prior strategies to see if similar approaches were tried
- Agent considers metrics from prior attempts
- Agent avoids repeating failed patterns
- Agent builds on successful patterns

**Success criteria**:
- ✓ Agent explicitly references relevant prior entries
- ✓ Rationale for new strategy acknowledges learnings from prior attempts
- ✓ If similar approach was tried before, agent explains why this attempt differs

---

## Integration Test: Full Workflow

**Scenario**: Complete strategy lifecycle from proposal through completion.

**Expected behavior**:
1. Agent proposes a strategy with clear rationale
2. Agent creates initial entry with Proposed status
3. Agent updates entry as implementation proceeds
4. Agent records specific files and commits
5. Agent captures metrics after implementation
6. Agent documents issues encountered and how they were resolved
7. Agent concludes with honest assessment and learnings
8. Entry becomes reference for future strategy decisions

**Success criteria**:
- ✓ Timeline flows logically from proposal to completion
- ✓ All sections are populated with specific, verifiable information
- ✓ Metrics support the outcome assessment
- ✓ Entry is useful for future decision-making
- ✓ No significant details are missing or vague
