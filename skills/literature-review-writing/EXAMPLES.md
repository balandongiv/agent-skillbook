# Examples: Knowledge-Library-Grounded Literature Review Writing

## Example 1: Library-grounded vs hallucinated citations

### Before (without this skill)

```
Several studies have used transformers for blink detection \citep{smith2021blinknet, lee2020deepblink}.
```

`smith2021blinknet` and `lee2020deepblink` are not in the library — they were invented because they
sounded plausible.

### After (with this skill applied)

```
# query library: keys present with theme "deep learning blink detection"
#   fodor2023blinklinmult | Transformer-Based Eye Blink Detection
#   gawande2022deep       | Deep-Learning Approach for Efficient Eye-blink Detection
Transformer- and CNN-based detectors have recently been applied to eye-blink detection
\citep{fodor2023blinklinmult,gawande2022deep}.
# GAP FLAG: no library entry specific to "video vision transformer blink" — ask user to add if needed.
```

### Why it's better

Only keys that exist in the library are cited; a missing-coverage gap is flagged for the user instead
of being filled with a fabricated paper.

---

## Example 2: Themed synthesis vs citation dump

### Before (without this skill)

```
Blink detection has been studied a lot \citep{a,b,c,d,e,f,g,h}.
```

### After (with this skill applied)

```
A first stream uses single-channel amplitude thresholding to localise blink peaks
\citep{chang2016detection,tran2021detection}. A second stream builds hybrid thresholding pipelines that
add robust outlier rejection \citep{kleifges2017blinker,cao2021unsupervised}. More recently, data-driven
detectors replace hand-tuned thresholds with learned models \citep{fodor2023blinklinmult,gawande2022deep},
which motivates the present focus on the interpretable thresholding stage these pipelines often build on.
```

### Why it's better

Prior work is grouped into method families with a narrative that leads into the paper's contribution,
and every key is library-backed.
