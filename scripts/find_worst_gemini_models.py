"""
Identify worst 10 cases per batch for Gemini and Gemini-Robotics models
Ranked by |log₁₀(pred/GT)|
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re

# Setup
data_dir = Path(r"c:\Users\prath\Downloads\ve")

# Load all batch CSVs
batch_dfs = {}
for i in range(1, 4):
    batch_dfs[f"batch_{i}"] = pd.read_csv(data_dir / f"batch_{i}.csv")

# Load ground truth
gt_df = pd.read_csv(data_dir / "groundtruth.csv", on_bad_lines='skip', engine='python')

# Merge batches with ground truth
combined_data = []
for batch_name, batch_df in batch_dfs.items():
    batch_num = int(batch_name.split('_')[1])
    batch_df_copy = batch_df.copy()
    batch_df_copy['batch'] = batch_num
    combined_data.append(batch_df_copy)

all_batches_df = pd.concat(combined_data, ignore_index=True)
merged_df = all_batches_df.merge(
    gt_df[['filename', 'type', 'custom_prompt', 'shorthand_notes']],
    on='filename',
    how='left'
)

# Filter for weight category
weight_df = merged_df[merged_df['type'] == 'weight'].copy()

# Extract weight values
def extract_weight(note_str):
    if pd.isna(note_str):
        return None
    note_str = str(note_str).strip()
    match = re.search(r'(\d+(?:\.\d+)?)', note_str)
    if match:
        try:
            return float(match.group(1))
        except:
            return None
    return None

weight_df['gt_weight'] = weight_df['shorthand_notes'].apply(extract_weight)

# Find worst 10 for each model per batch
models = {
    'gemini': 'gemini_num',
    'gemini-robotics': 'gemini-robotics_num'
}

worst_10_per_batch = {}

for model_name, pred_col in models.items():
    worst_10_per_batch[model_name] = {}
    
    weight_df[f'{model_name}_pred'] = weight_df[pred_col]
    weight_clean = weight_df.dropna(subset=['gt_weight', f'{model_name}_pred']).copy()
    
    for batch_num in [1, 2, 3]:
        batch_data = weight_clean[weight_clean['batch'] == batch_num].copy()
        
        # Calculate errors
        batch_data['abs_error'] = abs(batch_data[f'{model_name}_pred'] - batch_data['gt_weight'])
        batch_data['log_error'] = np.log10(np.abs(batch_data[f'{model_name}_pred'] / batch_data['gt_weight']) + 1e-10)
        
        # Get top 10 by log error
        top10 = batch_data.nlargest(10, 'log_error')[['filename', f'{model_name}_pred', 'gt_weight', 'abs_error']].copy()
        
        worst_10_per_batch[model_name][batch_num] = top10
        
        print(f"\n{model_name.upper()} - BATCH {batch_num} - TOP 10 WORST:")
        print("-" * 80)
        for rank, (idx, row) in enumerate(top10.iterrows(), 1):
            ratio = row[f'{model_name}_pred'] / row['gt_weight']
            direction = "OVER" if ratio > 1 else "UNDER"
            print(f"{rank:2d}. {row['filename']:30s} — {ratio:6.1f}× {direction}")

# Save to pickle for next script
import pickle
with open(data_dir / "worst_10_per_batch_gemini_models.pkl", 'wb') as f:
    pickle.dump(worst_10_per_batch, f)

print("\n✓ Worst 10 cases identified and saved for reasoning extraction")
