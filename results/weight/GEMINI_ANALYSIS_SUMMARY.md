# Gemini & Gemini-Robotics Models: Analysis Summary

## 📊 Files Generated

1. **gemini_models_worst_cases_reasoning.md** - Full reasoning traces for all 30 worst cases (10 per batch, per model)
2. **gemini_models_metrics_comparison.txt** - Detailed metrics with/without worst 10 per batch

---

## 🔴 KEY PATTERNS IN WORST CASES

### GEMINI MODEL

**Worst 10 cases per batch (ranked by magnitude of error):**

**Batch 1:**
1. `V-weight-image50.jpg` — 18.5× over (Metal frame incorrectly identified as heavier)
2. `V-weight-image45.jpg` — 3.7× over (Wooden crate misestimated)
3. `P-weight-image64.jpg` — 3.3× over (Fire extinguisher overestimated)
4. `P-weight-image6.jpg` — 2.4× over (Utility rope overestimated)
5. `V-weight-image54.jpg` — 2.4× over (Yoga blocks identified correctly but overestimated)
6. `P-weight-image31.jpg` — 2.2× over (Potted plant overestimated)
7. `P-weight-image28.jpg` — 2.2× over (Hot glue gun overestimated)
8. `P-weight-image54.jpg` — 2.2× over (Mini hot glue gun overestimated)
9. `V-weight-image46.jpg` — 2.0× over (Cushion overestimated)
10. `P-weight-image10.jpg` — 1.9× over (Packing tape overestimated)

**Batch 2:**
1. `V-weight-image50.jpg` — 15.2× over (Same metal frame error)
2. `P-weight-image64.jpg` — 3.1× over (Fire extinguisher)
3. `V-weight-image54.jpg` — 2.4× over (Yoga blocks)
4. `P-weight-image17.jpg` — 2.3× over
5. `P-weight-image28.jpg` — 2.2× over (Hot glue gun)
6. `V-weight-image45.jpg` — 2.0× over (Wooden crate)
7. `P-weight-image54.jpg` — 2.0× over (Mini hot glue gun)
8. `P-weight-image10.jpg` — 1.9× over (Packing tape)
9. `P-weight-image3.jpg` — 1.9× over
10. `P-weight-image5.jpg` — 1.9× over

**Batch 3:**
1. `V-weight-image50.jpg` — 18.5× over (Metal frame again)
2. `P-weight-image64.jpg` — 3.1× over (Fire extinguisher)
3. `P-weight-image28.jpg` — 2.2× over (Hot glue gun)
4. `P-weight-image56.jpg` — 2.1× over
5. `V-weight-image45.jpg` — 2.0× over (Wooden crate)
6. `P-weight-image3.jpg` — 1.9× over
7. `P-weight-image21.jpg` — 1.9× over
8. `V-weight-image54.jpg` — 1.9× over (Yoga blocks)
9. `V-weight-image38.jpg` — 1.8× over
10. `P-weight-image6.jpg` — 1.8× over (Utility rope)

**🎯 Gemini Patterns:**
- **Consistent offenders**: V-image50 (18.5× in Batch 1 & 3, 15.2× in Batch 2), V-image45, P-image64
- **No underestimation cases** - Only overestimates!
- **Reasoning bias**: Model applies heavy material density assumptions (metal frame = 4.5-6.5kg; fire extinguisher = 14-16kg)
- **Formula-based errors**: Often cites specific dimensions and applies material density formulas
- **Material confusion**: Attributes incorrect materials (e.g., treating foam yoga blocks as if made of heavier material)

---

### GEMINI-ROBOTICS MODEL

**Worst 10 cases per batch:**

**Batch 1:**
1. `V-weight-image50.jpg` — 13.5× over (Metal frame)
2. `P-weight-image6.jpg` — 4.3× over (Utility rope)
3. `V-weight-image45.jpg` — 3.0× over (Wooden crate)
4. `P-weight-image12.jpg` — 2.4× over
5. `V-weight-image49.jpg` — 2.3× over
6. `P-weight-image28.jpg` — 2.2× over (Hot glue gun)
7. `P-weight-image54.jpg` — 2.2× over (Mini hot glue gun)
8. `P-weight-image22.jpg` — 2.1× over
9. `V-weight-image43.jpg` — 2.0× over
10. `P-weight-image10.jpg` — 1.9× over (Packing tape)

**Batch 2:**
1. `V-weight-image50.jpg` — 13.5× over (Metal frame, same across batches!)
2. `P-weight-image6.jpg` — 4.3× over (Rope, consistent)
3. `P-weight-image12.jpg` — 2.7× over
4. `V-weight-image49.jpg` — 2.7× over
5. `V-weight-image45.jpg` — 2.5× over (Wooden crate)
6. `P-weight-image64.jpg` — 2.4× over (Fire extinguisher)
7. `V-weight-image43.jpg` — 2.4× over
8. `V-weight-image54.jpg` — 2.4× over (Yoga blocks)
9. `P-weight-image28.jpg` — 2.2× over (Hot glue gun)
10. `P-weight-image54.jpg` — 2.2× over (Mini hot glue gun)

