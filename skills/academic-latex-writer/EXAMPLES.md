# Examples: Academic LaTeX Paragraph Writer (ChatGPT UI)

## Example 1: The topic sentence carries the paragraph

### Before (without this skill)

```latex
The precision--recall operating points are shown in Figure~\ref{fig:pr_a} and
Figure~\ref{fig:pr_b}. In the pooled analysis, Proposed-Med and Proposed-Mean occupied the
high-precision, high-recall region, with precision and recall of 0.8127 and 0.8956 ...
```

### After (with this skill applied)

```latex
Across the pooled and corpus-specific analyses, the precision--recall operating points
showed a consistent ordering among the proposed and baseline conditions
(Figure~\ref{fig:pr_a} and Figure~\ref{fig:pr_b}). In the pooled analysis, Proposed-Med and
Proposed-Mean occupied the high-precision, high-recall region, with precision and recall of
0.8127 and 0.8956 ...
```

### Why it's better

The original opens with a *pointer*: it says where something is, not what is true. A reader
skimming topic sentences learns nothing. The revision states the finding — a consistent
ordering — and demotes the figure references to a parenthetical, so the same skim now yields
the argument.

---

## Example 2: A citation is not a topic sentence

### Before

```latex
The median/MAD centre was selected to reduce the influence of within-epoch peaks, consistent
with the general robustness of median-based estimators~\citep{leys2013detecting,rousseeuw1993alternatives}.
This rationale was not supported by a measurable performance gain in the present benchmark.
```

### After

```latex
The pipeline's advantage therefore arises from screening epochs before threshold estimation
rather than from whether the retained amplitudes are centred by the median or the mean. The
median/MAD centre was selected to reduce the influence of within-epoch peaks, consistent with
the general robustness of median-based estimators~\citep{leys2013detecting,rousseeuw1993alternatives}.
This rationale was not supported by a measurable performance gain in the present benchmark.
```

### Why it's better

The original buries its conclusion in sentence three and opens with background plus two
citations. The revision leads with the claim the paragraph exists to make, and "therefore"
ties it to the preceding paragraph. Note that nothing was deleted — the preservation gate
requires every number and citation key to survive a structural revision.

---

## Example 3: The evidence packet, and what it forbids

### Packet (built by code, never by the model)

```
Macro-averaged results, best-channel-per-session, 30 s epochs (n=104):
  [Pooled]
    BLINKER-concat: P=0.6182 R=0.9627 F1=0.7256
    Proposed-Med:   P=0.8127 R=0.8956 F1=0.8403
Wilcoxon, two-sided, Bonferroni x6:
    BLINKER-concat vs Proposed-Med: p=1.32e-11
```

### Accepted draft

```latex
In the strategy comparison, the proposed configuration achieved higher macro-$F_1$ than the
baseline on the pooled evaluation (Table~\ref{tab:main}). Proposed-Med obtained 0.8403 against
0.7256 for BLINKER-concat, a difference that was significant under a paired Wilcoxon
signed-rank test with Bonferroni correction ($p=1.32\times10^{-11}$).
```

### Rejected draft

```latex
... Proposed-Med obtained 0.8403 against 0.7256 for BLINKER-concat, an improvement of
15.8\% ...
```

`verify_numbers` rejects this: `15.8` appears nowhere in the packet. The model computed it,
and it is wrong (the actual relative gain is 15.8 *points* of a different quantity than the
phrasing implies). Either add the derived value to the packet — computed in code — or drop
the claim.

---

## Example 4: Reporting a negative result honestly

### Prompt fragment

```
This paragraph must be scrupulously honest, because the result does NOT match the stated
hypothesis. The hypothesis was that the median/MAD estimator would improve precision. What
actually happened is the reverse on precision and a gain on recall, with a small net F1
advantage that is not statistically significant. Report this plainly and do not claim
support for the hypothesis.
```

### Resulting prose

```latex
Within the two proposed configurations, the Stage-B threshold estimators produced similar
overall performance, although the direction of the metric changes did not support the stated
precision hypothesis (Table~\ref{tab:main}). ... The two estimators were statistically
indistinguishable under the two-sided Bonferroni-corrected Wilcoxon test ($p=1$).
```

### Why the explicit instruction matters

Without it the model reliably writes "the median centre showed a modest precision benefit" —
narrating the hypothesis rather than the data. State the negative result in the task text.

---

## Example 5: Layout on disk

```
writing/
  e_result/
    result.tex                    <- \input chain only
    r1_channel_ablation/paragraph.tex
    r2_strategy_main/paragraph.tex
    r3_epoch_duration/paragraph.tex
  _packets/
    r1_channel_ablation.txt       <- built by code from the artifacts
    r2_strategy_main.txt
  _transcripts/
    r2_strategy_main.prompt.txt   <- audit record
    r2_strategy_main.reply.txt
```

`result.tex` contains only structure and `\input{}` lines. When a build breaks or a number is
questioned, the failing unit is one small file with its own packet and its own transcript.
