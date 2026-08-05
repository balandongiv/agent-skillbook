# Examples: Manuscript Artifact Provenance and Generator Naming

## Example 1: The filename answers the question

### Before

```
experiment_script/
  regen_paper_tables.py          <- writes 12 tables; which one is Table 4?
  plot_pr_operating_points.py    <- which figure is this?
  paper_result_figures.py        <- overlaps with the above?
  regen_simple_figs.py           <- and this?
  update_exp2_latex.py           <- writes tables too
```

### After

```
experiment_script/
  tab4_tab5_strategy_comparison_30s.py   -> tab_comparison_30s_epoch.tex, tab_exp2_inversions.tex
  fig7_pr_operating_points.py            -> fig_pr_scatter.{pdf,png}
  tab13_fig10_epoch_duration.py          -> tab_effect_different_epoch_size.tex + figure
  paper_data.py                          <- shared data layer, imported by all of the above
```

### Why it's better

"Regenerate Table 6" is now a one-line answer. The monolith is gone, so one table can be
re-run without recomputing eleven others, and a bug in one generator cannot silently
propagate into the rest.

---

## Example 2: The empty-table bug

```python
# The generator filtered on a value that no longer exists in the CSV.
df = df[(df.center_method == "median") & (df.selection == "all")]
```

The column had been renamed to `all_channel`. The filter matched nothing, the table was built
from zero rows, LaTeX compiled without complaint, and the manuscript carried an empty table.

The shared data layer makes this loud instead of silent:

```python
def per_channel(ds: str) -> pd.DataFrame:
    df = load("exp1", ds)
    df = df[(df["center_method"] == "median") & (df["selection"] == ALL_CHANNEL)]
    if df.empty:
        raise SystemExit(
            f"no selection=={ALL_CHANNEL!r} rows in {result_path('exp1', ds)} — "
            "the per-channel table cannot be built."
        )
```

---

## Example 3: The overwritten-mapping bug

```python
# Iterating every group in the config: the catch-all group appears last and wins,
# so every channel ends up labelled "all_channel" instead of its real region.
for group, channels in doc["eeg_regions"].items():
    for ch in channels:
        out[ch] = group
```

Fix by excluding the groups that are selection gates rather than anatomy, and saying why:

```python
#: Groups that are selection gates, not anatomical regions: coarse unions of the
#: left/right pairs, single-channel probes, and the full-montage umbrella. Including
#: them would make the channel->region map ambiguous.
_NON_REGION_GROUPS = frozenset({"all_channel", "frontal", "central", "parietal", "occipital"})

for group, channels in doc["eeg_regions"].items():
    if group in _NON_REGION_GROUPS or group.endswith("_only"):
        continue
```

---

## Example 4: The manifest as a machine-checkable map

```python
Artifact("tab:exp1_main", "table", ["e_result/tab_comparison_30s_epoch.tex"],
         "tab4_tab5_strategy_comparison_30s.py", _exp("exp2"),
         "best-channel-per-session; Wilcoxon two-sided, Bonferroni x6",
         "Headline four-condition comparison at 30 s epochs."),
```

```
$ python experiment_script/reproduce_manuscript.py check
All artifacts accounted for.

$ python experiment_script/reproduce_manuscript.py provenance tab:exp1_main
label       : tab:exp1_main
script      : experiment_script/tab4_tab5_strategy_comparison_30s.py
aggregation : best-channel-per-session; Wilcoxon two-sided, Bonferroni x6
source data :
   OK      publication_results/exp2_raja/exp2_strategy_comparison_raja_results.csv
   OK      publication_results/exp2_cao/exp2_strategy_comparison_cao2018_results.csv
```

Prose documentation of this mapping drifts within weeks. A failing command does not.

---

## Example 5: Removing a dropped experiment completely

An experiment cut from the paper leaves five kinds of debris. All of it goes:

| Kind | Example |
|---|---|
| Primary scripts | `exp4_a_boundary_tolerance_{raja,cao2018}.py` |
| Config | `setup/exp4_boundary_tolerance.yaml` |
| Generated LaTeX | `e_result/tab_boundary_tolerance.tex` |
| `\input` lines | `\input{e_result/tab_boundary_tolerance}` |
| Prose and method text | the subsection, plus the method sentence describing its IoU sweep |

Miss the last two and the manuscript compiles with an undefined reference — or worse, keeps a
method paragraph describing an analysis that no longer has results.

---

## Example 6: Generate the "this work" row, never hand-maintain it

### Before

```python
THIS_WORK = (r"\textbf{This work}", "Single frontopolar EEG",
             "Raja + Cao2018", "Event-level overlap", r"macro-$F_1$ 0.84 / 0.78")
```

### After

```python
def _this_work_row():
    """The present detector's row, read from publication_results so it cannot drift."""
    best = P.load_exp2_best()
    raja = P.macro(best, "raja", "Proposed-Med")[2]
    cao = P.macro(best, "cao", "Proposed-Med")[2]
    return (..., rf"macro-$F_1$ {raja:.2f} / {cao:.2f}")
```

The hardcoded values were two runs stale; the generated row reported 0.88 / 0.81. Any number
in a table is a candidate for this failure, including the ones about your own method.
