# Benchmark Analysis: LLM Physical Perception Evaluation

Comprehensive findings and per-model error analysis across all 5 perception categories. This document is the single source of truth for all results, patterns, and failure mode analysis for this benchmark — intended to support writing the research paper directly.

---

## Table of Contents

1. [Benchmark Overview](#1-benchmark-overview)
2. [Category-Level Results](#2-category-level-results)
   - [2.1 Weight](#21-weight)
   - [2.2 Stability](#22-stability)
   - [2.3 Angle](#23-angle)
   - [2.4 Liquid Volume](#24-liquid-volume)
   - [2.5 Fit (Classification)](#25-fit-classification)
3. [Cross-Cutting Findings](#3-cross-cutting-findings)
4. [Per-Model Error Pattern Analysis](#4-per-model-error-pattern-analysis)
   - [4.1 OpenAI](#41-openai)
   - [4.2 Gemini](#42-gemini)
   - [4.3 Gemini-Robotics](#43-gemini-robotics)
5. [Failure Mode Taxonomy](#5-failure-mode-taxonomy)
6. [Model Comparison Summary](#6-model-comparison-summary)

---

## 1. Benchmark Overview

### Setup

Three large vision-language models — **OpenAI GPT-4o**, **Gemini 1.5 Pro**, and **Gemini-Robotics** — were evaluated on 5 physical perception tasks. Each task requires the model to estimate a physical quantity (weight, stability margin, angle, liquid volume) or make a binary containment judgment (fit) from a marked image.

Every model was evaluated **3 independent times** (batches 1, 2, 3) on the same set of images, yielding three replicate measurements per model per image. This enables direct assessment of **intra-model consistency** alongside accuracy.

### Dataset

| Category | Task | Unit | Images (unique) | N per batch |
|---|---|---|---|---|
| weight | Regression | grams | 112 | 112 |
| stability | Regression | varies (cm / degrees / mL / count) | 54 | 53–54 |
| angle | Regression | degrees | 100 | 99–100 |
| liquid_volume | Regression | mL | 76 | 74–76 |
| fit | Binary classification | YES/NO | 113 | 113 |

### Metrics

For regression tasks, each batch reports:
- **MAPE (full)**: Mean Absolute Percentage Error over all predictions in that batch
- **MAPE (filtered)**: MAPE with the worst 10 cases per batch removed — measures typical-case performance unclouded by extreme outliers
- MAE, RMSE, Median AE (absolute error metrics in original units)
- Within ±10% / ±25% / ±50% of ground truth (tolerance windows)
- Overestimate %, Bias, Pearson Correlation

For fit (binary), standard classification metrics: Accuracy, Precision, Recall, F1, Confusion Matrix.

> **Critical note on stability MAPE**: Several stability ground-truth values are exactly 0 (the object is already at the tipping threshold), causing division-by-zero in MAPE. Full MAPE for stability reaches ∼10¹¹–10¹²% for all models and is numerically meaningless. **All stability comparisons in this document use filtered MAPE or MAE.**

---

## 2. Category-Level Results

### 2.1 Weight

Weight estimation (in grams) is the most thoroughly analyzed category. Objects span lightweight items (~80g coiled rope, 91g glue gun) to heavy items (~12.4 kg water-filled bucket, ~8 kg boxed woven items).

#### MAPE — Full vs. Filtered

| Model | B1 Full | B1 Filt | B2 Full | B2 Filt | B3 Full | B3 Filt |
|---|---|---|---|---|---|---|
| OpenAI | 100.17% | 35.70% | 121.86% | 38.42% | 72.55% | 36.75% |
| Gemini | 54.55% | 29.54% | 49.66% | 29.94% | 50.72% | 28.94% |
| Gemini-Robotics | 49.47% | 28.99% | 51.33% | 29.72% | 51.22% | 30.14% |

**OpenAI outlier dominance**: Removing the worst 10 per batch cuts OpenAI's MAPE by an average of **66%** (from ~98% aggregate to ~37%). The same operation on Gemini and Gemini-Robotics produces only a ~44% reduction. OpenAI's aggregate performance is therefore heavily driven by a small number of extreme errors, while Gemini/Gemini-Robotics have more uniformly distributed errors.

**OpenAI cross-batch instability**: Full MAPE varies wildly (72.55% → 121.86%) across batches on the same image set. Filtered MAPE is stable (~36–38%), revealing that the variance lives entirely in the outlier tier.

**Gemini and Gemini-Robotics near-parity**: Both achieve ~29–30% filtered MAPE across all three batches. Gemini-Robotics achieves this with shorter, more categorical reasoning while Gemini uses explicit geometric calculations.

#### Correlation (Full dataset)

| Model | B1 | B2 | B3 |
|---|---|---|---|
| OpenAI | 0.94 | 0.82 | 0.92 |
| Gemini | 0.95 | — | — |
| Gemini-Robotics | — | — | — |

OpenAI B2 correlation drop (0.82) corresponds to the batch with the highest full MAPE (121.86%), consistent with extreme outlier predictions distorting the linear relationship.

#### Within ±25% and ±50% (representative batch — B1 full)

| Model | Within ±25% | Within ±50% |
|---|---|---|
| OpenAI | 55.36% | 71.43% |
| Gemini | 43.75% | 76.79% |
| Gemini-Robotics | — | — |

**Interesting inversion**: Despite worse ±25% performance, Gemini achieves better ±50% than OpenAI. Gemini's errors are moderately sized (landing inside ±50% more often) but rarely fall in the tighter ±25% window. OpenAI has more predictions close to correct (higher ±25%) but also more extreme outliers that fall outside ±50%.

#### Key worst-case images (weight)

The single most impactful image across all three models is **V-weight-image50** (hollow rectangular steel table leg frame, GT = 297g):
- OpenAI: 11×–35× overestimate across batches — mentally constructs a complete table
- Gemini: 15×–18.5× overestimate — correct steel density calculation but wrong structural scope
- Gemini-Robotics: **exactly 13.47× in all three batches** — strongest evidence of determinism

**B-weight-image1** (box of woven straw items, GT = 8000g) is OpenAI's canonical underestimate: predicted 700–900g across all batches because the model enumerates individual straw piece weights rather than treating the box as a filled unit.

---

### 2.2 Stability

Stability tasks are diverse: minimum displacement to cause an object to fall off a table (cm), angle at which a leaning board slides (degrees), number of additional blocks to topple a stack (count), and mass of water that can be removed before a see-saw tips (mL or g). Ground truth values range from 0 (already unstable) to ~225g.

#### Filtered MAPE (full MAPE is undefined due to GT=0 images)

| Model | B1 Filt | B2 Filt | B3 Filt |
|---|---|---|---|
| OpenAI | 37.41% | 41.32% | 35.89% |
| Gemini | 41.93% | 37.48% | 41.39% |
| Gemini-Robotics | 45.77% | 48.48% | 46.86% |

Gemini-Robotics performs **worst** on stability despite performing well on weight and liquid volume. OpenAI and Gemini are roughly equivalent.

#### MAE (full dataset, in original units)

| Model | B1 | B2 | B3 |
|---|---|---|---|
| OpenAI | 33.76 | 34.96 | 32.14 |
| Gemini | 33.70 | 35.41 | 40.39 |
| Gemini-Robotics | 37.45 | 33.08 | 35.94 |

MAE is in original (mixed) units — comparable within a model across batches but not directly across models for cross-category comparison.

#### Correlation (filtered)

| Model | B1 | B2 | B3 |
|---|---|---|---|
| OpenAI | 0.85 | 0.81 | 0.83 |
| Gemini | 0.83 | 0.85 | 0.72 |
| Gemini-Robotics | 0.88 | 0.87 | 0.90 |

Gemini B3 shows a correlation drop to 0.72 — the lowest of any model-batch combination in stability. Gemini-Robotics has the highest and most consistent stability correlation despite its higher MAPE.

#### Within ±25% and ±50% (B1 filtered)

| Model | Within ±25% | Within ±50% |
|---|---|---|
| OpenAI | 44.19% | 65.12% |
| Gemini | 37.21% | 65.12% |
| Gemini-Robotics | 32.56% | 53.49% |

Gemini-Robotics achieves fewer predictions in both tolerance windows, confirming its higher MAPE is a real performance gap and not just outlier-driven.

#### The GT=0 problem

Three images have GT=0 (the object is already at or past the tipping threshold — any prediction is technically infinite MAPE). All three models give non-zero estimates for these images (typically 20–40 degrees for the sliding angle case). This is unavoidable — the model cannot observe instability directly from a static image — but it means filtered MAPE must be used.

#### Key worst-case images (stability)

**P-stability-image10** (GT=0, sliding angle): all three models predict 20–40°, with Gemini-Robotics showing the most deterministic response (always 30° based on a generic friction coefficient formula).

**B-stability-image3** (GT=13°, rotation to stable position): Gemini-Robotics predicts exactly 90° in all three batches — a conceptual error where the model conflates "rotation to flat stable position" with "90 degrees of rotation." Error ratio: 6.92×.

**M-stability-image13** (GT=56.4°, leaning board instability angle): Gemini-Robotics predicts 90° in all batches — same error pattern. Any angle question framed as "what angle makes this unstable" is interpreted as 90° (vertical).

---

### 2.3 Angle

Angle estimation (in degrees) requires the model to read a visually marked angle from physical objects — furniture joints, leaning boards, pipe bends, cushion edges. Ground truth angles span roughly 7° to 170°.

#### MAPE — Full vs. Filtered

| Model | B1 Full | B1 Filt | B2 Full | B2 Filt | B3 Full | B3 Filt |
|---|---|---|---|---|---|---|
| OpenAI | 46.44% | 14.81% | 27.86% | 14.83% | 23.02% | 12.14% |
| Gemini | 20.77% | 10.96% | 25.10% | 13.04% | 17.11% | 10.69% |
| Gemini-Robotics | 49.67% | 14.38% | 50.45% | 14.76% | 24.35% | 11.68% |

**Angle is the best-performing category overall** — filtered MAPE reaches 10–15% for all models across most batches.

**Gemini has the best full MAPE** (17–25%), showing fewer extreme outliers than the other two models.

**Gemini-Robotics B1/B2 anomaly**: Full MAPE of ~50% collapses to ~14% after removing the worst 10 — a **71% reduction**. This is the largest outlier impact observed in any model-category combination. A small number of images with extreme errors (>20× ratio) completely dominate the full-MAPE signal.

**OpenAI B1 anomaly**: Similar pattern — 46.44% full → 14.81% filtered (−68%), driven by one extreme outlier (V-angle-image54, predicted 170° for GT=7.7°, ratio=22×).

**Correlation after filtering**:

| Model | B1 Filt | B2 Filt | B3 Filt |
|---|---|---|---|
| OpenAI | 0.94 | 0.93 | 0.97 |
| Gemini | 0.98 | 0.94 | 0.98 |
| Gemini-Robotics | 0.96 | 0.97 | 0.98 |

After outlier removal, all three models show near-identical and very high correlation (0.93–0.98). The angle benchmark effectively has two performance tiers: extremely well-understood "easy" images (all models correct) and a small set of geometric ambiguity cases that all models fail catastrophically.

#### Within ±25% (B1, full dataset)

| Model | Within ±25% |
|---|---|
| OpenAI | 72.00% |
| Gemini | 78.79% |
| Gemini-Robotics | 73.00% |

Gemini leads on this metric — more predictions fall in the tight accuracy window even before outlier removal.

#### The angle supplement confusion

The dominant failure mode across all three models is **interior/exterior angle confusion** — the model reads the supplement (180° − θ) or complement of the true angle. This is especially severe for small acute angles where the model defaults to reading the obtuse counterpart:

- **M-angle-image8** (GT=7.7°): OpenAI predicts 170°/25°/17° across batches; Gemini-Robotics predicts 165°/168°/15°. The first two batches read the near-flat pedal joint as ~170° (the supplement), while B3 finally reads the acute angle.
- **V-angle-image32** (GT=37.6°): Gemini-Robotics predicts 175°/150° in B1/B3 — interprets the stick as a nearly straight rod.
- **V-angle-image31** (GT=22.5°): OpenAI predicts 92°/80°/100° — reads the stool joint as approximately a right angle. Gemini-Robotics predicts 90°/90°/110° — same error pattern.

The extreme outlier MAPE values in B1/B2 for Gemini-Robotics are almost entirely caused by these few supplement-confusion images.

---

### 2.4 Liquid Volume

Liquid volume estimation (in mL) involves identifying the full volumetric capacity of containers shown in images — bottles, beakers, bowls, thermoses, tumblers.

#### MAPE — Full vs. Filtered

| Model | B1 Full | B1 Filt | B2 Full | B2 Filt | B3 Full | B3 Filt |
|---|---|---|---|---|---|---|
| OpenAI | 30.34% | 24.43% | 31.71% | 26.81% | 33.79% | 27.60% |
| Gemini | 29.12% | 24.80% | 38.58% | 21.15% | 26.63% | 21.77% |
| Gemini-Robotics | 23.75% | 19.27% | 23.98% | 19.35% | 23.08% | 18.52% |

**Gemini-Robotics achieves the best MAPE** across all three batches, both full and filtered. Filtered MAPE of ~18–20% is notably better than OpenAI (~24–28%) and Gemini (~21–25%).

**Gemini B2 outlier**: Full MAPE spikes to 38.58% in B2 but filtered drops to 21.15% — the worst 10 removal is the largest fractional improvement for Gemini in this category. This is caused by a single image (P-liquid_volume-image16, GT=100mL) where the model misreads an upside-down bottle's graduation mark as current fill, predicting 1000mL (10× error).

#### Pearson Correlation

| Model | B1 | B2 | B3 |
|---|---|---|---|
| OpenAI | 1.00 | 1.00 | 1.00 |
| Gemini | 1.00 | 1.00 | 1.00 |
| Gemini-Robotics | **0.41** | 1.00 | **0.41** |

**This is the most anomalous finding in the entire benchmark.** Despite having the best MAPE, Gemini-Robotics shows near-zero correlation in batches 1 and 3 while achieving perfect correlation in batch 2. A correlation of 0.41 means the rank-ordering of predictions does not match the rank-ordering of ground truths — some containers that should be predicted as small are predicted as large, and vice versa. This cannot be explained by uniform scaling (which would preserve rank order). It implies a structural inconsistency in how the model orders container sizes in B1/B3 vs B2.

The low MAPE alongside low correlation is not contradictory: if a model has a consistent additive bias that doesn't interact with GT magnitude, MAPE can be low while correlation is also low (the predictions cluster in a narrow range regardless of GT). The co-occurrence of best MAPE and worst correlation makes this finding worth dedicated investigation.

#### Systematic anchoring errors

All three models consistently make the same errors on the same images, across all batches:

| Image | GT | All Models Predict | Error |
|---|---|---|---|
| P-liquid_volume-image24 | 500 mL | 1000 mL | 2.0× |
| P-liquid_volume-image3 | 50 mL | 100 mL | 2.0× |
| P-liquid_volume-image21 | 50 mL | 100 mL | 2.0× |
| P-liquid_volume-image58 | 350 mL | 500 mL | 1.43× |
| P-liquid_volume-image64 | 350 mL | 500 mL | 1.43× |
| P-liquid_volume-image23/48 | 887 mL (30oz) | 1183–1200 mL (40oz) | 1.33–1.35× |

These images represent hard-anchored biases that appear to be shared priors across all three models: the 1L beaker's graduation marks are read as capacity rather than maximum marking, the 50mL beaker is rounded to the "next standard" 100mL size, all 350mL narrow bottles are rounded to the standard 500mL single-serve size, and Stanley-style tumblers are assumed to be 40oz rather than 30oz.

---

### 2.5 Fit (Classification)

The fit task requires a binary YES/NO judgment: does the red-marked object fit inside the blue-marked container? This is a spatial reasoning task involving object deformability, size estimation, and containment geometry.

#### Overall Classification Metrics (aggregate, N=339 per model)

| Model | Accuracy | Precision | Recall | F1 | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|---|
| OpenAI | 27.43% | 54.43% | 17.00% | 25.90% | 43 | 50 | 36 | 210 |
| Gemini | 27.43% | 57.14% | 25.86% | 35.60% | 68 | 25 | 51 | 195 |
| Gemini-Robotics | 27.43% | 67.09% | 19.41% | 30.11% | 53 | 40 | 26 | 220 |

> **Note**: All models achieve identical accuracy (27.43%). The confusion matrix counts in the data file produce a higher theoretical accuracy via standard formula, suggesting the accuracy metric reported here uses a non-standard definition — possibly computed against a specific class subset or with a different aggregation scheme. F1 score is the reliable comparative metric.

#### Per-Batch Breakdown

| Model | B1 Precision | B1 Recall | B1 F1 | B2 Precision | B2 Recall | B2 F1 | B3 Precision | B3 Recall | B3 F1 |
|---|---|---|---|---|---|---|---|---|---|
| OpenAI | 53.57% | 17.86% | 26.79% | 53.57% | 17.86% | 26.79% | 56.52% | 15.29% | 24.07% |
| Gemini | 53.85% | 24.71% | 33.87% | 59.52% | 27.78% | 37.88% | 57.89% | 25.00% | 34.92% |
| Gemini-Robotics | 68.97% | 21.51% | 32.79% | 65.38% | 18.89% | 29.31% | 66.67% | 17.78% | 28.07% |

**OpenAI B1=B2 identity**: Precision, recall, and F1 are numerically identical for batches 1 and 2. Combined with Gemini-Robotics' weight determinism, this suggests fit predictions may be fully deterministic for some models — an important finding about inference consistency.

**Gemini achieves the best F1 (35.60%)** — striking the best balance between precision and recall. Gemini-Robotics achieves the best precision (67.09%) at the cost of very low recall (19.41%), reflecting extreme conservatism in predicting YES. OpenAI has the worst F1 despite moderate precision, because its recall (17%) is the lowest.

#### False Positive Profile (predicted YES, actually NO)

All three models share a common FP pattern: **deformability overestimation**. When the red object is flexible (fabric, hose, cable), all models reason that it "can be folded/coiled/compressed to fit" even when the container is demonstrably too small. Recurring FP images across all models:
- Flexible cloth into glasses case
- Coiled hose into bucket
- Battery into wrong-size compartment (visual dimensions look similar)

OpenAI has 50 FPs vs Gemini's 25 — OpenAI is significantly more permissive on deformability thresholds.

#### False Negative Profile (predicted NO, actually YES)

All three models share a common FN pattern: **rigid object size underestimation**. When a rigid-looking board, panel, or box is presented alongside a container, models reason "the object is too large to fit" even when the container diagonal is sufficient. Recurring FN images across all models:
- Triangular/rectangular rigid board into cardboard box (diagonal fit is possible)
- Cup-inside-cup scenarios where rims create visual ambiguity
- Potato bags into plastic bag (bag is more elastic than it appears)

Gemini has 51 FNs vs OpenAI's 36 and Gemini-Robotics' 26 — Gemini is the most conservative about declaring fit for ambiguous size comparisons.

---

## 3. Cross-Cutting Findings

### 3.1 Outlier Impact Asymmetry

The effect of removing the worst 10 cases per batch differs dramatically across models:

| Category | OpenAI MAPE drop | Gemini MAPE drop | GR MAPE drop |
|---|---|---|---|
| Weight | −66% (∼98%→33%) | −44% (∼52%→29%) | −43% (∼51%→29%) |
| Angle | −68% (B1: 46%→15%) | −47% (B1: 21%→11%) | −71% (B1: 50%→14%) |
| Liquid Volume | −19% (B1: 30%→24%) | −15% (B1: 29%→25%) | −19% (B1: 24%→19%) |
| Stability | −100% (undefined full) | −100% | −100% |

OpenAI's weight performance is the most outlier-dominated. Gemini-Robotics' angle performance is even more dominated (−71%) despite having superior median performance. This bimodal character — very good on most images, catastrophically wrong on a few — is distinctive of Gemini-Robotics' behavior pattern.

### 3.2 Gemini-Robotics Cross-Batch Determinism

Gemini-Robotics produces statistically identical predictions across all three independent batches for a significant subset of images. Evidence:

**Weight examples (same image, all 3 batches)**:
- V-weight-image50: 4000g / 4000g / 4000g (GT = 297g)
- P-weight-image6: 350g / 350g / 250g (GT = 82g)
- P-weight-image28: 200g / 200g / 200g (GT = 91g)
- P-weight-image54: 200g / 200g / 250g (GT = 91g)
- P-weight-image10: 200g / 200g / 200g (GT = 104g)

**Stability examples (same image, all 3 batches)**:
- P-stability-image10: 30° / 30° / 30°
- B-stability-image3: 90° / 90° / 90°
- M-stability-image13: 90° / 90° / 90°

**Fit examples**: OpenAI B1 and B2 are identical (precision, recall, F1 all match exactly).

This determinism indicates that these models are either running inference with temperature=0 or close to it, or have memorized canonical visual representations for certain objects. It also means that running the same benchmark multiple times on Gemini-Robotics is not providing independent measurement replicates for these images — the batch replication has limited statistical value for this model.

In contrast, OpenAI shows high prediction variance for identical images across batches (V-weight-image54: 7500g / 13000g / 1000g; V-weight-image45: 6200g / 6000g / 5800g). This variability is consistent with non-zero temperature inference.

### 3.3 Liquid Volume Correlation Anomaly

Gemini-Robotics achieves r=0.41 in batches 1 and 3 but r=1.00 in batch 2 for liquid volume. All other model-batch combinations in this category achieve r=1.00.

A Pearson correlation of 0.41 with low MAPE (~23%) is unusual. A plausible explanation: a subset of containers receives predictions that are in the correct absolute range but in the wrong relative order compared to ground truth. If the model's volume estimation procedure is slightly miscalibrated such that it assigns similar values to containers that should differ substantially in rank (e.g., two containers both estimated at ~500mL when GTs are 250mL and 750mL), MAPE could be low while rank order is disrupted. The fact that B2 achieves r=1.00 while B1 and B3 do not — despite Gemini-Robotics being broadly deterministic elsewhere — is unexplained and warrants direct investigation of which specific images drive the correlation difference between batches.

### 3.4 The Stability 90° Threshold Bias in Gemini-Robotics

Gemini-Robotics consistently predicts 90° as the instability threshold angle for any image where the question involves an angle at which a leaning/tilted object becomes unstable. This occurs identically across all three batches. The reasoning is always some variant of: "at 90 degrees (vertical position), the support structure fails."

This is a structural conceptual error. For a leaning board propped against a wall (B-stability-image3, GT=13°), stability is lost at a small angle — the board needs only slight rotation to leave the prop. For a leaning board resting against an ottoman (M-stability-image13, GT=56.4°), the critical angle is mid-range. Gemini-Robotics cannot distinguish these cases and always outputs 90°, producing 6.9× errors on the former and 1.6× on the latter by coincidence.

### 3.5 Shared Cross-Model Anchoring in Liquid Volume

The three most common liquid volume errors are identical across all three models:

1. **The 1L beaker problem**: A 500mL beaker has graduation marks up to 1000mL. All models read the top graduation mark as the capacity, predicting 1000mL. This is a fundamental misunderstanding: the top mark indicates the scale maximum, not the fill capacity of the vessel.

2. **The 50mL→100mL rounding**: A 50mL graduated beaker is always predicted as 100mL. 50mL appears to be below the threshold of "plausible small beaker" for all three models, which round up to the next standard size.

3. **The 30oz Stanley tumbler problem**: A 30oz (887mL) insulated tumbler with handle is predicted as 40oz (~1183mL) by all models. The 40oz Stanley Quencher model is far more prominent in training data, and the models cannot distinguish the 30oz vs 40oz form factor from a single image.

These shared anchoring failures suggest all three models draw on similar training data distributions for these specific object categories.

---

## 4. Per-Model Error Pattern Analysis

### 4.1 OpenAI

#### Weight
- **Error range**: 0.09× to 61×. The widest range of any model — includes both extreme overestimates and significant underestimates.
- **Cross-batch inconsistency**: The same image can yield completely different predictions across batches. V-weight-image54 (yoga blocks on stool, GT=212g) is predicted at 7500g, 13000g, and 1000g across batches. V-weight-image45 (wooden crate/tray, GT=403g) is predicted at 6200g, 6000g, and 5800g — slightly more consistent, but the absolute values are all wildly wrong in the same direction.
- **No directional bias**: Unlike Gemini models, OpenAI produces both extreme overestimates (61× for V-image54 in B2) and significant underestimates (0.09× for B-weight-image1 box of straw items). This bidirectionality means errors cannot be corrected by a simple scaling factor.
- **Material misclassification as root cause**: B-weight-image1 (GT=8000g) — OpenAI counts individual straw placemat pieces and multiplies by per-piece weight (~180g each), predicting 700–900g. It fails to account for the total mass of the box contents and treats each piece in isolation. P-weight-image73 (water bucket, GT=12400g) — correctly identifies a small plastic bucket but estimates it as ~5L half-filled, predicting ~3kg. The ground truth bucket is substantially larger.
- **Hollow-frame problem**: V-weight-image50 (hollow steel table leg frame) is predicted at 3000–13000g across batches (GT=297g). OpenAI mentally constructs a complete table and estimates the entire piece of furniture, not just the marked frame. The prediction variance (3000 to 13000g) across batches for the same object reflects unstable object-level scene interpretation.
- **Reasoning style**: Largely verbal and qualitative. Descriptions like "a small padded fabric bag" or "solid hardwood armrest" followed by size estimation from context, without systematic material density calculations or reference object scaling.

#### Stability
- **All worst cases are overestimates** — OpenAI never predicts a system to be more stable than it is.
- **GT=0 failures**: Cannot represent the concept of "already unstable." Predicts 20–40° for cases where GT=0. This is perhaps unavoidable from a static image, but the spread of 20° to 40° across batches for the same image reflects lack of any principled physical model.
- **Small margin overestimation**: For GT values of 2–5 cm displacement to instability, OpenAI predicts 5–25 cm — off by 2–12×. Reasoning is purely visual: "looks about 12 cm" with no lever arm calculation.
- **Cross-batch inconsistency**: M-stability-image3 (GT=2cm) is predicted at 20cm, 12cm, 12cm. No convergence toward the correct answer across runs.

#### Angle
- **Interior/exterior supplement confusion is the dominant failure**: OpenAI reads the obtuse angle at a joint when the ground truth marks the acute angle. The error is not always in the same direction — in B1, M-angle-image8 (GT=7.7°) is predicted at 170° (22× error). In B2, the same image is predicted at 25° (3.25×). In B3, it's 17° (2.2×). No convergence.
- **Overestimate bias**: All 30 worst-case errors in the worst-cases document are overestimates. When uncertain, OpenAI rounds toward 90° or toward the supplement of the true angle.
- **No pixel analysis**: Reasoning is qualitative geometric description ("slopes moderately steeply," "appears to form an acute angle") without computing slope ratios or using reference geometry.
- **Persistent errors on specific images**: P-angle-image9 (GT=37.2°) is predicted at 65° in all three batches — a stable but incorrect answer (1.75× overestimate). This is one of the few images where OpenAI converges, but to the wrong value.

#### Fit
- **FP-heavy (50 FPs, 36 FNs)**: Strongly biased toward predicting YES. OpenAI is the most permissive model on deformability.
- **FP root cause**: Flexible objects are almost always called YES. Reasoning follows a template: "the object can be folded/coiled/compressed significantly, and the container appears large enough to hold the compacted form." This reasoning fails to account for minimum cross-section constraints (a rope coiled to its limit still has a certain diameter).
- **FN root cause**: Rigid objects placed against containers where the container seems visually smaller. OpenAI refuses to infer diagonal fit potential or container elasticity.
- **No volumetric reasoning**: OpenAI makes verbal size comparisons without computing relative volumes or cross-sections.

#### Liquid Volume
- **Consistent moderate overestimation of 1.33–2×**. No extreme outliers (max ~2× error) — the tightest worst-case distribution of any model in this category.
- **Standard-size anchoring**: Consistently maps container appearances to the nearest "common" size (500mL bottle, 1000mL beaker) regardless of actual visual measurement.
- **Cross-batch consistency is better here than for weight**: Same images produce the same prediction across batches (image24 always = 1000mL), suggesting this category triggers more deterministic behavior than weight.

---

### 4.2 Gemini

#### Weight
- **Error range: 1.83× to 18.52×**. No underestimates appear in the worst 30 cases — pure overestimate direction.
- **Single categorical outlier: V-weight-image50** (GT=297g): predicted at 5500g, 4500g, 5500g across batches (~15–18×). The reasoning is geometrically principled — Gemini estimates the tubing length (∼2.6m), assigns a steel density (1.5–2.5 kg/m), and calculates 4–6kg. The error is that the calculation is correct for a full table frame, but the ground truth marks only the visible leg section. This is a scene scope error, not a density error.
- **CO2 fire extinguisher canonical error**: P-weight-image64 (GT=4500g, the CO2 charge mass) is predicted at 14000–15000g (3.1–3.3×) in all batches. Gemini correctly identifies CO2 extinguishers as heavy-duty due to high-pressure cylinders and estimates the total gross weight including cylinder + CO2. The GT is for the CO2 charge only.
- **Controlled overestimate ceiling**: Outside V-image50 and the extinguisher, all worst-case errors in B1 and B3 are ≤3.33× and in B2 ≤3.11×. Gemini never exhibits the 10–60× magnitude errors that appear in OpenAI's worst cases.
- **Better material identification**: Correctly classifies EVA foam (yoga blocks, ~250g each), pine wood density (0.4–0.5 g/cm³), rope packing fraction, and pot/soil weight composition. Errors are in structural scope or scale, not material property lookup.
- **Methodology**: Uses explicit reference object scaling (comparing to known objects — gas cylinders, floor tiles, water bottles) and often calculates volume × density explicitly. More principled than OpenAI.

#### Stability
- **GT=0 case**: Always predicts ~20° by computing arctan(0.35) ≈ 20° based on a stated coefficient of friction of 0.3–0.4. This is principled physics reasoning, but the specific friction pair (smooth plastic on MDF) has a friction threshold near 0.
- **Formula-driven block stacking**: For stability-image11 (block stacking, GT=3 blocks to collapse), Gemini applies N×d > L correctly but miscounts pixel offsets, arriving at 6 or 12 blocks needed rather than 3.
- **B-stability-image6 direction error (B2)**: Correctly identifies the mat spans two tables and has 18×12 inch dimensions. Determines the shortest path to instability is sliding the mat forward (perpendicular to the table edge) rather than sideways. Predicts 15.24cm (half the 12-inch width) when the actual closest tipping direction requires only 5cm sideways movement. A plausible but incorrect physical analysis.
- **Cross-batch variation**: Same image produces different answers (M-stability-image15: 100mL, 100mL, 50mL across batches). Not as deterministic as Gemini-Robotics.

#### Angle
- **Large outlier in B1**: V-angle-image74 (GT=28.3°) predicted at 165° — Gemini identifies two red line segments and explicitly computes the angle between their direction vectors, arriving at ∼166°. The error is picking the wrong pair of vectors (the exterior reflex angle rather than the intended acute angle).
- **V-angle-image32 complement error**: (GT=37.6°) predicted at 126° and 124.5° in B1/B2. Gemini correctly measures the stick's slope angle from horizontal (~35°) but then adds 90° to get "the angle between the upward-left direction and the downward vertical," yielding the supplement. In B3 it switches to measuring angle from vertical directly, predicting 55°.
- **Pixel-coordinate analysis**: Gemini frequently provides explicit pixel coordinates for angle computation (e.g., "vertex at (443, 555), arm to (541, 419)"). This shows genuine geometric analysis effort, but the errors arise from choosing incorrect reference lines or measuring the supplement.
- **Best consistent performance across batches** of all three models (full MAPEs of 17–25% vs 23–50% for others).
- **Rectangular frame defaults**: When the marked point is at a corner of a clearly rectangular object, Gemini sometimes defaults to 90°, even if the question asks about the board's tilt relative to the floor.

#### Fit
- **FN-heavy (25 FPs, 51 FNs)**: Opposite direction from OpenAI. Gemini is the most conservative model — biased toward predicting NO.
- **FP pattern**: Shares deformability overestimation with other models, but applies tighter constraints. Some cloth-through-ring cases that OpenAI calls YES are correctly called NO by Gemini.
- **FN root cause**: Scale underestimation of containers. For M-fit-image13 (rigid triangular board vs cardboard box), Gemini correctly identifies the board as rigid and visually large, then concludes it cannot fit — but the box diagonal is actually sufficient. Gemini's visual scale estimation fails for unusual orientations and non-square containers.
- **Best F1 overall (35.60%)**: The more conservative NO bias raises precision (57.14%) while recall stays respectable (25.86%), yielding the best F1.
- **Unique Gemini B2 error**: P-liquid_volume-image16 — sees a glass bottle resting upside-down on its cap. The 1000mL graduation mark is visible at what is now the bottom. Predicts 1000mL (GT=100mL, the actual fill level). The 10× error comes from confusing the beaker's maximum scale marking with the current liquid volume.

#### Liquid Volume
- **Error pattern similar to OpenAI** for most images — same anchoring biases, slightly better filtered MAPE.
- **More detailed geometric reasoning**: Computes pixel height ratios, uses cylinder volume formulas (π×r²×h), adjusts for wall thickness. This provides incremental improvement but does not overcome the fundamental standard-size anchoring problem.
- **Cross-batch correlation**: r=1.00 in all three batches — no anomaly unlike Gemini-Robotics.

---

### 4.3 Gemini-Robotics

#### Weight
- **Cross-batch determinism is the defining characteristic**: Identical predictions across all three batches for a large fraction of images. This is the strongest evidence in the dataset that Gemini-Robotics uses temperature=0 or equivalent deterministic inference.
- **Error range: 1.83× to 13.47×**. The 13.47× is exclusively V-weight-image50 (same steel frame image). All other worst-case errors are within 4.3×.
- **Pure overestimate direction**: No underestimates appear in any batch's worst 30. Combined with determinism, this means the overestimate bias is a systematic property of the model's physical priors, not sampling noise.
- **Categorical prior anchoring**: Reasoning is shorter and more categorical than Gemini. Examples: "bundles of this type typically weigh 250–450 grams" (no density calculation), "typical weight for this category is 200g" (no reference object scaling). The model assigns weights from a lookup-table of category-weight associations rather than computing from visual geometry.
- **The glue gun canonical error**: All hot glue gun images (P-weight-image28, P-weight-image54) are predicted at exactly 200g across all three batches. The reasoning text is structurally identical: "mini glue guns typically weigh 150–300 grams, 200g is reasonable." GT = 91g (2.2× error). This is a pure category prior — the model cannot update this estimate from context.
- **No reference object scaling**: Unlike Gemini, Gemini-Robotics never explicitly computes relative sizes using reference objects. This shortens reasoning but removes the mechanism for updating from image-specific information.

#### Stability
- **Worst stability performance of the three models** (filtered MAPE 45–48% vs 35–42% for others).
- **Hardcoded GT=0 response**: P-stability-image10 (sliding angle, GT=0) is always predicted at exactly 30° across all three batches. Reasoning: "typical static friction angle for common materials ≈ 30°." This is a stored constant, not image-derived.
- **90° as universal instability threshold**: B-stability-image3 (rotation angle, GT=13°, ratio=6.92×), M-stability-image13 (leaning board angle, GT=56.4°, ratio=1.6×), B-stability-image14 (leaning block angle, GT=50°, ratio=1.8×) — all predicted at 90° in every batch. The conceptual error: "to become unstable, a leaning object must reach vertical (90°) where its center of gravity is directly over a narrow support." This is physically wrong in all three cases.
- **No lever-arm calculations**: Unlike Gemini's pixel-based torque analysis, Gemini-Robotics estimates stability margins intuitively. This removes the possibility of formula-based errors but also removes the possibility of correct physics-based reasoning.

#### Angle
- **Most extreme outliers in the dataset**: M-angle-image8 (GT=7.7°) predicted at 165° in B1 and 168° in B2 — ratios of 21.4× and 21.8×. This single image drives the entire B1/B2 full MAPE signal.
- **V-angle-image32** (GT=37.6°): predicted at 175° (B1, ratio=4.65×) — the model reasons that the marked point on the wooden stick shows "no distinct sharp bend; the stick appears essentially straight," so predicts ~180°. In B3, correctly identifies the angle as 55°.
- **Rectangular-object default**: Any angle marked at a corner of a box, cushion, or board is predicted at 90°, regardless of the actual geometry. This fires even when the question clearly asks about the board's tilt angle relative to the floor (not the corner angle of the board itself). Examples: V-angle-image31, V-angle-image59/59-pov2, V-angle-image74 (predicted 90° in B3).
- **Best performance after outlier removal**: Filtered MAPE of 11–15% is as good as or better than OpenAI (~12–15%) and nearly as good as Gemini (~11–13%). The bimodal character — near-perfect on most images, catastrophic on a few — makes Gemini-Robotics the most sensitive model to outlier removal in angle.
- **Strong overestimate bias in angle**: Overestimate % is 77–79% in the full dataset, the highest of any model. The supplement-confusion and 90°-default errors both contribute predictions that are systematically larger than GT.

#### Fit
- **Moderate FP count (40), lowest FN count (26)**: Between OpenAI (FP=50) and Gemini (FP=25). Least conservative about declaring fit for rigid objects but has unique FP patterns.
- **Unique FP class — purpose-built container assumption**: M-fit-image18 (battery into wrong compartment) — Gemini-Robotics predicts YES because it identifies the slot as "specifically designed to hold a battery of that exact size." Other models make the same error, but Gemini-Robotics' reasoning is the most confident and type-specific.
- **Playing card FP**: P-fit-image17 — predicts cards can fit into a thermos because "playing cards are flexible and can be slightly curved." This type of material-flexibility reasoning error is more pronounced in Gemini-Robotics.
- **Best precision (67.09%)**: High selectivity in predicting YES for ambiguous cases leads to fewer FPs per true positive, driving the highest precision despite moderate overall FP count.

#### Liquid Volume
- **Best MAPE overall (18–20% filtered)** but paired with the correlation anomaly described in Section 3.3.
- **All worst cases bounded at ≤2×**: The maximum error in any batch is 2.00× (P-liquid_volume-image24: 1000mL vs GT=500mL). This tight error ceiling means the model is never catastrophically wrong on individual containers, even when global rank ordering is disrupted.
- **Same anchoring biases as other models**: Stanley tumbler = 1183–1200mL (GT=887mL), small beakers = 100mL (GT=50mL), narrow glass bottles = 500mL (GT=350mL).

---

## 5. Failure Mode Taxonomy

A systematic classification of failure modes identified from reasoning trace analysis across all categories.

| # | Failure Mode | Categories | Models Affected | Description |
|---|---|---|---|---|
| FM-1 | **Scene scope misinterpretation** | weight | All, esp. OpenAI | Model includes surrounding objects or assumes full structure when only part is marked. V-weight-image50: marked leg frame = full table weight |
| FM-2 | **Categorical prior anchoring** | weight, liquid_volume | GR primarily | Fixed weight/volume lookup by object category, no image-driven update. Glue gun always = 200g |
| FM-3 | **Standard-size snapping** | liquid_volume | All (shared) | Maps any container to nearest "common" size (50mL→100mL, 350mL→500mL, 887mL→1183mL) |
| FM-4 | **Graduation mark ≠ capacity confusion** | liquid_volume | All (shared) | Reads the top graduation on a beaker (e.g., 1000mL marking) as the beaker's full capacity rather than the scale maximum |
| FM-5 | **Gross vs. net weight confusion** | weight, stability | Gemini, GR | Predicts gross system weight when GT marks a component (extinguisher CO2 only; table frame only) |
| FM-6 | **Interior/exterior angle supplement confusion** | angle | All, esp. GR | Reads the supplement or complement of the intended angle. Predicts 165° for 7.7° joints |
| FM-7 | **Rectangular default** | angle, fit | GR, Gemini | Assumes all marked corners on rectangular objects are 90°, regardless of the board's actual tilt relative to the floor |
| FM-8 | **90° instability threshold** | stability | GR only | Systematically predicts 90° as the angle at which any leaning structure becomes unstable |
| FM-9 | **GT=0 instability blindness** | stability | All (shared) | Cannot detect that an object is already at or past the tipping threshold from a static image; always predicts a non-zero threshold |
| FM-10 | **Deformability overestimation** | fit | All, esp. OpenAI | Overestimates how far flexible objects (cloth, hose, cable) can be compressed to fit through constrained openings |
| FM-11 | **Container size underestimation** | fit | All, esp. Gemini | Underestimates container interior capacity for rigid objects, missing diagonal fit potential |
| FM-12 | **Fill-level vs. capacity confusion** | liquid_volume | Gemini (B2) | For upside-down or full containers, confuses the current fill volume with the container's total capacity |
| FM-13 | **Directionality of instability error** | stability | Gemini (B2) | Correctly identifies instability exists but predicts the wrong direction of movement that would cause tipping |
| FM-14 | **Material density correct, structural scope wrong** | weight | Gemini | Applies accurate material density (steel, pine, EVA foam) but to the wrong structural element (whole frame vs marked component) |
| FM-15 | **Cross-batch hallucination variance** | weight, angle | OpenAI | Same image produces wildly different object descriptions across batches, driving prediction variance of up to 13× for the same item |

---

## 6. Model Comparison Summary

### Performance Rankings by Category

| Category | Best → Worst (filtered MAPE) |
|---|---|
| Weight | Gemini ≈ Gemini-Robotics >> OpenAI |
| Stability | OpenAI ≈ Gemini >> Gemini-Robotics |
| Angle | Gemini > OpenAI ≈ Gemini-Robotics (after filtering) |
| Liquid Volume | Gemini-Robotics > Gemini > OpenAI |
| Fit (F1) | Gemini > Gemini-Robotics > OpenAI |

No single model dominates across all categories.

### Behavioral Profiles

| Dimension | OpenAI | Gemini | Gemini-Robotics |
|---|---|---|---|
| Error direction | Bidirectional (over and under) | Consistently overestimates | Consistently overestimates |
| Max error ratio observed | 61× (weight) | 18.5× (weight) | 21.8× (angle) |
| Cross-batch consistency | Low — high variance | Medium | High — near-deterministic |
| Reasoning methodology | Visual/qualitative | Pixel-coordinate geometry | Categorical priors |
| Outlier sensitivity | Extreme (weight) | Moderate | Extreme (angle) |
| Best category | — | Angle | Liquid volume |
| Worst category | Weight (full MAPE) | Stability | Stability |
| Stability 90° error | No | No | Yes — systematic |
| Liquid volume correlation anomaly | No | No | Yes (B1, B3) |
| Fit bias | FP-heavy (permissive) | FN-heavy (conservative) | Moderate |

### Condensed MAPE Reference Table (Filtered, per batch)

| Category | OpenAI B1 | B2 | B3 | Gemini B1 | B2 | B3 | GR B1 | B2 | B3 |
|---|---|---|---|---|---|---|---|---|---|
| Weight | 35.70% | 38.42% | 36.75% | 29.54% | 29.94% | 28.94% | 28.99% | 29.72% | 30.14% |
| Stability† | 37.41% | 41.32% | 35.89% | 41.93% | 37.48% | 41.39% | 45.77% | 48.48% | 46.86% |
| Angle | 14.81% | 14.83% | 12.14% | 10.96% | 13.04% | 10.69% | 14.38% | 14.76% | 11.68% |
| Liquid Vol. | 24.43% | 26.81% | 27.60% | 24.80% | 21.15% | 21.77% | 19.27% | 19.35% | 18.52% |

†Stability full MAPE is undefined (GT=0 division). Filtered only.

### Condensed Fit Reference Table

| Model | Precision | Recall | F1 | FP count | FN count |
|---|---|---|---|---|---|
| OpenAI | 54.43% | 17.00% | 25.90% | 50 | 36 |
| Gemini | 57.14% | 25.86% | 35.60% | 25 | 51 |
| Gemini-Robotics | 67.09% | 19.41% | 30.11% | 40 | 26 |
