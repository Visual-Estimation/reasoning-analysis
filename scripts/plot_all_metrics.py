"""
Plot metrics comparison across all categories and models.
Categories: weight, stability, angle, liquid_volume (continuous) + fit (classification)
Models: OpenAI, Gemini, Gemini-Robotics

All batches shown explicitly — no averaging across batches.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "results"

# ── Hardcoded data from the txt files ────────────────────────────────────────
# Format: {model: {batch: {metric: value}}}
# Batches 1-3; values averaged later for summary views.

# ── WEIGHT ───────────────────────────────────────────────────────────────────
weight = {
    "OpenAI": {
        1: dict(mape_all=100.17, mape_filt=35.70, corr_all=0.94, w25_all=55.36, w50_all=71.43, w25_filt=60.78, w50_filt=78.43),
        2: dict(mape_all=121.86, mape_filt=38.42, corr_all=0.82, w25_all=47.32, w50_all=67.86, w25_filt=51.96, w50_filt=74.51),
        3: dict(mape_all=72.55,  mape_filt=36.75, corr_all=0.92, w25_all=57.14, w50_all=71.43, w25_filt=62.75, w50_filt=78.43),
    },
    "Gemini": {
        1: dict(mape_all=54.55, mape_filt=29.54, corr_all=0.95, w25_all=43.75, w50_all=76.79, w25_filt=48.04, w50_filt=84.31),
        2: dict(mape_all=49.66, mape_filt=29.94, corr_all=0.95, w25_all=45.95, w50_all=76.58, w25_filt=50.50, w50_filt=84.16),
        3: dict(mape_all=50.72, mape_filt=28.94, corr_all=0.97, w25_all=45.54, w50_all=78.57, w25_filt=50.00, w50_filt=86.27),
    },
    "Gemini-Robotics": {
        1: dict(mape_all=49.47, mape_filt=28.99, corr_all=0.96, w25_all=53.57, w50_all=71.43, w25_filt=58.82, w50_filt=78.43),
        2: dict(mape_all=51.33, mape_filt=29.72, corr_all=0.95, w25_all=51.79, w50_all=75.00, w25_filt=56.86, w50_filt=82.35),
        3: dict(mape_all=51.22, mape_filt=30.14, corr_all=0.96, w25_all=50.89, w50_all=74.11, w25_filt=55.88, w50_filt=81.37),
    },
}

# ── STABILITY ────────────────────────────────────────────────────────────────
# MAPE "with all" is astronomically large (division by zero GT=0 cases)
# We use 'nan' for those and only plot filtered MAPE.
stability = {
    "OpenAI": {
        1: dict(mape_all=np.nan, mape_filt=37.41, corr_all=0.77, w25_all=35.85, w50_all=58.49, w25_filt=44.19, w50_filt=65.12),
        2: dict(mape_all=np.nan, mape_filt=41.32, corr_all=0.78, w25_all=24.53, w50_all=56.60, w25_filt=30.23, w50_filt=67.44),
        3: dict(mape_all=np.nan, mape_filt=35.89, corr_all=0.82, w25_all=39.62, w50_all=60.38, w25_filt=48.84, w50_filt=72.09),
    },
    "Gemini": {
        1: dict(mape_all=np.nan, mape_filt=41.93, corr_all=0.74, w25_all=30.19, w50_all=54.72, w25_filt=37.21, w50_filt=65.12),
        2: dict(mape_all=np.nan, mape_filt=37.48, corr_all=0.76, w25_all=34.62, w50_all=61.54, w25_filt=42.86, w50_filt=76.19),
        3: dict(mape_all=np.nan, mape_filt=41.39, corr_all=0.51, w25_all=30.77, w50_all=55.77, w25_filt=35.71, w50_filt=66.67),
    },
    "Gemini-Robotics": {
        1: dict(mape_all=np.nan, mape_filt=45.77, corr_all=0.82, w25_all=26.42, w50_all=43.40, w25_filt=32.56, w50_filt=53.49),
        2: dict(mape_all=np.nan, mape_filt=48.48, corr_all=0.83, w25_all=18.87, w50_all=41.51, w25_filt=23.26, w50_filt=51.16),
        3: dict(mape_all=np.nan, mape_filt=46.86, corr_all=0.81, w25_all=22.64, w50_all=49.06, w25_filt=25.58, w50_filt=55.81),
    },
}

# ── ANGLE ────────────────────────────────────────────────────────────────────
angle = {
    "OpenAI": {
        1: dict(mape_all=46.44, mape_filt=14.81, corr_all=0.73, w25_all=72.00, w50_all=87.00, w25_filt=80.00, w50_filt=96.67),
        2: dict(mape_all=27.86, mape_filt=14.83, corr_all=0.81, w25_all=74.00, w50_all=86.00, w25_filt=82.22, w50_filt=95.56),
        3: dict(mape_all=23.02, mape_filt=12.14, corr_all=0.90, w25_all=76.00, w50_all=92.00, w25_filt=84.44, w50_filt=100.00),
    },
    "Gemini": {
        1: dict(mape_all=20.77, mape_filt=10.96, corr_all=0.86, w25_all=78.79, w50_all=94.95, w25_filt=87.64, w50_filt=100.00),
        2: dict(mape_all=25.10, mape_filt=13.04, corr_all=0.83, w25_all=73.00, w50_all=90.00, w25_filt=81.11, w50_filt=98.89),
        3: dict(mape_all=17.11, mape_filt=10.69, corr_all=0.94, w25_all=82.00, w50_all=95.00, w25_filt=91.11, w50_filt=100.00),
    },
    "Gemini-Robotics": {
        1: dict(mape_all=49.67, mape_filt=14.38, corr_all=0.70, w25_all=73.00, w50_all=87.00, w25_filt=81.11, w50_filt=96.67),
        2: dict(mape_all=50.45, mape_filt=14.76, corr_all=0.70, w25_all=74.00, w50_all=87.00, w25_filt=82.22, w50_filt=96.67),
        3: dict(mape_all=24.35, mape_filt=11.68, corr_all=0.84, w25_all=79.00, w50_all=93.00, w25_filt=87.78, w50_filt=100.00),
    },
}

# ── LIQUID VOLUME ────────────────────────────────────────────────────────────
liquid_volume = {
    "OpenAI": {
        1: dict(mape_all=30.34, mape_filt=24.43, corr_all=1.00, w25_all=52.63, w50_all=85.53, w25_filt=60.61, w50_filt=90.91),
        2: dict(mape_all=31.71, mape_filt=26.81, corr_all=1.00, w25_all=46.05, w50_all=81.58, w25_filt=53.03, w50_filt=86.36),
        3: dict(mape_all=33.79, mape_filt=27.60, corr_all=1.00, w25_all=44.74, w50_all=84.21, w25_filt=51.52, w50_filt=89.39),
    },
    "Gemini": {
        1: dict(mape_all=29.12, mape_filt=24.80, corr_all=1.00, w25_all=56.00, w50_all=85.33, w25_filt=61.54, w50_filt=89.23),
        2: dict(mape_all=38.58, mape_filt=21.15, corr_all=1.00, w25_all=58.11, w50_all=86.49, w25_filt=67.19, w50_filt=93.75),
        3: dict(mape_all=26.63, mape_filt=21.77, corr_all=1.00, w25_all=57.89, w50_all=88.16, w25_filt=65.15, w50_filt=92.42),
    },
    "Gemini-Robotics": {
        1: dict(mape_all=23.75, mape_filt=19.27, corr_all=0.41, w25_all=61.84, w50_all=92.11, w25_filt=68.18, w50_filt=95.45),
        2: dict(mape_all=23.98, mape_filt=19.35, corr_all=1.00, w25_all=60.53, w50_all=92.11, w25_filt=66.67, w50_filt=95.45),
        3: dict(mape_all=23.08, mape_filt=18.52, corr_all=0.41, w25_all=68.42, w50_all=89.47, w25_filt=74.24, w50_filt=92.42),
    },
}

# ── FIT (classification) ─────────────────────────────────────────────────────
fit = {
    "OpenAI":           dict(accuracy=27.43, precision=54.43, recall=17.00, f1=25.90),
    "Gemini":           dict(accuracy=27.43, precision=57.14, recall=25.86, f1=35.60),
    "Gemini-Robotics":  dict(accuracy=27.43, precision=67.09, recall=19.41, f1=30.11),
}

fit_per_batch = {
    "OpenAI": {
        1: dict(accuracy=27.43, precision=53.57, recall=17.86, f1=26.79),
        2: dict(accuracy=27.43, precision=53.57, recall=17.86, f1=26.79),
        3: dict(accuracy=27.43, precision=56.52, recall=15.29, f1=24.07),
    },
    "Gemini": {
        1: dict(accuracy=27.43, precision=53.85, recall=24.71, f1=33.87),
        2: dict(accuracy=27.43, precision=59.52, recall=27.78, f1=37.88),
        3: dict(accuracy=27.43, precision=57.89, recall=25.00, f1=34.92),
    },
    "Gemini-Robotics": {
        1: dict(accuracy=27.43, precision=68.97, recall=21.51, f1=32.79),
        2: dict(accuracy=27.43, precision=65.38, recall=18.89, f1=29.31),
        3: dict(accuracy=27.43, precision=66.67, recall=17.78, f1=28.07),
    },
}

# ── Helpers ──────────────────────────────────────────────────────────────────
MODELS = ["OpenAI", "Gemini", "Gemini-Robotics"]
BATCHES = [1, 2, 3]
COLORS = {"OpenAI": "#4C72B0", "Gemini": "#DD8452", "Gemini-Robotics": "#55A868"}
BATCH_COLORS = ["#5B9BD5", "#ED7D31", "#70AD47"]

model_patches = [mpatches.Patch(color=COLORS[m], label=m) for m in MODELS]

categories_cont = {
    "Weight":       (weight,        True),   # (data, has_valid_full_mape)
    "Angle":        (angle,         True),
    "Stability":    (stability,     False),  # full MAPE is undefined (GT=0 division)
    "Liquid Volume":(liquid_volume, True),
}

# ── helper: draw 6 bars per batch (3 full faded + 3 filtered solid) ──────────
BW = 0.10          # individual bar width
GAP = 0.06         # gap between the full group and the filtered group
GROUP_W = 3 * BW   # width of one model-trio group


def draw_mape_bars(ax, cat_data, has_full, key_full="mape_all", key_filt="mape_filt",
                   ylabel="MAPE (%)"):
    batch_x = np.arange(len(BATCHES), dtype=float)

    for b_idx, batch in enumerate(BATCHES):
        for m_idx, model in enumerate(MODELS):
            color = COLORS[model]

            # full bar (faded / hatched) — left sub-group
            full_val = cat_data[model][batch][key_full]
            if has_full and not np.isnan(full_val):
                fx = batch_x[b_idx] - GROUP_W - GAP/2 + m_idx * BW + BW/2
                ax.bar(fx, full_val, BW, color=color, alpha=0.30,
                       edgecolor=color, linewidth=0.8, hatch='//')
                ax.text(fx, full_val + 0.4, f"{full_val:.1f}",
                        ha='center', va='bottom', fontsize=6, color='#666')

            # filtered bar (solid) — right sub-group
            fv = cat_data[model][batch][key_filt]
            offset = 0 if has_full else -GROUP_W/2   # centre when no full bars
            fx2 = batch_x[b_idx] + offset + GAP/2 + m_idx * BW + BW/2
            ax.bar(fx2, fv, BW, color=color, alpha=0.88,
                   edgecolor='black', linewidth=0.6)
            ax.text(fx2, fv + 0.4, f"{fv:.1f}",
                    ha='center', va='bottom', fontsize=6.5)

    ax.set_xticks(batch_x)
    ax.set_xticklabels([f"Batch {b}" for b in BATCHES], fontsize=9)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.22)
    ax.grid(axis='y', linestyle='--', alpha=0.45)
    ax.spines[['top', 'right']].set_visible(False)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — MAPE: Full vs Filtered, per batch, all 4 continuous categories
# ═══════════════════════════════════════════════════════════════════════════════
fig1, axes1 = plt.subplots(2, 2, figsize=(18, 12))
fig1.suptitle("MAPE: Full Data (hatched) vs. −Worst 10/batch (solid)  |  per batch, per model",
              fontsize=13, fontweight='bold')

for ax, (cat_name, (cat_data, has_full)) in zip(axes1.flat, categories_cont.items()):
    draw_mape_bars(ax, cat_data, has_full)
    ax.set_title(cat_name + ("" if has_full else "\n(full MAPE undefined — GT=0 cases)"),
                 fontweight='bold')

# shared legend: model colours
fig1.legend(handles=model_patches, loc='lower center', ncol=3, fontsize=10,
            frameon=True, title="Model", bbox_to_anchor=(0.5, 0.01))
# variant legend
v_full = mpatches.Patch(facecolor='gray', alpha=0.3, edgecolor='gray',
                         hatch='//', label='Full data')
v_filt = mpatches.Patch(facecolor='gray', alpha=0.88, edgecolor='black',
                         label='−Worst 10/batch')
fig1.legend(handles=[v_full, v_filt], loc='lower center', ncol=2, fontsize=9,
            frameon=True, bbox_to_anchor=(0.5, 0.055))
fig1.tight_layout(rect=[0, 0.10, 1, 1])
fig1.savefig(RESULTS_DIR / "metrics_mape_per_batch.png", dpi=150, bbox_inches='tight')
print("Saved metrics_mape_per_batch.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — Within ±25% and ±50%, per batch, all 4 continuous categories
# ═══════════════════════════════════════════════════════════════════════════════
fig2, axes2 = plt.subplots(2, 2, figsize=(18, 12))
fig2.suptitle("Accuracy Windows: Within ±25% (hatched) and ±50% (solid)  |  per batch, per model\n(full data)",
              fontsize=13, fontweight='bold')

for ax, (cat_name, (cat_data, _)) in zip(axes2.flat, categories_cont.items()):
    draw_mape_bars(ax, cat_data, has_full=True,
                   key_full="w25_all", key_filt="w50_all",
                   ylabel="% Samples")
    ax.set_title(cat_name, fontweight='bold')
    ax.axhline(50, color='red', linestyle=':', linewidth=0.9, alpha=0.55, label='50% line')
    ax.set_ylim(0, 115)

v_w25 = mpatches.Patch(facecolor='gray', alpha=0.3, edgecolor='gray', hatch='//', label='Within ±25%')
v_w50 = mpatches.Patch(facecolor='gray', alpha=0.88, edgecolor='black', label='Within ±50%')
fig2.legend(handles=model_patches, loc='lower center', ncol=3, fontsize=10,
            frameon=True, title="Model", bbox_to_anchor=(0.5, 0.01))
fig2.legend(handles=[v_w25, v_w50], loc='lower center', ncol=2, fontsize=9,
            frameon=True, bbox_to_anchor=(0.5, 0.055))
fig2.tight_layout(rect=[0, 0.10, 1, 1])
fig2.savefig(RESULTS_DIR / "metrics_accuracy_windows_per_batch.png", dpi=150, bbox_inches='tight')
print("Saved metrics_accuracy_windows_per_batch.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 3 — FIT classification metrics (per batch breakdown)
# ═══════════════════════════════════════════════════════════════════════════════
fig3, axes3 = plt.subplots(1, 3, figsize=(16, 5))
fig3.suptitle("Fit Classification Metrics (Boolean: does it fit?)", fontsize=14, fontweight='bold')

metrics_list  = ["accuracy", "precision", "recall", "f1"]
metric_labels = ["Accuracy", "Precision", "Recall", "F1 Score"]
width = 0.25

# One subplot per batch
for ax, batch in zip(axes3, BATCHES):
    x = np.arange(len(metrics_list))
    for i, model in enumerate(MODELS):
        vals = [fit_per_batch[model][batch][m] for m in metrics_list]
        bars = ax.bar(x + (i - 1) * width, vals, width,
                      label=model, color=COLORS[model], alpha=0.85,
                      edgecolor='black', linewidth=0.6)
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
                    f"{val:.1f}", ha='center', va='bottom', fontsize=7)
    ax.set_title(f"Batch {batch}", fontweight='bold')
    ax.set_ylabel("Score (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(metric_labels, fontsize=9)
    ax.set_ylim(0, 80)
    ax.legend(fontsize=8)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.spines[['top', 'right']].set_visible(False)

fig3.tight_layout()
fig3.savefig(RESULTS_DIR / "metrics_fit_classification.png", dpi=150, bbox_inches='tight')
print("Saved metrics_fit_classification.png")

print("\nAll plots saved to:", RESULTS_DIR)
