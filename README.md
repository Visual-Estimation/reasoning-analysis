# Visual Estimation Benchmark — LLM Perception Evaluation

Benchmark evaluating three large vision-language models on physical property estimation from images. Models are tested across **5 perception categories** using **3 independent batches** (same images, different inference runs).

**Models evaluated:** OpenAI GPT-4o · Gemini 1.5 Pro · Gemini-Robotics

---

## Table of Contents

1. [What This Measures](#what-this-measures)
2. [Repository Structure](#repository-structure)
3. [Data](#data)
4. [Results](#results)
5. [Plots](#plots)
6. [Scripts](#scripts)
7. [How to Run](#how-to-run)
8. [Quick Results Reference](#quick-results-reference)

> **Full analysis → [ANALYSIS.md](ANALYSIS.md)**
> All detailed findings, per-model failure mode analysis, failure mode taxonomy, and research-paper-level discussion are in `ANALYSIS.md`. The sections below are a quick navigation reference only.

---

## What This Measures

Five physical perception tasks, each requiring the model to estimate a quantity from a marked image:

| Category | Task Type | Unit | Images |
|---|---|---|---|
| **weight** | Regression | grams | 112 |
| **stability** | Regression | varies (cm, degrees, mL, count) | 54 |
| **angle** | Regression | degrees | 100 |
| **liquid_volume** | Regression | mL | 76 |
| **fit** | Binary classification | YES/NO | 113 |

Each task was run **3 times** (batch 1, 2, 3) on the same images to measure consistency. Metrics are computed both over the **full dataset** and with the **worst 10 cases per batch removed** to assess impact of outliers.

---

## Repository Structure

```
ve/
├── data/                          # Raw model outputs and ground truth
├── results/                       # Analysis outputs per category + summary plots
│   ├── weight/
│   ├── stability/
│   ├── angle/
│   ├── fit/
│   ├── liquid_volume/
│   ├── metrics_mape_per_batch.png
│   ├── metrics_accuracy_windows_per_batch.png
│   └── metrics_fit_classification.png
├── scripts/                       # Analysis and plotting scripts
├── cache/                         # Cached intermediate computations (pkl)
└── README.md
```

---

## Data

### `data/groundtruth.csv`
Ground truth values for all 457 images.
- Columns: `filename`, `type` (category), `custom_prompt` (the question asked), `shorthand_notes` (GT value as text)

### `data/batch_1.csv`, `batch_2.csv`, `batch_3.csv`
Model predictions — one row per image per batch (658 rows each, includes base + blur/pov variants).
- Columns: `filename`, `openai_num`, `openai_bool`, `openai_reasoning`, `openai_reasoning_tokens`, `gemini_num`, `gemini_bool`, `gemini_reasoning`, `gemini-robotics_num`, `gemini-robotics_bool`, `gemini-robotics_reasoning`
- `_num`: numeric prediction (regression tasks)
- `_bool`: boolean prediction (fit classification)
- `_reasoning`: full chain-of-thought text from the model

### `data/gemini_robotics_reasoning_traces_batch_{1,2,3}.csv` / `.json`
Detailed reasoning traces specifically for Gemini-Robotics, in both CSV and JSON format.
- Columns: `filename`, `prompt`, `reasoning_trace`, `predicted_value`

### `data/small-model-outputs.csv`
Outputs from smaller/alternative models (Qwen, Gemma-4) on the same images. Same column structure as batch files.

### `data/prompt_groups.json`
Groups images by the question prompt type — useful for stratified analysis.

---

## Results

Each category subdirectory contains:

### Continuous categories (weight, stability, angle, liquid_volume)

| File | Contents |
|---|---|
| `*_metrics_comparison_all_models.txt` | Primary metrics table. Per-batch breakdown for all 3 models. Each batch shows: MAPE (full + without worst 10), MAE, RMSE, Median AE, Within ±10%/±25%/±50%, Overestimate %, Bias, Correlation. |
| `*_worst_cases_reasoning_all_models.md` | Top 10 worst-error images per batch per model, with ground truth, prediction, error ratio, and full model reasoning trace. |

**Additional files in `results/weight/` only** (most developed category):

| File | Contents |
|---|---|
| `metrics_comparison_with_without_worst.txt` | OpenAI-specific metrics with/without worst 10 |
| `gemini_models_metrics_comparison.txt` | Gemini + Gemini-Robotics comparison |
| `GEMINI_ANALYSIS_SUMMARY.md` | High-level narrative summary of Gemini model weight analysis — good starting point for understanding weight results |
| `gemini_models_worst_cases_reasoning.md` | Worst cases + reasoning for both Gemini models |
| `worst_cases_reasoning_analysis.md` | Worst cases + reasoning for OpenAI |
| `weight_analysis.ipynb` | Exploratory notebook |
| `weight_analysis_visualizations.png` | Visualizations from the notebook |
| `failure_mode_analysis.png` | Failure mode breakdown chart |

### Fit category

| File | Contents |
|---|---|
| `fit_metrics_comparison_all_models.txt` | Accuracy, Precision, Recall, F1 per batch per model + confusion matrix |
| `fit_worst_misclassifications.md` | False positives (predicted YES, actually NO) and false negatives (predicted NO, actually YES) with full reasoning traces |

> **Note on stability MAPE**: Full MAPE values in stability are astronomically large (∼10¹¹%) because some ground truth values are 0, causing division-by-zero. **Always use the "WITHOUT Worst 10" MAPE for stability comparisons**, or compare MAE/Median AE instead.

---

## Plots

All plots saved to `results/`:

### `metrics_mape_per_batch.png`
2×2 grid covering weight, angle, stability, liquid_volume. X-axis = batch (1/2/3). For each batch, shows 3 model pairs:
- **Faded hatched bar** = full MAPE (all data)
- **Solid bar** = filtered MAPE (worst 10 removed)
- Stability panel shows filtered only (full MAPE is meaningless due to GT=0 division)

### `metrics_accuracy_windows_per_batch.png`
Same 2×2 layout. Shows percentage of predictions landing within:
- **Hatched bar** = Within ±25% of GT
- **Solid bar** = Within ±50% of GT

### `metrics_fit_classification.png`
1×3 grid (one subplot per batch). Shows Accuracy, Precision, Recall, F1 for all 3 models side by side.

---

## Scripts

| Script | What it does |
|---|---|
| `plot_all_metrics.py` | **Generates the 3 summary plots** from hardcoded data. Run this to regenerate plots. |
| `metrics_comparison.py` | Computes all metrics (MAPE, MAE, correlation, etc.) with/without worst N cases. Outputs the `*_metrics_comparison_all_models.txt` files. |
| `find_worst_all_categories.py` | Identifies the worst N cases per batch per model across all categories. Saves results to `cache/`. |
| `find_worst_gemini_models.py` | Same as above but specifically for Gemini vs Gemini-Robotics comparison. |
| `extract_all_categories_analysis.py` | Builds the `*_worst_cases_reasoning_all_models.md` files by pulling reasoning traces for worst cases. |
| `extract_gemini_analysis.py` | Same extraction but for Gemini-specific weight analysis files. |
| `analyze_fit_category.py` | Computes fit classification metrics (accuracy, precision, recall, F1, confusion matrix) and generates `fit_metrics_comparison_all_models.txt`. |
| `retrieve_reasoning_traces.py` | Fetches and formats reasoning traces from raw batch CSV files. |
| `worst_cases_reasoning_reader.py` | Utility: reads and pretty-prints worst case reasoning from cache. |
| `inspect_robotics_output.py` | Diagnostic: inspects Gemini-Robotics output format and structure. |

---

## How to Run

### Environment setup (Linux / WSL2)

The repo contains a Windows-created venv (`.venv/`) that cannot run on Linux. Use the Linux venv instead:

```bash
# Create Linux-compatible venv (only needed once)
uv venv .venv-linux --python 3.12
uv pip install --python .venv-linux matplotlib numpy pandas

# Activate
source .venv-linux/bin/activate
```

### Regenerate plots

```bash
source .venv-linux/bin/activate
python scripts/plot_all_metrics.py
# Outputs: results/metrics_mape_per_batch.png
#          results/metrics_accuracy_windows_per_batch.png
#          results/metrics_fit_classification.png
```

### Recompute metrics from raw data

```bash
python scripts/metrics_comparison.py          # all categories
python scripts/analyze_fit_category.py        # fit only
```

---

## Quick Results Reference

### MAPE (filtered — worst 10 per batch removed)

| Category | OpenAI B1/B2/B3 | Gemini B1/B2/B3 | Gemini-Robotics B1/B2/B3 |
|---|---|---|---|
| Weight | 35.70% / 38.42% / 36.75% | 29.54% / 29.94% / 28.94% | 28.99% / 29.72% / 30.14% |
| Stability† | 37.41% / 41.32% / 35.89% | 41.93% / 37.48% / 41.39% | 45.77% / 48.48% / 46.86% |
| Angle | 14.81% / 14.83% / 12.14% | 10.96% / 13.04% / 10.69% | 14.38% / 14.76% / 11.68% |
| Liquid Volume | 24.43% / 26.81% / 27.60% | 24.80% / 21.15% / 21.77% | 19.27% / 19.35% / 18.52% |

†Stability full MAPE is undefined (GT=0 division by zero). Filtered only.

### Fit Classification

| Model | Precision | Recall | F1 |
|---|---|---|---|
| OpenAI | 54.43% | 17.00% | 25.90% |
| Gemini | 57.14% | 25.86% | **35.60%** |
| Gemini-Robotics | **67.09%** | 19.41% | 30.11% |

### Five headline findings

1. **Gemini-Robotics is near-deterministic** — produces identical predictions for the same image across all 3 batches (e.g., V-weight-image50 = exactly 13.47× overestimate in all 3 runs). OpenAI shows high cross-batch variance on the same images.
2. **Outlier impact is asymmetric** — removing 10 worst cases per batch cuts OpenAI weight MAPE by 66% (98%→33%); same operation on Gemini cuts only 44%. OpenAI errors are dominated by a small number of extreme cases; Gemini errors are more uniformly distributed.
3. **Gemini-Robotics liquid volume correlation anomaly** — r=0.41 in batches 1 and 3 (vs r=1.00 for all other model/batch combinations) despite having the best MAPE in this category.
4. **Gemini-Robotics has a 90° instability threshold bug** — systematically predicts 90° as the angle at which any leaning structure becomes unstable, regardless of actual geometry, in all 3 batches.
5. **All three models share liquid volume anchoring failures** — same images produce the same wrong predictions across all models: 500mL beaker predicted as 1000mL, 50mL beaker as 100mL, 30oz tumbler as 40oz.

**For full analysis, failure mode taxonomy, and per-model reasoning trace breakdowns → [ANALYSIS.md](ANALYSIS.md)**
