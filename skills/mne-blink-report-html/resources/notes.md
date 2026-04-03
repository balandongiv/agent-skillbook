# Notes: MNE Blink Report HTML

Use this skill for reusable per-blink HTML sanity checks.

Default assumptions:

- the source data is an epoch `.fif` file
- blink tables can be normalized to `epoch_index`, `blink_onset`, `blink_duration`
- plots use `0.5 s` padding before and after each blink
- the default channel set is frontal EEG plus an optional frontal mean

Useful subset labels:

- `true_positives`
- `false_negatives`
- `false_positives`
- `all_predicted`
- `all_reference`

For this repository, `prepare_epoch_detection_input(...)` is the preferred preprocessing entry point before plotting.
