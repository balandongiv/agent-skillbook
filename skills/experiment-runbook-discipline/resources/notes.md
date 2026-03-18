# Notes: Experiment Runbook Discipline

This skill distills reusable runbook rules for long-running experiments and validation sweeps.

Core artifacts to prefer:

- markdown investigation note
- rolling text log
- live status JSON
- live status Markdown
- final summary CSV
- final overall JSON

Core checkpoints to preserve:

- confirm dataset path and scope before running
- choose a fresh experiment prefix
- verify progress through changing counters or timestamps
- confirm final metrics from produced artifacts
- rerun validated scopes under a new prefix after result-affecting logic changes
