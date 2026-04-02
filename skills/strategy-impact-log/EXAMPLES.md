# Strategy Impact Log Examples

## Example 1: Simple Performance Improvement

```markdown
## Strategy: Cache Blink Detection Results

**Date**: 2026-04-02  
**Proposal**: Instead of recomputing blink detection for every epoch, cache results keyed by epoch properties to avoid redundant computation on repeated runs.  
**Rationale**: Blink detection is deterministic—if we've already detected blinks for a given epoch with specific parameters, we should reuse that result. This could significantly speed up iterative analysis and validation runs.  
**Status**: Completed

### Implementation

**Files Changed**:
- `pyblinker/blink_detector.py` (lines 45-90): Added `_CacheManager` class to handle in-memory cache with LRU eviction
- `pyblinker/epoch_detection_strategy_c/pipeline.py` (lines 120-135): Integrated cache lookup before processing
- `tests/test_cache.py`: New test file with cache hit/miss scenarios

**Commits**:
- `a7f3e8c`: feat: Add LRU cache for blink detection results
- `b2d1f4e`: test: Add cache hit/miss test cases
- `c5e2a9f`: docs: Document cache behavior and cache key structure

### Performance & Metrics

**Before**: 1000 epochs processed in 45.2 seconds (no cache)  
**After**: 1000 epochs processed in 12.3 seconds (with cache hits on 90% of calls)  
**Change**: **-72.8% latency** on repeated analyses

**Data Source**: `scripts/benchmark_cache.py` run on `sample_data/seed_exp01_pyblinker_results_1.pkl`

**Notes**: 
- First pass still takes ~45s (no cache yet)
- Subsequent passes on same data take ~2.3s (cached hits)
- Cache invalidation occurs when epoch parameters change

### Issues Encountered

- **Issue 1**: Cache key construction needed to account for subtle parameter differences (e.g., `threshold=0.5` vs `threshold=0.50`)
  - *Resolution*: Normalized all float parameters to 3 decimal places in cache key
  - *Impact*: Minimal, trade-off worth it for cache hits

- **Issue 2**: Memory usage grows with cache size on long-running analysis sessions
  - *Resolution*: Implemented LRU eviction (keep 1000 most recent entries)
  - *Impact*: Memory stays below 200MB in typical use, acceptable trade-off

### Outcome

**Success**: Caching worked as intended. Repeated analyses on the same dataset are now dramatically faster, and the cache is transparent to callers (backward compatible).

### Learnings

- Cache key design is critical—overly narrow keys miss opportunities, overly broad keys introduce correctness risks
- LRU eviction is simple and effective; consider adding a `cache.clear()` method for edge cases
- Worth considering whether to persist cache across sessions (SQLite backend) for larger projects

### Next Steps

None immediately. Could revisit persistence layer if users request cross-session caching.
```

---

## Example 2: Failed Strategy with Learnings

```markdown
## Strategy: GPU Acceleration for Batch Processing

**Date**: 2026-03-28  
**Proposal**: Use PyTorch GPU tensors to vectorize epoch-by-epoch blink detection, aiming for 10x speedup on batches of 100+ epochs.  
**Rationale**: Current detection is CPU-bound and processes epochs serially. GPU would enable massive parallelization.  
**Status**: Abandoned

### Implementation Attempt

**Files Changed**:
- `pyblinker/gpu_detector.py` (new file): GPU implementation using torch.cuda

**Commits**:
- `d8e4f2a`: feat: GPU acceleration attempt with PyTorch

### Performance & Metrics

**Before**: 100 epochs in 4.2 seconds (CPU, serial)  
**After (GPU)**: 100 epochs in 8.7 seconds (GPU, with transfer overhead)  
**Change**: **+107% slower** (regression)

**Data Source**: `scripts/benchmark_gpu.py` on `sample_data/seed_exp01_pyblinker_results_1.pkl`

### Issues Encountered

- **Issue 1**: GPU transfer overhead dominated execution time
  - Individual epoch processing is too lightweight to justify CPU↔GPU transfer cost
  - Transfer alone took ~4-5ms per batch, larger than the actual computation
  
- **Issue 2**: Not all operations were GPU-friendly
  - EDF file loading and annotation parsing remained CPU-bound
  - Vectorization only benefited the core detection kernel, not the I/O or prep stages

### Outcome

**Abandoned**: GPU acceleration actually made things *slower* due to transfer overhead and bottlenecks in non-vectorizable stages. The win-case (100+ epochs in one batch with all computation on GPU) didn't match our actual usage patterns.

### Learnings

- GPU acceleration requires careful profiling of actual bottlenecks before implementation
- Transfer overhead can outweigh computation time for lightweight operations
- End-to-end analysis often has non-parallelizable stages (I/O, parsing) that cap speedup potential
- In hindsight, memory caching (completed as separate strategy) was a better fit for our repeated-access pattern

### Why This Matters

If the project scales to truly massive batch processing (10k+ epochs in one pass), GPU might become viable. But for the current interactive/iterative workflow, CPU with caching is simpler and faster.

### Alternative Approaches Considered

- Numba JIT compilation (lower barrier than GPU, might be worth revisiting)
- Multiprocessing on CPU (could parallelize epoch loop without transfer overhead)
```

---

## Example 3: A/B Strategy Comparison