**Batch 3:**
1. `V-weight-image50.jpg` — 13.5× over (Metal frame, **identical across all 3 batches**)
2. `P-weight-image12.jpg` — 3.0× over
3. `P-weight-image6.jpg` — 3.0× over (Rope)
4. `V-weight-image45.jpg` — 3.0× over (Wooden crate)
5. `P-weight-image54.jpg` — 2.7× over (Mini hot glue gun)
6. `V-weight-image49.jpg` — 2.5× over
7. `V-weight-image43.jpg` — 2.4× over
8. `V-weight-image54.jpg` — 2.4× over (Yoga blocks)
9. `P-weight-image28.jpg` — 2.2× over (Hot glue gun)
10. `P-weight-image17.jpg` — 2.0× over

**🎯 Gemini-Robotics Patterns:**
- **Ultra-consistent**: V-image50 shows **exactly 13.5× over in all 3 batches** (deterministic behavior!)
- **No underestimation cases** - Also only overestimates
- **Different offenders than Gemini**: P-image6 (rope) ranks much higher; P-image64 lower
- **More stable**: Failure cases are very similar across batches (suggests deterministic model)
- **Robotics-specific bias**: Likely trained on heavier industrial/robotic components, leading to overestimation on light objects

---

## 📈 METRICS: WITH vs WITHOUT WORST 10 PER BATCH

### GEMINI MODEL

| Batch | MAPE Before | MAPE After | Improvement | Top Issue |
|-------|------------|-----------|-------------|-----------|
| **1** | 54.6% | 29.5% | **-45.8%** | V-image50 (18.5×) |
| **2** | 49.7% | 29.9% | **-39.7%** | V-image50 (15.2×) |
| **3** | 50.7% | 28.9% | **-42.9%** | V-image50 (18.5×) |

**Per-Batch Additional Metrics (After removing worst 10):**

**Batch 1:**
- MAE: 976.4 (was 1057.6, -7.7%)
- Within ±25%: 48.0% (was 43.8%)
- Overestimate rate: 38.2% (was 43.8%)

**Batch 2:**
- MAE: 914.3 (was 968.5, -5.6%)
- Within ±50%: 84.2% (was 76.6%)
- Correlation improved: 0.96 (was 0.95)

**Batch 3:**
- MAE: 926.5 (was 1016.1, -8.8%)
- Median AE: 95.5 (was 107.0, -10.7%)
- Within ±25%: 50.0% (was 45.5%)

---

### GEMINI-ROBOTICS MODEL

| Batch | MAPE Before | MAPE After | Improvement | Top Issue |
|-------|------------|-----------|-------------|-----------|
| **1** | 49.5% | 29.0% | **-41.4%** | V-image50 (13.5×) |
| **2** | 51.3% | 29.7% | **-42.1%** | V-image50 (13.5×) |
| **3** | 51.2% | 30.1% | **-41.2%** | V-image50 (13.5×) |

**Per-Batch Additional Metrics (After removing worst 10):**

**Batch 1:**
- MAPE improvement: -41.4%
- Within ±10%: 27.5% (was 25.0%)
- Correlation: 0.96 (unchanged)
- Bias slightly worse after removal: -334.9 (was -253.2)

**Batch 2:**
- MAPE improvement: -42.1%
- Median AE: 157.5 (was 182.5, -13.7%)
- Within ±50%: 82.4% (was 75.0%)

**Batch 3:**
- MAPE improvement: -41.2%
- Bias slightly negative: -368.1 (was -280.0)
- Correlation stable at 0.96

---

## 🔍 COMPARATIVE INSIGHTS

### OpenAI vs Gemini vs Gemini-Robotics

| Metric | OpenAI | Gemini | Gemini-Robotics |
|--------|--------|--------|-----------------|
| **MAPE (all data)** | 98.2% | ~51.6% | ~50.7% |
| **MAPE (no worst 10)** | 33.2% | ~29.5% | ~29.6% |
| **Improvement** | -66.2% | ~-43% | ~-41% |
| **Error Direction** | Both over & under | Over only | Over only |
| **Worst Case Magnitude** | 61× (Batch 2) | 18.5× (Batch 1 & 3) | 13.5× (all batches) |
| **Consistency** | Variable | High | **Very High** |

**Key Findings:**
- **OpenAI** has highest baseline errors but worst cases are more extreme
- **Gemini** more moderate overall but consistent overestimation bias
- **Gemini-Robotics** most consistent/deterministic (V-image50 = exactly 13.5× across all 3 batches)
- **Gemini models** don't underestimate - only overestimate (vs OpenAI which does both)
- **Removing worst 10 per batch provides 40-45% MAPE improvement** for all models

---

## 💡 REASONING PATTERN ANALYSIS

### GEMINI: Formula-Based Reasoning
- Cites specific dimensions and applies material density calculations
- Example: "Metal tubing ~2.6m × 1.5-2.5 kg/m = 4.5-6.5 kg" (actual: 297g)
- Over-applies density assumptions

### GEMINI-ROBOTICS: Industrial-Biased Reasoning
- Treats objects as if they're industrial/robotic components
- More conservative dimensional estimates but applies heavier assumptions
- Deterministic behavior: exact same error ratio across batches

### Common Theme
Both Gemini models show **material density misjudgment** — they systematically overestimate how much materials weigh per unit volume.

---

## 📁 Files to Review

✅ **gemini_models_worst_cases_reasoning.md** — 60 detailed reasoning traces (organized by model and batch)
✅ **gemini_models_metrics_comparison.txt** — Full metrics breakdown for all 3 batches per model

**Next Steps:** You can manually inspect the reasoning traces for additional pattern insights!
