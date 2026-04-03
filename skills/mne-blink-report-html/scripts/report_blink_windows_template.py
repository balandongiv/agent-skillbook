"""Template for building an MNE HTML report of blink windows from epoch data.

Adapt the FILE PATHS and subset choice below for a concrete task.
The script is designed for this repository's epoch-based blink workflow.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path

import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd

from pyblinker.epoch_detection_strategy_a.epoch_blink_pipeline import (
    prepare_epoch_detection_input,
)


# ---------------------------
# Fill these values in first
# ---------------------------
EPOCHS_PATH = Path("sample_data/dev_epo.fif")
PREDICTED_TABLE_PATH = Path("sample_data/predicted_blinks.csv")
REFERENCE_TABLE_PATH = Path("sample_data/reference_blinks.csv")
OUT_HTML_PATH = Path("handoff/blink_report_template_output.html")

SUBSET = "true_positives"
PAD_S = 0.5
REPORT_TITLE = "Blink Report"
SECTION_NAME = "Blink windows"

CHANNELS_TO_PLOT = (
    "EEG Fp1 - Pz",
    "EEG Fp2 - Pz",
    "EEG F7 - Pz",
    "EEG F8 - Pz",
    "EEG F3 - Pz",
    "EEG Fz - Pz",
    "EEG F4 - Pz",
)


@dataclass
class PlotRow:
    epoch_index: int
    label: str
    ref_onset: float | None
    ref_duration: float | None
    pred_onset: float | None
    pred_duration: float | None
    overlap_s: float | None


def normalize_blink_table(frame: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        "epoch_id": "epoch_index",
        "epoch_onset_sec": "blink_onset",
        "epoch_duration_sec": "blink_duration",
    }
    frame = frame.rename(columns=rename_map).copy()
    required = {"epoch_index", "blink_onset", "blink_duration"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Missing required blink-table columns: {', '.join(missing)}")
    return frame[["epoch_index", "blink_onset", "blink_duration"]].copy().reset_index(drop=True)


def interval_overlap(left_onset: float, left_duration: float, right_onset: float, right_duration: float) -> float:
    left_end = float(left_onset + left_duration)
    right_end = float(right_onset + right_duration)
    return max(0.0, min(left_end, right_end) - max(left_onset, right_onset))


def match_rows(predicted: pd.DataFrame, reference: pd.DataFrame) -> tuple[list[PlotRow], list[PlotRow], list[PlotRow]]:
    true_positives: list[PlotRow] = []
    false_positives: list[PlotRow] = []
    false_negatives: list[PlotRow] = []

    for epoch_index in sorted(set(predicted["epoch_index"]) | set(reference["epoch_index"])):
        pred_group = predicted[predicted["epoch_index"] == epoch_index].reset_index(drop=True)
        ref_group = reference[reference["epoch_index"] == epoch_index].reset_index(drop=True)
        unmatched_ref = set(ref_group.index.tolist())

        for _, pred_row in pred_group.iterrows():
            best_ref = None
            best_overlap = 0.0
            for ref_index in list(unmatched_ref):
                ref_row = ref_group.loc[ref_index]
                overlap = interval_overlap(
                    float(pred_row["blink_onset"]),
                    float(pred_row["blink_duration"]),
                    float(ref_row["blink_onset"]),
                    float(ref_row["blink_duration"]),
                )
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_ref = ref_index

            if best_ref is None or best_overlap <= 0.0:
                false_positives.append(
                    PlotRow(
                        epoch_index=int(epoch_index),
                        label="false_positive",
                        ref_onset=None,
                        ref_duration=None,
                        pred_onset=float(pred_row["blink_onset"]),
                        pred_duration=float(pred_row["blink_duration"]),
                        overlap_s=None,
                    )
                )
                continue

            ref_row = ref_group.loc[best_ref]
            unmatched_ref.remove(best_ref)
            true_positives.append(
                PlotRow(
                    epoch_index=int(epoch_index),
                    label="true_positive",
                    ref_onset=float(ref_row["blink_onset"]),
                    ref_duration=float(ref_row["blink_duration"]),
                    pred_onset=float(pred_row["blink_onset"]),
                    pred_duration=float(pred_row["blink_duration"]),
                    overlap_s=float(best_overlap),
                )
            )

        for ref_index in sorted(unmatched_ref):
            ref_row = ref_group.loc[ref_index]
            false_negatives.append(
                PlotRow(
                    epoch_index=int(epoch_index),
                    label="false_negative",
                    ref_onset=float(ref_row["blink_onset"]),
                    ref_duration=float(ref_row["blink_duration"]),
                    pred_onset=None,
                    pred_duration=None,
                    overlap_s=None,
                )
            )

    return true_positives, false_positives, false_negatives


def build_plot_rows(predicted: pd.DataFrame, reference: pd.DataFrame, subset: str) -> list[PlotRow]:
    tp_rows, fp_rows, fn_rows = match_rows(predicted, reference)
    if subset == "true_positives":
        return tp_rows
    if subset == "false_positives":
        return fp_rows
    if subset == "false_negatives":
        return fn_rows
    if subset == "all_predicted":
        return [
            PlotRow(
                epoch_index=int(row.epoch_index),
                label="predicted",
                ref_onset=None,
                ref_duration=None,
                pred_onset=float(row.blink_onset),
                pred_duration=float(row.blink_duration),
                overlap_s=None,
            )
            for row in predicted.itertuples(index=False)
        ]
    if subset == "all_reference":
        return [
            PlotRow(
                epoch_index=int(row.epoch_index),
                label="reference",
                ref_onset=float(row.blink_onset),
                ref_duration=float(row.blink_duration),
                pred_onset=None,
                pred_duration=None,
                overlap_s=None,
            )
            for row in reference.itertuples(index=False)
        ]
    raise ValueError(f"Unknown subset: {subset}")


def plot_row(prepared, row: PlotRow, *, pad_s: float) -> plt.Figure:
    sfreq = float(prepared.sfreq)
    event_onset = row.ref_onset if row.ref_onset is not None else row.pred_onset
    event_duration = row.ref_duration if row.ref_duration is not None else row.pred_duration
    if event_onset is None or event_duration is None:
        raise ValueError("plot_row requires at least one interval")
    event_offset = float(event_onset + event_duration)

    win_start = max(0.0, float(event_onset - pad_s))
    win_end = min(float(prepared.epoch_length_samples / sfreq), float(event_offset + pad_s))
    start_sample = max(0, int(np.floor(win_start * sfreq)))
    end_sample = min(int(prepared.epoch_length_samples), int(np.ceil(win_end * sfreq)))
    time_axis = np.arange(start_sample, end_sample, dtype=float) / sfreq

    plot_channels = [channel for channel in CHANNELS_TO_PLOT if channel in prepared.channel_names]
    channel_indices = [prepared.channel_names.index(channel) for channel in plot_channels]
    window_data = prepared.data[int(row.epoch_index), channel_indices, start_sample:end_sample]
    frontal_mean = window_data.mean(axis=0) if len(channel_indices) else None

    fig, ax = plt.subplots(figsize=(11, 4.5))
    offset_step = 8e-05
    for line_index, (channel_name, channel_signal) in enumerate(zip(plot_channels, window_data)):
        ax.plot(
            time_axis,
            channel_signal + offset_step * line_index,
            lw=1.0,
            label=channel_name,
        )
    if frontal_mean is not None:
        ax.plot(
            time_axis,
            frontal_mean + offset_step * len(plot_channels),
            lw=2.0,
            color="black",
            label="frontal_mean",
        )

    if row.ref_onset is not None and row.ref_duration is not None:
        ax.axvspan(
            float(row.ref_onset),
            float(row.ref_onset + row.ref_duration),
            color="tab:green",
            alpha=0.18,
            label="reference",
        )
    if row.pred_onset is not None and row.pred_duration is not None:
        ax.axvspan(
            float(row.pred_onset),
            float(row.pred_onset + row.pred_duration),
            color="tab:orange",
            alpha=0.18,
            label="predicted",
        )

    ax.set_xlim(win_start, win_end)
    ax.set_xlabel("Time From Epoch Start (s)")
    ax.set_ylabel("Filtered Signal + channel offset")
    ax.set_title(f"Epoch {row.epoch_index} | {row.label}")
    ax.grid(True, alpha=0.2)
    ax.legend(loc="upper right", fontsize=8, ncol=2)
    fig.tight_layout()
    return fig


def main() -> None:
    epochs = mne.read_epochs(EPOCHS_PATH, preload=True, verbose="ERROR")
    prepared = prepare_epoch_detection_input(
        epochs,
        pick_types_options={"eeg": True},
        filter_low=1.0,
        filter_high=20.0,
        resample_rate=None,
    )
    predicted = normalize_blink_table(pd.read_csv(PREDICTED_TABLE_PATH))
    reference = normalize_blink_table(pd.read_csv(REFERENCE_TABLE_PATH))
    plot_rows = build_plot_rows(predicted, reference, SUBSET)

    report = mne.Report(title=REPORT_TITLE)
    summary_html = f"""
    <h3>{escape(REPORT_TITLE)}</h3>
    <ul>
      <li><b>Epoch file:</b> <code>{escape(str(EPOCHS_PATH))}</code></li>
      <li><b>Predicted table:</b> <code>{escape(str(PREDICTED_TABLE_PATH))}</code></li>
      <li><b>Reference table:</b> <code>{escape(str(REFERENCE_TABLE_PATH))}</code></li>
      <li><b>Subset:</b> {escape(SUBSET)}</li>
      <li><b>Rows plotted:</b> {len(plot_rows)}</li>
      <li><b>Padding:</b> {PAD_S:.2f} s before and after</li>
      <li><b>Channels:</b> {escape(', '.join(CHANNELS_TO_PLOT))}</li>
    </ul>
    """
    report.add_html(title="Summary", html=summary_html, section="Overview")
    report.add_html(
        title="Plot rows",
        html=pd.DataFrame(plot_rows).to_html(index=False, float_format=lambda value: f"{value:.6f}" if isinstance(value, float) else value),
        section="Overview",
    )

    for plot_index, row in enumerate(plot_rows):
        fig = plot_row(prepared, row, pad_s=PAD_S)
        try:
            report.add_figure(
                fig=fig,
                title=f"{plot_index:03d} | Epoch {row.epoch_index} | {row.label}",
                caption=(
                    f"Reference onset={row.ref_onset}, prediction onset={row.pred_onset}, "
                    f"padding={PAD_S:.2f}s"
                ),
                section=SECTION_NAME,
                tags=("blink", SUBSET),
            )
        finally:
            plt.close(fig)

    OUT_HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    report.save(OUT_HTML_PATH, overwrite=True, open_browser=False)
    print(f"report_path={OUT_HTML_PATH}")


if __name__ == "__main__":
    main()
