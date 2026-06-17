# Examples: MNE Blink Report HTML

## Example 1: Inspecting false negatives blink-by-blink

### Before (without this skill)

```
A metrics table reports recall = 0.72, but it is unclear which blinks were missed or why.
```

### After (with this skill applied)

```python
# Generate an MNE HTML report plotting only the false-negative blink windows, one per figure,
# with padding around each window and the configured channel set.
build_blink_report(epochs, detections, subset="false_negatives", pad_s=0.3,
                   channels=["Fp1", "Fp2"], out_html="fn_blinks.html")
# -> open fn_blinks.html and scroll missed blinks individually
```

### Why it's better

The missed blinks become visually inspectable one at a time, turning an opaque recall number into a
concrete, debuggable artifact.

---

## Example 2: Comparing TP vs FP morphology

### Before (without this skill)

```
False positives are reported only as a count.
```

### After (with this skill applied)

```python
build_blink_report(epochs, detections, subset="true_positives", out_html="tp.html")
build_blink_report(epochs, detections, subset="false_positives", out_html="fp.html")
# compare waveform shape of correct detections vs spurious ones
```

### Why it's better

Side-by-side HTML reports reveal whether false positives are saccades, drift, or muscle artifacts,
informing threshold and channel choices.
