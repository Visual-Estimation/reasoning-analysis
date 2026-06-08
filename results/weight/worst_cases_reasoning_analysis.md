# Worst 30 Weight-Estimation Cases: Detailed Reasoning Analysis

This document extracts the full reasoning traces for the 30 worst-performing weight estimation cases,
ranked by log-scale error (|log₁₀(pred/GT)|) within each batch.

---

## BATCH 1

### #1: `V-weight-image54.jpg`

**Prediction Metrics:**
- Ground Truth: 212.0
- Prediction: 7500.0
- Ratio (Pred/GT): 35.38× (OVER)
- Relative Error: 3437.7%

**OpenAI Reasoning Trace:**
> The marked area appears to be a small solid-wood stool/bench with two lightweight foam yoga blocks on top; a reasonable estimate is about 7 kg for the stool and 0.5 kg for the blocks.

---

### #2: `V-weight-image45.jpg`

**Prediction Metrics:**
- Ground Truth: 403.0
- Prediction: 6200.0
- Ratio (Pred/GT): 15.38× (OVER)
- Relative Error: 1438.5%

**OpenAI Reasoning Trace:**
> The object appears to be a medium-sized stepped wooden/MDF panel or rack, roughly 65–75 cm tall, 25–35 cm wide, and about 4–6 cm thick, which suggests a weight in the mid single-digit kilograms.

---

### #3: `V-weight-image50.jpg`

**Prediction Metrics:**
- Ground Truth: 297.0
- Prediction: 3400.0
- Ratio (Pred/GT): 11.45× (OVER)
- Relative Error: 1044.8%

**OpenAI Reasoning Trace:**
> Large hollow metal furniture frame, likely made from steel tubing and roughly 75–90 cm tall, so it likely weighs a few kilograms.

---

### #4: `B-weight-image1.jpg`

**Prediction Metrics:**
- Ground Truth: 8000.0
- Prediction: 700.0
- Ratio (Pred/GT): 0.09× (UNDER)
- Relative Error: 91.2%

**OpenAI Reasoning Trace:**
> The box contains about four lightweight woven straw/rattan placemat or tray-like pieces; estimating roughly 150–200 g each gives a total near 700 g.

---

### #5: `P-weight-image54.jpg`

**Prediction Metrics:**
- Ground Truth: 91.0
- Prediction: 480.0
- Ratio (Pred/GT): 5.27× (OVER)
- Relative Error: 427.5%

**OpenAI Reasoning Trace:**
> The red mark appears to cover a small padded fabric bag/case, roughly lunch-bag sized; such bags typically weigh a few hundred grams, so an estimate near half a kilogram is reasonable.

---

### #6: `V-weight-image43.jpg`

**Prediction Metrics:**
- Ground Truth: 148.0
- Prediction: 700.0
- Ratio (Pred/GT): 4.73× (OVER)
- Relative Error: 373.0%

**OpenAI Reasoning Trace:**
> It looks like a solid hardwood bracket/arm piece about 45–50 cm long with an average section near 4 × 3.5 cm, giving roughly 900 cm³ of wood; using typical hardwood density gives an estimate around 700 g.

---

### #7: `P-weight-image59.jpg`

**Prediction Metrics:**
- Ground Truth: 573.0
- Prediction: 135.0
- Ratio (Pred/GT): 0.24× (UNDER)
- Relative Error: 76.4%

**OpenAI Reasoning Trace:**
> The boxed item appears to be a small manual pump piece with a rubber bulb, plastic/glass cup, and wood connector; given its size and materials, a reasonable estimate is about 135 grams.

---

### #8: `P-weight-image26.jpg`

**Prediction Metrics:**
- Ground Truth: 102.0
- Prediction: 430.0
- Ratio (Pred/GT): 4.22× (OVER)
- Relative Error: 321.6%

**OpenAI Reasoning Trace:**
> The marked item looks like a small rugged cylindrical device/container about 15 cm long; objects of that size are often around 0.3 to 0.5 kg, so a mid-range estimate is reasonable.

---

### #9: `P-weight-image73.jpg`

**Prediction Metrics:**
- Ground Truth: 12400.0
- Prediction: 2950.0
- Ratio (Pred/GT): 0.24× (UNDER)
- Relative Error: 76.2%

**OpenAI Reasoning Trace:**
> This looks like a small plastic bucket of roughly 4.5–5 L capacity, filled a bit over half with water; that suggests about 2.7 kg of water plus about 0.25 kg for the bucket itself.

---

### #10: `P-weight-image6.jpg`

