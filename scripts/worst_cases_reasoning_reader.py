"""
Worst Cases Reasoning Reader
Extract and display detailed reasoning traces for the 30 worst-performing weight estimation cases
across all 3 batches, ranked by log-scale error.
"""

import pandas as pd
import json
from pathlib import Path

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

# Filter for weight category only
weight_df = merged_df[merged_df['type'] == 'weight'].copy()

# List of worst cases per batch
worst_cases = {
    1: [
        'V-weight-image54.jpg',
        'V-weight-image45.jpg',
        'V-weight-image50.jpg',
        'B-weight-image1.jpg',
        'P-weight-image54.jpg',
        'V-weight-image43.jpg',
        'P-weight-image59.jpg',
        'P-weight-image26.jpg',
        'P-weight-image73.jpg',
        'P-weight-image6.jpg',
    ],
    2: [
        'V-weight-image54.jpg',
        'V-weight-image45.jpg',
        'B-weight-image1.jpg',
        'V-weight-image50.jpg',
        'P-weight-image59.jpg',
        'P-weight-image16.jpg',
        'V-weight-image43.jpg',
        'P-weight-image6.jpg',
        'P-weight-image73.jpg',
        'P-weight-image78-pov2.jpg',
    ],
    3: [
        'V-weight-image45.jpg',
        'V-weight-image50.jpg',
        'B-weight-image1.jpg',
        'V-weight-image43.jpg',
        'V-weight-image54.jpg',
        'P-weight-image16.jpg',
        'P-weight-image73.jpg',
        'P-weight-image12.jpg',
        'P-weight-image17.jpg',
        'P-weight-image64.jpg',
    ]
}

# Extract helper function
def extract_weight(note_str):
    """Extract numeric weight from shorthand_notes"""
    if pd.isna(note_str):
        return None
    note_str = str(note_str).strip()
    import re
    match = re.search(r'(\d+(?:\.\d+)?)', note_str)
    if match:
        try:
            return float(match.group(1))
        except:
            return None
    return None

# Generate output file
output_file = data_dir / "worst_cases_reasoning_analysis.md"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Worst 30 Weight-Estimation Cases: Detailed Reasoning Analysis\n\n")
    f.write("This document extracts the full reasoning traces for the 30 worst-performing weight estimation cases,\n")
    f.write("ranked by log-scale error (|log₁₀(pred/GT)|) within each batch.\n\n")
    f.write("---\n\n")
    
    # Process each batch
    for batch_num in [1, 2, 3]:
        f.write(f"## BATCH {batch_num}\n\n")
        
        batch_data = weight_df[weight_df['batch'] == batch_num]
        batch_worst = worst_cases[batch_num]
        
        for rank, filename in enumerate(batch_worst, 1):
            # Find this case in the batch
            matching_rows = batch_data[batch_data['filename'] == filename]
            
            if len(matching_rows) == 0:
                f.write(f"### #{rank}: {filename}\n")
                f.write(f"⚠️ **NOT FOUND IN BATCH DATA**\n\n")
                continue
            
            row = matching_rows.iloc[0]
            
            # Extract values
            gt_weight = extract_weight(row['shorthand_notes'])
            pred_weight = row['openai_num']
            reasoning = str(row['openai_reasoning']) if pd.notna(row['openai_reasoning']) else "No reasoning provided"
            
            # Calculate error metrics
            if pd.notna(pred_weight) and pd.notna(gt_weight) and gt_weight != 0:
                abs_error = abs(pred_weight - gt_weight)
                rel_error = abs_error / gt_weight * 100
                ratio = pred_weight / gt_weight
                direction = "OVER" if pred_weight > gt_weight else "UNDER"
            else:
                abs_error = None
                rel_error = None
                ratio = None
                direction = "N/A"
            
            # Format output
            f.write(f"### #{rank}: `{filename}`\n\n")
            
            f.write("**Prediction Metrics:**\n")
            f.write(f"- Ground Truth: {gt_weight}\n")
            f.write(f"- Prediction: {pred_weight}\n")
            if ratio is not None:
                f.write(f"- Ratio (Pred/GT): {ratio:.2f}× ({direction})\n")
            if rel_error is not None:
                f.write(f"- Relative Error: {rel_error:.1f}%\n")
            f.write("\n")
            
            f.write("**OpenAI Reasoning Trace:**\n")
            f.write(f"> {reasoning}\n\n")
            f.write("---\n\n")

print(f"✓ Output written to: {output_file}")
print(f"\nFile ready for analysis!")
print(f"Total worst cases analyzed: 30 (10 per batch)")
