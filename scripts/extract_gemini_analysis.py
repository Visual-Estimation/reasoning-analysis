"""
Extract reasoning traces for Gemini models and calculate metrics with/without worst 10
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

# Load worst 10 per batch
with open(data_dir / "worst_10_per_batch_gemini_models.pkl", 'rb') as f:
    worst_10_per_batch = pickle.load(f)

# Generate reasoning markdown file
reasoning_file = data_dir / "gemini_models_worst_cases_reasoning.md"

with open(reasoning_file, 'w', encoding='utf-8') as f:
    f.write("# Gemini & Gemini-Robotics Weight-Estimation: Worst 30 Cases Reasoning Analysis\n\n")
    f.write("Worst 10 per batch for each model, ranked by |log₁₀(pred/GT)|\n\n")
    f.write("---\n\n")
    
    # Process each model
    for model_name in ['gemini', 'gemini-robotics']:
        reasoning_col = f'{model_name}_reasoning'
        pred_col = f'{model_name}_num'
        
        f.write(f"# {model_name.upper()} MODEL\n\n")
        
        # Process each batch
        for batch_num in [1, 2, 3]:
            f.write(f"## BATCH {batch_num}\n\n")
            
            batch_data = weight_df[weight_df['batch'] == batch_num]
            batch_worst = worst_10_per_batch[model_name][batch_num]
            
            for rank, (idx, row_worst) in enumerate(batch_worst.iterrows(), 1):
                filename = row_worst['filename']
                
                # Find matching row
                matching_rows = batch_data[batch_data['filename'] == filename]
                
                if len(matching_rows) == 0:
                    f.write(f"### #{rank}: {filename}\n")
                    f.write(f"⚠️ **NOT FOUND**\n\n")
                    continue
                
                row = matching_rows.iloc[0]
                
                # Extract values
                gt_weight = extract_weight(row['shorthand_notes'])
                pred_weight = row[pred_col]
                reasoning = str(row[reasoning_col]) if pd.notna(row[reasoning_col]) else "No reasoning provided"
                
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
                
                f.write("**Reasoning Trace:**\n")
                f.write(f"> {reasoning}\n\n")
                f.write("---\n\n")

print(f"✓ Reasoning traces saved to: {reasoning_file}")

# Now calculate metrics with/without worst 10 per batch
# Models to analyze
models_config = {
    'gemini': {'pred_col': 'gemini_num'},
    'gemini-robotics': {'pred_col': 'gemini-robotics_num'}
}

def calc_metrics(df, pred_col):
    """Calculate error metrics"""
    abs_error = np.abs(df[pred_col] - df['gt_weight'])
    rel_error = np.abs((df[pred_col] - df['gt_weight']) / df['gt_weight']) * 100
    
    mape = np.mean(rel_error)
    mae = np.mean(abs_error)
    rmse = np.sqrt(np.mean(abs_error**2))
    median_ae = np.median(abs_error)
    std_error = np.std(abs_error)
    
    within_10 = (rel_error <= 10).sum() / len(df) * 100
    within_25 = (rel_error <= 25).sum() / len(df) * 100
    within_50 = (rel_error <= 50).sum() / len(df) * 100
    
    overest_rate = (df[pred_col] > df['gt_weight']).sum() / len(df) * 100
    bias = np.mean(df[pred_col] - df['gt_weight'])
    corr = df[pred_col].corr(df['gt_weight'])
    
    return {
        'N': len(df),
        'MAPE (%)': mape,
        'MAE': mae,
        'RMSE': rmse,
        'Median AE': median_ae,
        'Std Dev': std_error,
        'Within ±10%': within_10,
        'Within ±25%': within_25,
        'Within ±50%': within_50,
        'Overestimate %': overest_rate,
        'Bias': bias,
        'Correlation': corr,
    }

# Generate metrics file
metrics_file = data_dir / "gemini_models_metrics_comparison.txt"

with open(metrics_file, 'w') as f:
    f.write("="*100 + "\n")
    f.write("PERFORMANCE METRICS: GEMINI & GEMINI-ROBOTICS - WITH vs WITHOUT TOP 10 WORST CASES PER BATCH\n")
    f.write("="*100 + "\n\n")
    
    for model_name, model_info in models_config.items():
        pred_col = model_info['pred_col']
        
        f.write(f"\n{'='*100}\n")
        f.write(f"{model_name.upper()}\n")
        f.write(f"{'='*100}\n\n")
        
        weight_analysis = weight_df.dropna(subset=['gt_weight', pred_col]).copy()
        
        for batch_num in [1, 2, 3]:
            f.write(f"\n{'-'*100}\n")
            f.write(f"BATCH {batch_num}\n")
            f.write(f"{'-'*100}\n\n")
            
            batch_data = weight_analysis[weight_analysis['batch'] == batch_num].copy()
            
            # All data
            metrics_all = calc_metrics(batch_data, pred_col)
            
            # Filtered data (without worst cases)
            worst_for_batch = worst_10_per_batch[model_name][batch_num]['filename'].tolist()
            batch_filtered = batch_data[~batch_data['filename'].isin(worst_for_batch)].copy()
            metrics_filtered = calc_metrics(batch_filtered, pred_col)
            
            f.write(f"{'Metric':<25} {'WITH All (N={})':>30} {'WITHOUT Worst 10 (N={})':>30} {'Change':>15}\n".format(
                metrics_all['N'], metrics_filtered['N']))
            f.write("-" * 100 + "\n")
            
            for key in metrics_all.keys():
                if key == 'N':
                    continue
                
                all_val = metrics_all[key]
                filt_val = metrics_filtered[key]
                
                if isinstance(all_val, (int, float)):
                    if all_val != 0:
                        pct_change = ((filt_val - all_val) / abs(all_val)) * 100
                        change_str = f"{pct_change:+.1f}%"
                    else:
                        change_str = "N/A"
                    
                    if isinstance(all_val, float):
                        f.write(f"{key:<25} {all_val:>30.2f} {filt_val:>30.2f} {change_str:>15}\n")
                    else:
                        f.write(f"{key:<25} {all_val:>30} {filt_val:>30} {change_str:>15}\n")

print(f"✓ Metrics saved to: {metrics_file}")
print("\nDone! Files generated:")
print(f"  - {reasoning_file}")
print(f"  - {metrics_file}")
