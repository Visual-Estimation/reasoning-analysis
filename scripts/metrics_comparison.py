"""
Metrics Comparison: With vs Without Worst 30 Cases
Calculate performance metrics (MAPE, MAE, RMSE, etc.) before and after removing the 30 worst cases
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

# Filter for weight category only
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
weight_df['predicted_weight'] = weight_df['openai_num']
weight_clean_df = weight_df.dropna(subset=['gt_weight', 'predicted_weight']).copy()

# Worst cases to exclude
worst_cases = {
    1: [
        'V-weight-image54.jpg', 'V-weight-image45.jpg', 'V-weight-image50.jpg',
        'B-weight-image1.jpg', 'P-weight-image54.jpg', 'V-weight-image43.jpg',
        'P-weight-image59.jpg', 'P-weight-image26.jpg', 'P-weight-image73.jpg', 'P-weight-image6.jpg',
    ],
    2: [
        'V-weight-image54.jpg', 'V-weight-image45.jpg', 'B-weight-image1.jpg',
        'V-weight-image50.jpg', 'P-weight-image59.jpg', 'P-weight-image16.jpg',
        'V-weight-image43.jpg', 'P-weight-image6.jpg', 'P-weight-image73.jpg', 'P-weight-image78-pov2.jpg',
    ],
    3: [
        'V-weight-image45.jpg', 'V-weight-image50.jpg', 'B-weight-image1.jpg',
        'V-weight-image43.jpg', 'V-weight-image54.jpg', 'P-weight-image16.jpg',
        'P-weight-image73.jpg', 'P-weight-image12.jpg', 'P-weight-image17.jpg', 'P-weight-image64.jpg',
    ]
}

# Function to calculate metrics
def calc_metrics(df):
    """Calculate comprehensive error metrics"""
    
    abs_error = np.abs(df['predicted_weight'] - df['gt_weight'])
    rel_error = np.abs((df['predicted_weight'] - df['gt_weight']) / df['gt_weight']) * 100
    
    # MAPE (Mean Absolute Percentage Error) - handling division by zero
    mape = np.mean(rel_error)
    
    # MAE (Mean Absolute Error)
    mae = np.mean(abs_error)
    
    # RMSE (Root Mean Square Error)
    rmse = np.sqrt(np.mean(abs_error**2))
    
    # Median Absolute Error
    median_ae = np.median(abs_error)
    
    # Standard deviation of errors
    std_error = np.std(abs_error)
    
    # Percentage of predictions within ±10%, ±25%, ±50%
    within_10 = (rel_error <= 10).sum() / len(df) * 100
    within_25 = (rel_error <= 25).sum() / len(df) * 100
    within_50 = (rel_error <= 50).sum() / len(df) * 100
    
    # Overestimation rate
    overest_rate = (df['predicted_weight'] > df['gt_weight']).sum() / len(df) * 100
    
    # Bias (mean signed error)
    bias = np.mean(df['predicted_weight'] - df['gt_weight'])
    
    # Correlation
    corr = df['predicted_weight'].corr(df['gt_weight'])
    
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

# Calculate metrics for all data and filtered data
results = {}

for batch_num in [1, 2, 3]:
    batch_data = weight_clean_df[weight_clean_df['batch'] == batch_num].copy()
    
    # All data
    metrics_all = calc_metrics(batch_data)
    
    # Filtered data (without worst cases)
    worst_for_batch = worst_cases[batch_num]
    batch_filtered = batch_data[~batch_data['filename'].isin(worst_for_batch)].copy()
    metrics_filtered = calc_metrics(batch_filtered)
    
    results[batch_num] = {
        'all': metrics_all,
        'filtered': metrics_filtered,
    }

# Generate output report
output_file = data_dir / "metrics_comparison_with_without_worst.txt"

with open(output_file, 'w') as f:
    f.write("="*100 + "\n")
    f.write("PERFORMANCE METRICS: WITH vs WITHOUT TOP 10 WORST CASES PER BATCH\n")
    f.write("="*100 + "\n\n")
    
    for batch_num in [1, 2, 3]:
        f.write(f"\n{'='*100}\n")
        f.write(f"BATCH {batch_num}\n")
        f.write(f"{'='*100}\n\n")
        
        all_metrics = results[batch_num]['all']
        filt_metrics = results[batch_num]['filtered']
        
        f.write(f"{'Metric':<25} {'WITH All (N={})':>30} {'WITHOUT Worst 10 (N={})':>30} {'Change':>15}\n".format(
            all_metrics['N'], filt_metrics['N']))
        f.write("-" * 100 + "\n")
        
        for key in all_metrics.keys():
            if key == 'N':
                continue
            
            all_val = all_metrics[key]
            filt_val = filt_metrics[key]
            
            # Calculate change
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
    
    # Overall summary
    f.write(f"\n\n{'='*100}\n")
    f.write("OVERALL SUMMARY (ALL BATCHES COMBINED)\n")
    f.write(f"{'='*100}\n\n")
    
    # Combine all data
    all_combined = weight_clean_df.copy()
    all_metrics_combined = calc_metrics(all_combined)
    
    # Filter combined
    exclude_list = []
    for batch_num in [1, 2, 3]:
        exclude_list.extend(worst_cases[batch_num])
    combined_filtered = all_combined[~all_combined['filename'].isin(exclude_list)].copy()
    filt_metrics_combined = calc_metrics(combined_filtered)
    
    f.write(f"{'Metric':<25} {'WITH All (N={})':>30} {'WITHOUT Worst 30 (N={})':>30} {'Change':>15}\n".format(
        all_metrics_combined['N'], filt_metrics_combined['N']))
    f.write("-" * 100 + "\n")
    
    for key in all_metrics_combined.keys():
        if key == 'N':
            continue
        
        all_val = all_metrics_combined[key]
        filt_val = filt_metrics_combined[key]
        
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
    
    f.write("\n\n" + "="*100 + "\n")
    f.write("INTERPRETATION\n")
    f.write("="*100 + "\n\n")
    
    f.write("KEY METRICS EXPLAINED:\n")
    f.write("- MAPE (Mean Absolute Percentage Error): Average % deviation from ground truth\n")
    f.write("- MAE (Mean Absolute Error): Average absolute deviation\n")
    f.write("- RMSE (Root Mean Square Error): Penalizes larger errors more heavily\n")
    f.write("- Median AE: Middle value of absolute errors (robust to outliers)\n")
    f.write("- Within ±X%: % of predictions within X% of ground truth\n")
    f.write("- Overestimate %: % of predictions that exceed ground truth\n")
    f.write("- Bias: Mean signed error (positive = consistent overestimation)\n")
    f.write("- Correlation: Strength of linear relationship between pred and truth\n\n")
    
    f.write("OBSERVATIONS:\n")
    mape_improvement = ((all_metrics_combined['MAPE (%)'] - filt_metrics_combined['MAPE (%)']) / all_metrics_combined['MAPE (%)']) * 100
    f.write(f"- MAPE improves by {mape_improvement:.1f}% when removing worst 30 cases\n")
    f.write(f"- Original MAPE: {all_metrics_combined['MAPE (%)']:.1f}%\n")
    f.write(f"- Filtered MAPE: {filt_metrics_combined['MAPE (%)']:.1f}%\n")
    f.write(f"- Removing {exclude_list.__len__()} cases ({exclude_list.__len__()/all_metrics_combined['N']*100:.1f}% of data) improves MAPE by {mape_improvement:.1f}%\n")

print(f"✓ Report saved to: {output_file}")
print(f"\n" + open(output_file).read())
