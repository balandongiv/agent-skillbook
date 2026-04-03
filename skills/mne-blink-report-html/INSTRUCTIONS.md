# MNE Blink Report HTML

Use this skill to generate a saved MNE HTML report that plots blink windows one by one from epoch data.

---

## Core workflow

### 1. Identify the three core inputs

Collect:

- the epoch file, typically `.fif`
- the predicted blink table
- the reference blink table if the report is for matched subsets such as true positives, false negatives, or false positives

Expected blink-table columns after normalization:

- `epoch_index`
- `blink_onset`
- `blink_duration`

If the source file uses names like `epoch_id`, `epoch_onset_sec`, and `epoch_duration_sec`, rename them before plotting.

### 2. Decide the subset to plot

Pick one of:

- true positives
- false negatives
- false positives
- all predicted blinks
- all reference blinks

For matched subsets, use interval overlap within the same epoch. Do not guess by proximity alone.

### 3. Reuse the template script

Start from `scripts/report_blink_windows_template.py` in this skill.

Adapt only what is necessary:

- file paths
- subset selection
- channel list
- output report path
- title and summary metadata

Keep the plotting structure consistent unless the user asks for a different layout.

### 4. Plot each blink with fixed context

Default to `0.5 s` before and after each blink unless the user asks for a different padding.

For each blink figure:

- plot the chosen channels over the same time axis
- optionally add a frontal mean if frontal channels are present
- mark the reference interval
- mark the predicted interval when available
- title the figure with epoch index and onset-offset times

### 5. Save as MNE report HTML

Use `mne.Report`.

Always include:

- a summary section
- a table of the plotted blink rows
- one figure per plotted blink

Save the report to disk and tell the user the exact file path.

---

## Default plotting choices

- Use the filtered epoch data prepared by `prepare_epoch_detection_input(...)`.
- Prefer frontal channels for blink sanity checks:
  - `EEG Fp1 - Pz`
  - `EEG Fp2 - Pz`
  - `EEG F7 - Pz`
  - `EEG F8 - Pz`
  - `EEG F3 - Pz`
  - `EEG Fz - Pz`
  - `EEG F4 - Pz`
- Add `frontal_mean` when those channels are available.
- Use a single figure per blink, not one figure per channel.

---

## Rules

- Always normalize blink-table column names before matching or plotting.
- Always match predicted and reference blinks by overlap within the same epoch.
- Always include the plotted subset count in the summary.
- Always save the HTML artifact rather than relying on interactive display only.
- Never silently switch from matched subsets to raw predicted rows.
- Never plot without making clear whether the highlighted interval is reference, prediction, or both.

---

## Common mistakes to avoid

- **Using mismatched column names**: normalize reference and prediction tables first.
- **Comparing across epochs**: only match intervals within the same epoch.
- **Plotting only the detected interval**: keep the pre/post context window so the shape is interpretable.
- **Using too many channels**: start with the frontal set unless the user asks for a broader montage.
- **Forgetting the output artifact**: the task is not complete until the HTML report is written and its path is reported.

---

## Bundled resources

- Template script: `scripts/report_blink_windows_template.py`
- Notes: `resources/notes.md`
- OpenAI export: `exports/openai/SKILL.md`