**Prediction Metrics:**
- Ground Truth: 82.0
- Prediction: 320.0
- Ratio (Pred/GT): 3.90× (OVER)
- Relative Error: 290.2%

**OpenAI Reasoning Trace:**
> The marked object appears to be a coiled synthetic utility rope, roughly 12–15 m long and about 6–8 mm thick; ropes of that size usually weigh a few hundred grams.

---

## BATCH 2

### #1: `V-weight-image54.jpg`

**Prediction Metrics:**
- Ground Truth: 212.0
- Prediction: 13000.0
- Ratio (Pred/GT): 61.32× (OVER)
- Relative Error: 6032.1%

**OpenAI Reasoning Trace:**
> The outlined object appears to be a small solid-wood bench/coffee table; one of this size typically weighs around 10–15 kg.

---

### #2: `V-weight-image45.jpg`

**Prediction Metrics:**
- Ground Truth: 403.0
- Prediction: 6000.0
- Ratio (Pred/GT): 14.89× (OVER)
- Relative Error: 1388.8%

**OpenAI Reasoning Trace:**
> The object appears to be a medium-sized painted wooden/MDF slatted panel, roughly around 70×35×8 cm; that size and material would typically weigh about 5–7 kg.

---

### #3: `B-weight-image1.jpg`

**Prediction Metrics:**
- Ground Truth: 8000.0
- Prediction: 720.0
- Ratio (Pred/GT): 0.09× (UNDER)
- Relative Error: 91.0%

**OpenAI Reasoning Trace:**
> About four medium woven straw trays/mats are visible; items of this size and material are usually light, roughly 150–200 g each, so the total is around 700 g.

---

### #4: `V-weight-image50.jpg`

**Prediction Metrics:**
- Ground Truth: 297.0
- Prediction: 3100.0
- Ratio (Pred/GT): 10.44× (OVER)
- Relative Error: 943.8%

**OpenAI Reasoning Trace:**
> It appears to be a single hollow steel table/desk leg frame roughly 70×50 cm made from rectangular tubing, which typically weighs about 3 kg.

---

### #5: `P-weight-image59.jpg`

**Prediction Metrics:**
- Ground Truth: 573.0
- Prediction: 65.0
- Ratio (Pred/GT): 0.11× (UNDER)
- Relative Error: 88.7%

**OpenAI Reasoning Trace:**
> The marked item appears to be a medium-sized hollow rubber suction bulb with a small wood/metal connector, which is typically light and around a few dozen grams.

---

### #6: `P-weight-image16.jpg`

**Prediction Metrics:**
- Ground Truth: 573.0
- Prediction: 75.0
- Ratio (Pred/GT): 0.13× (UNDER)
- Relative Error: 86.9%

**OpenAI Reasoning Trace:**
> The marked item appears to be a medium-sized hollow rubber squeeze bulb with a small wood/metal connector, so it should be relatively light.

---

### #7: `V-weight-image43.jpg`

**Prediction Metrics:**
- Ground Truth: 148.0
- Prediction: 1050.0
- Ratio (Pred/GT): 7.09× (OVER)
- Relative Error: 609.5%

**OpenAI Reasoning Trace:**
> The marked object looks like a solid hardwood piece roughly 50×7×4 cm overall; that gives about 1.5–1.7 liters of wood, and with typical hardwood density (~0.65 g/cm³) the weight is around 1.0–1.1 kg.

---

### #8: `P-weight-image6.jpg`

**Prediction Metrics:**
- Ground Truth: 82.0
- Prediction: 360.0
- Ratio (Pred/GT): 4.39× (OVER)
- Relative Error: 339.0%

**OpenAI Reasoning Trace:**
> The red-marked item appears to be a medium coil of synthetic utility rope, roughly 20 cm long and 6–7 cm thick, which typically weighs a few hundred grams.

---

### #9: `P-weight-image73.jpg`

**Prediction Metrics:**
- Ground Truth: 12400.0
- Prediction: 3100.0
- Ratio (Pred/GT): 0.25× (UNDER)
- Relative Error: 75.0%

**OpenAI Reasoning Trace:**
> Small plastic bucket likely holds about 5–6 L when full and appears roughly half-filled with water; that suggests about 2.7–3.0 kg of water plus ~0.3 kg for the bucket.

---

### #10: `P-weight-image78-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 96.0
- Prediction: 24.0
- Ratio (Pred/GT): 0.25× (UNDER)
- Relative Error: 75.0%

**OpenAI Reasoning Trace:**
> The pile looks roughly 9–10 cm by 6–7 cm with about 0.8–1 cm average mound height; using a typical salt bulk density around 1.2 g/mL gives an estimate near 24 grams.

