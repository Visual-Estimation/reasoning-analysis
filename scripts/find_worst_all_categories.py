"""
Comprehensive analysis for all categories (angle, stability, fit, liquid_volume)
For all 3 models: OpenAI, Gemini, Gemini-Robotics
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re
import pickle

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

# Helper function to extract numeric values
def extract_numeric(note_str):
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

# Categories and their configurations
categories = {
    'angle': {'pred_models': {'openai': 'openai_num', 'gemini': 'gemini_num', 'gemini-robotics': 'gemini-robotics_num'}},
    'stability': {'pred_models': {'openai': 'openai_num', 'gemini': 'gemini_num', 'gemini-robotics': 'gemini-robotics_num'}},
    'liquid_volume': {'pred_models': {'openai': 'openai_num', 'gemini': 'gemini_num', 'gemini-robotics': 'gemini-robotics_num'}},
    'fit': {'pred_models': {'openai': 'openai_bool', 'gemini': 'gemini_bool', 'gemini-robotics': 'gemini-robotics_bool'}},  # Boolean
}

# Store worst 10 per category, model, batch
all_worst_10 = {}

# Process each category
for category in categories.keys():
    print(f"\n{'='*80}")
    print(f"PROCESSING CATEGORY: {category.upper()}")
    print(f"{'='*80}")
    
    category_df = merged_df[merged_df['type'] == category].copy()
    
    # Extract ground truth
    category_df['gt_value'] = category_df['shorthand_notes'].apply(extract_numeric)
    
    all_worst_10[category] = {}
    
    # Process each model
    for model_name, pred_col in categories[category]['pred_models'].items():
        all_worst_10[category][model_name] = {}
        
        category_df[f'{model_name}_pred'] = category_df[pred_col]
        
        # For fit category, skip GT extraction (it's boolean)
        if category == 'fit':
            category_clean = category_df.dropna(subset=[f'{model_name}_pred']).copy()
            
            # For boolean, can't use error ratio - skip worst 10 analysis
            print(f"\n  {model_name}: SKIPPING (fit is boolean classification, not numeric)")
            continue
        
        category_clean = category_df.dropna(subset=['gt_value', f'{model_name}_pred']).copy()
        
        # For stability/angle: might have underestimation too (unlike weight)
        for batch_num in [1, 2, 3]:
            batch_data = category_clean[category_clean['batch'] == batch_num].copy()
            
            if len(batch_data) == 0:
                print(f"  {model_name} Batch {batch_num}: NO DATA")
                all_worst_10[category][model_name][batch_num] = pd.DataFrame()
                continue
            
            # Calculate errors - use both absolute and signed
            batch_data['abs_error'] = abs(batch_data[f'{model_name}_pred'] - batch_data['gt_value'])
            batch_data['log_error'] = np.log10(np.abs(batch_data[f'{model_name}_pred'] / (batch_data['gt_value'] + 1e-10)) + 1e-10)
            
            # Get top 10 by absolute log error
            top10 = batch_data.nlargest(10, 'log_error')[['filename', f'{model_name}_pred', 'gt_value', 'abs_error']].copy()
            
            all_worst_10[category][model_name][batch_num] = top10
            
            print(f"  {model_name} Batch {batch_num}: {len(top10)} worst cases found")
            for rank, (idx, row) in enumerate(top10.head(3).iterrows(), 1):
                ratio = row[f'{model_name}_pred'] / row['gt_value'] if row['gt_value'] != 0 else np.inf
                direction = "OVER" if ratio > 1 else "UNDER"
                print(f"    #{rank}. {row['filename']}: {ratio:.2f}× {direction}")

# Save to pickle for next script
with open(data_dir / "worst_10_all_categories.pkl", 'wb') as f:
    pickle.dump(all_worst_10, f)

print(f"\n✓ Worst 10 cases for all categories identified and saved")
