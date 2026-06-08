"""
Extract reasoning and calculate metrics for all categories (except fit)
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

# Load worst 10 cases
with open(data_dir / "worst_10_all_categories.pkl", 'rb') as f:
    all_worst_10 = pickle.load(f)

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

def calc_metrics(df, pred_col, gt_col='gt_value'):
    """Calculate error metrics for numeric predictions"""
    valid_df = df.dropna(subset=[pred_col, gt_col])
    if len(valid_df) == 0:
        return None
    
    abs_error = np.abs(valid_df[pred_col] - valid_df[gt_col])
    rel_error = np.abs((valid_df[pred_col] - valid_df[gt_col]) / (valid_df[gt_col] + 1e-10)) * 100
    
    mape = np.mean(rel_error[np.isfinite(rel_error)])  # Handle inf values
    mae = np.mean(abs_error)
    rmse = np.sqrt(np.mean(abs_error**2))
    median_ae = np.median(abs_error)
    std_error = np.std(abs_error)
    
    within_10 = (rel_error <= 10).sum() / len(valid_df) * 100
    within_25 = (rel_error <= 25).sum() / len(valid_df) * 100
    within_50 = (rel_error <= 50).sum() / len(valid_df) * 100
    
    overest_rate = (valid_df[pred_col] > valid_df[gt_col]).sum() / len(valid_df) * 100
    bias = np.mean(valid_df[pred_col] - valid_df[gt_col])
    corr = valid_df[pred_col].corr(valid_df[gt_col])
    
    return {
        'N': len(valid_df),
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

# Categories to process (excluding fit)
categories = ['angle', 'stability', 'liquid_volume']
models = ['openai', 'gemini', 'gemini-robotics']
model_pred_cols = {
    'openai': 'openai_num',
    'gemini': 'gemini_num',
    'gemini-robotics': 'gemini-robotics_num'
}

# Generate comprehensive reasoning and metrics files
for category in categories:
    print(f"\nProcessing {category.upper()}...")
    
    # Create reasoning file
    reasoning_file = data_dir / f"{category}_worst_cases_reasoning_all_models.md"
    metrics_file = data_dir / f"{category}_metrics_comparison_all_models.txt"
    
    with open(reasoning_file, 'w', encoding='utf-8') as f:
        f.write(f"# {category.upper()} Estimation: Worst 30 Cases Reasoning Analysis\n\n")
        f.write("Worst 10 per batch for each model (OpenAI, Gemini, Gemini-Robotics), ranked by |log₁₀(pred/GT)|\n\n")
        f.write("---\n\n")
        
        category_df = merged_df[merged_df['type'] == category].copy()
        category_df['gt_value'] = category_df['shorthand_notes'].apply(extract_numeric)
        
        for model_name in models:
            pred_col = model_pred_cols[model_name]
            reasoning_col = f'{model_name}_reasoning'
            
            f.write(f"# {model_name.upper()} MODEL\n\n")
            
            for batch_num in [1, 2, 3]:
                f.write(f"## BATCH {batch_num}\n\n")
                
                worst_df = all_worst_10[category][model_name][batch_num]
                if len(worst_df) == 0:
                    f.write("No data available\n\n")
                    continue
                
                batch_data = category_df[category_df['batch'] == batch_num]
                
                for rank, (idx, row_worst) in enumerate(worst_df.iterrows(), 1):
                    filename = row_worst['filename']
                    matching_rows = batch_data[batch_data['filename'] == filename]
                    
                    if len(matching_rows) == 0:
                        f.write(f"### #{rank}: {filename}\n⚠️ NOT FOUND\n\n")
                        continue
                    
                    row = matching_rows.iloc[0]
                    gt_val = row['gt_value']
                    pred_val = row[pred_col]
                    reasoning = str(row[reasoning_col]) if pd.notna(row[reasoning_col]) else "No reasoning"
                    
                    if pd.notna(pred_val) and pd.notna(gt_val) and gt_val != 0:
                        ratio = pred_val / gt_val
                        direction = "OVER" if ratio > 1 else "UNDER"
                        error_pct = abs((pred_val - gt_val) / gt_val) * 100
                    else:
                        ratio = None
                        direction = "N/A"
                        error_pct = None
                    
                    f.write(f"### #{rank}: `{filename}`\n\n")
                    f.write("**Prediction Metrics:**\n")
                    f.write(f"- Ground Truth: {gt_val}\n")
                    f.write(f"- Prediction: {pred_val}\n")
                    if ratio is not None:
                        f.write(f"- Ratio (Pred/GT): {ratio:.2f}× ({direction})\n")
                        f.write(f"- Error: {error_pct:.1f}%\n")
                    f.write("\n")
                    f.write("**Reasoning Trace:**\n")
                    f.write(f"> {reasoning}\n\n")
                    f.write("---\n\n")
    
    # Generate metrics file
    with open(metrics_file, 'w') as f:
        f.write("="*100 + "\n")
        f.write(f"PERFORMANCE METRICS: {category.upper()} - WITH vs WITHOUT TOP 10 WORST CASES PER BATCH\n")
        f.write("="*100 + "\n\n")
        
        for model_name in models:
            pred_col = model_pred_cols[model_name]
            
            f.write(f"\n{'='*100}\n")
            f.write(f"{model_name.upper()}\n")
            f.write(f"{'='*100}\n\n")
            
            category_analysis = category_df.dropna(subset=['gt_value', pred_col]).copy()
            
            for batch_num in [1, 2, 3]:
                f.write(f"\n{'-'*100}\n")
                f.write(f"BATCH {batch_num}\n")
                f.write(f"{'-'*100}\n\n")
                
                batch_data = category_analysis[category_analysis['batch'] == batch_num].copy()
                
                if len(batch_data) == 0:
                    f.write("No data available\n\n")
                    continue
                
                # All data
                metrics_all = calc_metrics(batch_data, pred_col)
                
                if metrics_all is None:
                    f.write("Insufficient data for metrics calculation\n\n")
                    continue
                
                # Filtered data
                worst_for_batch = all_worst_10[category][model_name][batch_num]['filename'].tolist()
                batch_filtered = batch_data[~batch_data['filename'].isin(worst_for_batch)].copy()
                metrics_filtered = calc_metrics(batch_filtered, pred_col)
                
                if metrics_filtered is None:
                    f.write("Insufficient filtered data\n\n")
                    continue
                
                f.write(f"{'Metric':<25} {'WITH All (N={})':>30} {'WITHOUT Worst 10 (N={})':>30} {'Change':>15}\n".format(
                    metrics_all['N'], metrics_filtered['N']))
                f.write("-" * 100 + "\n")
                
                for key in metrics_all.keys():
                    if key == 'N':
                        continue
                    
                    all_val = metrics_all[key]
                    filt_val = metrics_filtered[key]
                    
                    if isinstance(all_val, (int, float)):
                        if all_val != 0 and not np.isnan(all_val):
                            pct_change = ((filt_val - all_val) / abs(all_val)) * 100
                            change_str = f"{pct_change:+.1f}%"
                        else:
                            change_str = "N/A"
                        
                        if isinstance(all_val, float):
                            f.write(f"{key:<25} {all_val:>30.2f} {filt_val:>30.2f} {change_str:>15}\n")

print(f"\n✓ All analysis files generated!")
print(f"\nGenerated files:")
for cat in categories:
    print(f"  - {cat}_worst_cases_reasoning_all_models.md")
    print(f"  - {cat}_metrics_comparison_all_models.txt")