```markdown
## Strategy: Blink Detection Threshold Tuning

**Date**: 2026-03-20  
**Proposal**: Test two threshold strategies to determine which maximizes F1 score on validation set.  
**Status**: Completed

### Approach A: Global Fixed Threshold (0.5)

**Implementation**:
- `pyblinker/blink_detector.py` (lines 60-70): Use fixed threshold for all subjects
- Simple, deterministic, no parameter tuning needed

**Metrics** (on validation set, n=50 subjects):
- Precision: 0.82
- Recall: 0.76
- F1: 0.79
- False Positives: 12
- False Negatives: 24

**Trade-offs**:
- Pros: Simple, fast, no tuning required
- Cons: May not adapt to different signal quality across subjects

### Approach B: Adaptive Per-Subject Threshold

**Implementation**:
- `pyblinker/adaptive_threshold.py` (new file, lines 1-150): Per-subject threshold calibration
- Adds preprocessing step: fit threshold to each subject's signal statistics
- Adds hyperparameter: calibration set size (used 10 epochs per subject)

**Metrics** (on validation set, n=50 subjects):
- Precision: 0.85
- Recall: 0.81
- F1: 0.83
- False Positives: 9
- False Negatives: 19

**Trade-offs**:
- Pros: Better F1, lower false negatives (crucial for clinical use)
- Cons: Requires calibration data, adds ~2s per subject during setup

### Outcome: Approach B Selected

**Decision**: Adaptive threshold wins on F1 (+5.1%) and is more robust to signal quality variation. The calibration overhead is acceptable (typically <100ms on real data).

**Commits**:
- `e9f5d3b`: feat: Add adaptive per-subject threshold
- `f6a4e7c`: test: Compare adaptive vs fixed threshold on validation set
- `g7h8i9j`: docs: Document threshold calibration process

### Learnings

- Signal quality varies significantly across subjects; adaptive approach captures that variation
- Calibration with just 10 epochs is sufficient; diminishing returns beyond that
- Clinical context matters: lower false negatives is worth the false positive trade-off

### Future Considerations

Could explore ensemble thresholds (weighted average of global + adaptive) if clinical feedback suggests false positives are also an issue.
```

---

## Example 4: Iterative Refinement

```markdown
## Strategy: Epoch Exclusion Logic — Iteration 1

**Date**: 2026-03-15  
**Proposal**: Exclude "bad" epochs (marked in annotations) from blink detection to improve signal quality.  
**Status**: Completed → See Iteration 2

### Implementation

**Files Changed**:
- `pyblinker/epoch_detection_strategy_c/pipeline.py` (lines 80-100): Added epoch exclusion filter
- Simple boolean check: skip epochs where annotation contains "bad"

**Metrics**:
- Valid epochs: 950 / 1000 (95% coverage)
- Processing time: 38.2s
- F1 on remaining epochs: 0.81

### Issues Encountered

- Detected that simple string matching misses some edge cases
- Some epochs marked as "bad_signal_quality" but not "bad"—these should also be excluded

### Outcome

Basic exclusion works but needs refinement. → Proceed to Iteration 2.

---

## Strategy: Epoch Exclusion Logic — Iteration 2

**Date**: 2026-03-17  
**Previous Attempt**: Iteration 1 (simple string match)  
**Change From Last Attempt**: Use regex pattern to match any annotation containing "bad", including "bad_signal_quality", "bad_impedance", etc.  
**Status**: Completed

### Implementation

**Files Changed**:
- `pyblinker/epoch_detection_strategy_c/pipeline.py` (lines 80-100): Changed from string equality to regex search

**Code Change**:
```python
# Before:
exclude = annotation == "bad"

# After:
exclude = bool(re.search(r'\bbad\w*', annotation, re.IGNORECASE))
```

**Commits**:
- `h8i9j0k`: fix: Use regex for flexible epoch exclusion matching

### Metrics (on same 1000 epochs):
- Valid epochs: 920 / 1000 (92% coverage, more aggressive filtering)
- Processing time: 36.1s
- F1 on remaining epochs: 0.84 (+3.7% improvement)

### Outcome

**Success**: Regex approach is more flexible and actually improves F1 on the remaining epochs (likely because we're now correctly filtering truly problematic data). Ready for production.

### Learnings

- Annotations are often more granular than a simple boolean value
- Regex matching is worth the small overhead for flexibility
- Stricter data filtering can paradoxically improve metrics on remaining data
```

---

## Example 5: Abandoned Idea with Reasoning

```markdown
## Strategy: Custom Binary File Format for Epoch Cache

**Date**: 2026-03-10  
**Proposal**: Design a custom binary format to store cached blink detection results (instead of pickle) for smaller file size and faster loading.  
**Status**: Abandoned

### Rationale

Pickle files are convenient but large (~2MB per 1000 epochs). Custom binary format could halve size and load faster.

### Investigation

- Estimated custom format overhead: ~200 lines of code
- Estimated size reduction: 40-50%
- Estimated speed improvement: 15-20%

### Why Abandoned

During initial prototyping:
1. Pickle with compression (`.pkl.gz`) achieved 45% size reduction with zero custom code
2. Most of our workflow processes freshly computed results (no persistent cache) so file size matters little
3. Load time is negligible compared to computation time
4. Maintenance burden of a custom format not justified

### Decision

Use pickle with gzip compression. Simpler, achieves same goals, less technical debt.

### Learnings

Premature optimization trap: measure first, optimize only bottlenecks. Compression gave us 90% of the benefit with 10% of the effort.
```
