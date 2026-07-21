# Examples: Parallel Agents in Git Worktrees

---

## Example 1: Provisioning a fresh worktree so the worker uses real data

### Before (without this skill)

```text
git worktree add ../ws-kinematics -b agent/ml/kinematics
# launch the agent
# paths.yaml is git-ignored, so it isn't in the new tree
# the worker can't resolve the dataset and generates .synthetic_data to keep going
# it reports results on ~4 fabricated events per session
```

### After (with this skill applied)

```text
git worktree add ../ws-kinematics -b agent/ml/kinematics
cp paths.yaml ../ws-kinematics/                 # copy the git-ignored runtime config
# spot-check: the worker resolves the REAL dataset and event counts look right
# handoff says: "if real inputs cannot be resolved, STOP and report — never synthesize"
# launch the agent
```

### Why it's better

The worker runs on real inputs, and a collapse in event counts is treated as a red flag rather
than silently accepted as a result.

---

## Example 2: Consolidating by assembling, not raw-merging

### Before (without this skill)

```text
git checkout consolidate
git merge agent/ml/wavelet
git merge agent/ml/mode-decomp
# conflicts in the shared harness on every merge, even though it's identical
```

### After (with this skill applied)

```text
# 1. Verify the shared harness is byte-identical across branches
git diff agent/ml/wavelet agent/ml/mode-decomp -- src/pkg/evaluation.py   # empty

# 2. Bring each workstream's UNIQUE files onto the consolidation branch
git checkout consolidate
git checkout agent/ml/wavelet      -- src/pkg/wavelet_features.py scripts/run_wavelet.py tests/test_wavelet.py
git checkout agent/ml/mode-decomp  -- src/pkg/mode_features.py    scripts/run_mode_decomp.py tests/test_mode_decomp.py
```

### Why it's better

When the shared files match, assembling the unique files avoids meaningless merge conflicts and
keeps history clean while preserving each workstream's contribution.

---

## Example 3: Teardown to a single clean mainline

### Before (without this skill)

```text
# push main
# leave 8 worktrees and 11 branches lying around
```

### After (with this skill applied)

```text
git push origin main
for w in ../ws-*; do git worktree remove "$w"; done
git branch -d agent/ml/wavelet agent/ml/mode-decomp ...   # delete merged branches
git worktree prune
# repo ends as one clean mainline
```

### Why it's better

The repository ends in a single, well-defined state instead of accumulating stale worktrees and
merged branches that confuse later agents.