---

## BATCH 3

### #1: `V-weight-image45.jpg`

**Prediction Metrics:**
- Ground Truth: 403.0
- Prediction: 5800.0
- Ratio (Pred/GT): 14.39× (OVER)
- Relative Error: 1339.2%

**OpenAI Reasoning Trace:**
> The marked item looks like a small painted wooden/MDF slatted rack or panel, roughly 60–70 cm tall with moderate thickness; objects of that size usually weigh about 5–6 kg.

---

### #2: `V-weight-image50.jpg`

**Prediction Metrics:**
- Ground Truth: 297.0
- Prediction: 3900.0
- Ratio (Pred/GT): 13.13× (OVER)
- Relative Error: 1213.1%

**OpenAI Reasoning Trace:**
> It looks like a single hollow steel furniture/table frame, roughly 75×55 cm with rectangular tubing, which would typically weigh about 4 kg.

---

### #3: `B-weight-image1.jpg`

**Prediction Metrics:**
- Ground Truth: 8000.0
- Prediction: 900.0
- Ratio (Pred/GT): 0.11× (UNDER)
- Relative Error: 88.8%

**OpenAI Reasoning Trace:**
> The box appears to contain about 4 flat woven seagrass/raffia placemat-style pieces: one larger center piece and three smaller ones. Such items typically weigh roughly 200–300 g each, so the total is around 0.9 kg.

---

### #4: `V-weight-image43.jpg`

**Prediction Metrics:**
- Ground Truth: 148.0
- Prediction: 780.0
- Ratio (Pred/GT): 5.27× (OVER)
- Relative Error: 427.0%

**OpenAI Reasoning Trace:**
> The object appears to be a medium-sized solid hardwood armrest/bracket, roughly 45–55 cm long with a fairly thick cross-section, so a weight around three-quarters of a kilogram is reasonable.

---

### #5: `V-weight-image54.jpg`

**Prediction Metrics:**
- Ground Truth: 212.0
- Prediction: 1000.0
- Ratio (Pred/GT): 4.72× (OVER)
- Relative Error: 371.7%

**OpenAI Reasoning Trace:**
> The red outline appears to cover two medium empty plastic storage boxes stacked together; boxes of about 30×20×12 cm typically weigh roughly 450–550 g each, so together they are about 1.0 kg.

---

### #6: `P-weight-image16.jpg`

**Prediction Metrics:**
- Ground Truth: 573.0
- Prediction: 130.0
- Ratio (Pred/GT): 0.23× (UNDER)
- Relative Error: 77.3%

**OpenAI Reasoning Trace:**
> Based on its size relative to the die and bottle cap, the boxed item appears to be a medium hollow rubber bulb with light glass/plastic and wood parts, which would typically weigh around 100–150 g.

---

### #7: `P-weight-image73.jpg`

**Prediction Metrics:**
- Ground Truth: 12400.0
- Prediction: 3000.0
- Ratio (Pred/GT): 0.24× (UNDER)
- Relative Error: 75.8%

**OpenAI Reasoning Trace:**
> The object is a small plastic bucket that looks roughly 5–6 L in capacity and appears about half full of water. That suggests about 2.7–3.0 kg of water plus about 0.3 kg for the bucket itself.

---

### #8: `P-weight-image12.jpg`

**Prediction Metrics:**
- Ground Truth: 82.0
- Prediction: 320.0
- Ratio (Pred/GT): 3.90× (OVER)
- Relative Error: 290.2%

**OpenAI Reasoning Trace:**
> The red-marked item looks like a small coiled synthetic rope/cord, roughly 20–25 cm long and about 8–10 mm thick; a bundle of that size is typically a few hundred grams.

---

### #9: `P-weight-image17.jpg`

**Prediction Metrics:**
- Ground Truth: 215.0
- Prediction: 800.0
- Ratio (Pred/GT): 3.72× (OVER)
- Relative Error: 272.1%

**OpenAI Reasoning Trace:**
> The red-marked object appears to be a short wooden plank/lumber piece, roughly around 50 x 9 x 4 cm; for typical softwood, that gives an estimated mass near 0.8 kg.

---

### #10: `P-weight-image64.jpg`

**Prediction Metrics:**
- Ground Truth: 4500.0
- Prediction: 14500.0
- Ratio (Pred/GT): 3.22× (OVER)
- Relative Error: 222.2%

**OpenAI Reasoning Trace:**
> The red-marked object is a wall-mounted CO2 fire extinguisher, and its size looks like a common 5 kg CO2 unit; those typically weigh around 13–16 kg total when full.

---

