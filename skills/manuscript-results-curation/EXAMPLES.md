# Examples: Manuscript Results Curation

---

## Example 1: Adding a subject-performance table to the paper

### Before (without this skill)

```text
Mention that some subjects perform worse than others.
```

### After (with this skill applied)

```text
1. Derive the per-subject metrics table from the completed run artifacts.
2. Insert the table directly into `writing/result/result.tex`.
3. Explain which subject is the weakest, which is the strongest, and what that spread implies for the experiment.
4. Rebuild the manuscript and record the compile log.
```

### Why it's better

The result section becomes concrete, comparable, and tied to the real run instead of making an unsupported general statement.

---

## Example 2: Writing a direct conclusion about experiment readiness

### Before (without this skill)

```text
The results look promising overall.
```

### After (with this skill applied)

```text
Conclusion so far:
- Experiment 1 provides the strongest signal.
- Experiments 2 and 3 support the multimodal direction.
- Experiment 4 remains weak and likely needs setup refinement.
- The current evidence suggests the project is on the right track, but the experiment design still needs improvement before strong final claims.
```

### Why it's better

It tells the reader what is working, what is not yet convincing, and how that affects the interpretation of the project.

---

## Example 3: Adding a new figure with interpretation

### Before (without this skill)

```text
Add a graph of the run results.
```

### After (with this skill applied)

```text
1. Create a reproducible plot from the run's metrics or predictions.
2. Save it under the manuscript figure workflow.
3. Reference it in `writing/result/result.tex`.
4. Explain what comparison the graph highlights and why it matters for the current hypothesis.
5. Rebuild the PDF and record the compile evidence.
```

### Why it's better

It ensures the figure is not decorative; it serves a specific interpretive purpose in the manuscript.
