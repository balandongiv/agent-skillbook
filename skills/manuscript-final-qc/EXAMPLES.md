# Examples: Manuscript Final Compile QC Gate

## Example 1: A draft note that leaked into the rendered PDF

### Before (without this skill)

The forbidden-term grep passes, so the manuscript is declared "clean" and handed off:

```
$ pdftotext main.pdf - | grep -Ei 'dbo|murat' ; echo done
done            # 0 hits -> "clean"
```

But a table row was live (uncommented) draft text:

```latex
\texttt{extra\_analysis} &
\textbf{Pending refresh:} additional stale artifacts ... should be recomputed
or removed before final narrative revision. \\
```

…which renders verbatim in the published table.

### After (with this skill applied)

The gate also greps the rendered text for draft patterns and catches it:

```
$ pdftotext main.pdf - | grep -Ei 'TODO|pending refresh|should be recomputed|we recommend|placeholder'
... analyses without a corresponding rerun CSV are marked as pending refresh.
```

Fix (delete the draft row + its dangling caption phrase), then **recompile and re-grep**:

```
$ # remove the row + fix caption, then pdflatex -> biber -> pdflatex x2
$ pdftotext main.pdf - | grep -ci 'pending refresh'
0
QC_DONE pages=23 undefined=0 forbidden=0 draft_notes=0 numbers_ok=yes
```

### Why it's better

Editorial/draft notes are invisible to a domain-term grep but visible to readers. Grepping the rendered PDF for
draft patterns turns a silent embarrassment into a blocking check.

---

## Example 2: A table number that drifted from its source CSV

### Before (without this skill)

Compile is clean and the abstract reads confidently, so the number is trusted:

```
Abstract: "...achieved a pooled macro-F1 of 0.872..."
```

No one checks it against the artifact that produced it.

### After (with this skill applied)

The gate spot-checks headline numbers against their source:

```
$ python -c "import csv; r=[x for x in csv.DictReader(open('runs/exp41/summary.csv',encoding='utf-8')) \
    if x['dataset']=='all' and x['condition']=='Proposed-Med']; print(r[0]['macro_f1'])"
0.8666757077885343      # table/abstract says 0.872  -> MISMATCH, blocking
```

Trace and resolve: the abstract was stale; correct it to 0.867 (or re-derive), then recompile.

```
QC_DONE pages=23 undefined=0 forbidden=0 draft_notes=0 numbers_ok=yes
```

### Why it's better

A clean compile says nothing about correctness. Tying each headline number to its artifact (and never editing the
number to match a guess) catches stale values before reviewers do.
