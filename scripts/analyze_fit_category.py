"""
Analyze FIT category (boolean classification)
Calculate accuracy, precision, recall, F1 scores
"""

import pandas as pd
import numpy as np
from pathlib import Path
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

# Filter for fit category
fit_df = merged_df[merged_df['type'] == 'fit'].copy()

# Convert shorthand notes to boolean (Yes/No)
def parse_bool(val):
    if pd.isna(val):
        return None
    val = str(val).strip().lower()
    if val in ['yes', 'true', '1']:
        return True
    elif val in ['no', 'false', '0']:
        return False
    return None

fit_df['gt_bool'] = fit_df['shorthand_notes'].apply(parse_bool)

models = ['openai', 'gemini', 'gemini-robotics']
model_cols = {
    'openai': 'openai_bool',
    'gemini': 'gemini_bool',
    'gemini-robotics': 'gemini-robotics_bool'
}

# Functions to calculate metrics manually
def calculate_confusion_matrix(y_true, y_pred):
    tp = sum((y_true.iloc[i] == True) and (y_pred.iloc[i] == True) for i in range(len(y_true)))
    tn = sum((y_true.iloc[i] == False) and (y_pred.iloc[i] == False) for i in range(len(y_true)))
    fp = sum((y_true.iloc[i] == False) and (y_pred.iloc[i] == True) for i in range(len(y_true)))
    fn = sum((y_true.iloc[i] == True) and (y_pred.iloc[i] == False) for i in range(len(y_true)))
    return tn, fp, fn, tp

def calculate_accuracy(y_true, y_pred):
    tp, tn, fp, fn = calculate_confusion_matrix(y_true, y_pred)
    total = tp + tn + fp + fn
    return (tp + tn) / total if total > 0 else 0

def calculate_precision(y_true, y_pred):
    tp, tn, fp, fn = calculate_confusion_matrix(y_true, y_pred)
    return tp / (tp + fp) if (tp + fp) > 0 else 0

def calculate_recall(y_true, y_pred):
    tp, tn, fp, fn = calculate_confusion_matrix(y_true, y_pred)
    return tp / (tp + fn) if (tp + fn) > 0 else 0

def calculate_f1(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

# Generate metrics file
metrics_file = data_dir / "fit_metrics_comparison_all_models.txt"

with open(metrics_file, 'w') as f:
    f.write("="*100 + "\n")
    f.write("PERFORMANCE METRICS: FIT CLASSIFICATION (Boolean) - ALL MODELS\n")
    f.write("="*100 + "\n\n")
    
    for model_name in models:
        pred_col = model_cols[model_name]
        
        f.write(f"\n{'='*100}\n")
        f.write(f"{model_name.upper()}\n")
        f.write(f"{'='*100}\n\n")
        
        fit_analysis = fit_df.dropna(subset=['gt_bool', pred_col]).copy()
        
        if len(fit_analysis) == 0:
            f.write("No data available\n\n")
            continue
        
        f.write(f"{'Metric':<30} {'Value':>50}\n")
        f.write("-" * 100 + "\n")
        
        # Overall metrics
        total_samples = len(fit_analysis)
        accuracy = calculate_accuracy(fit_analysis['gt_bool'], fit_analysis[pred_col])
        precision = calculate_precision(fit_analysis['gt_bool'], fit_analysis[pred_col])
        recall = calculate_recall(fit_analysis['gt_bool'], fit_analysis[pred_col])
        f1 = calculate_f1(precision, recall)
        
        f.write(f"{'Total Samples':<30} {total_samples:>50}\n")
        f.write(f"{'Accuracy':<30} {accuracy*100:>50.2f}%\n")
        f.write(f"{'Precision':<30} {precision*100:>50.2f}%\n")
        f.write(f"{'Recall':<30} {recall*100:>50.2f}%\n")
        f.write(f"{'F1 Score':<30} {f1*100:>50.2f}%\n")
        
        # Confusion matrix
        tn, fp, fn, tp = calculate_confusion_matrix(fit_analysis['gt_bool'], fit_analysis[pred_col])
        
        f.write(f"\n{'Confusion Matrix:':<30}\n")
        f.write(f"{'  True Negatives (TN)':<30} {tn:>50}\n")
        f.write(f"{'  False Positives (FP)':<30} {fp:>50}\n")
        f.write(f"{'  False Negatives (FN)':<30} {fn:>50}\n")
        f.write(f"{'  True Positives (TP)':<30} {tp:>50}\n")
        
        # Per-batch breakdown
        f.write(f"\n{'Per-Batch Breakdown:':<30}\n")
        f.write("-" * 100 + "\n")
        
        for batch_num in [1, 2, 3]:
            batch_data = fit_analysis[fit_analysis['batch'] == batch_num]
            
            if len(batch_data) == 0:
                continue
            
            batch_acc = calculate_accuracy(batch_data['gt_bool'], batch_data[pred_col])
            batch_prec = calculate_precision(batch_data['gt_bool'], batch_data[pred_col])
            batch_rec = calculate_recall(batch_data['gt_bool'], batch_data[pred_col])
            batch_f1 = calculate_f1(batch_prec, batch_rec)
            
            f.write(f"\nBatch {batch_num} (N={len(batch_data)}):\n")
            f.write(f"  Accuracy:  {batch_acc*100:>6.2f}%\n")
            f.write(f"  Precision: {batch_prec*100:>6.2f}%\n")
            f.write(f"  Recall:    {batch_rec*100:>6.2f}%\n")
            f.write(f"  F1 Score:  {batch_f1*100:>6.2f}%\n")
        
        f.write("\n\n")

# Generate worst misclassifications analysis
worst_misclass_file = data_dir / "fit_worst_misclassifications.md"

with open(worst_misclass_file, 'w') as f:
    f.write("# FIT Classification: Worst Misclassifications\n\n")
    f.write("Analysis of incorrect predictions (False Positives and False Negatives)\n\n")
    f.write("---\n\n")
    
    for model_name in models:
        pred_col = model_cols[model_name]
        reasoning_col = f'{model_name}_reasoning'
        
        f.write(f"# {model_name.upper()}\n\n")
        
        fit_analysis = fit_df.dropna(subset=['gt_bool', pred_col, reasoning_col]).copy()
        
        # Find misclassifications
        fit_analysis['is_correct'] = fit_analysis['gt_bool'] == fit_analysis[pred_col]
        misclassifications = fit_analysis[~fit_analysis['is_correct']]
        
        if len(misclassifications) == 0:
            f.write("Perfect classification! No misclassifications.\n\n")
            continue
        
        # False Positives (predicted True, actual False)
        false_positives = misclassifications[(misclassifications[pred_col] == True) & (misclassifications['gt_bool'] == False)]
        
        f.write(f"## False Positives (Predicted YES, Actually NO): {len(false_positives)} cases\n\n")
        
        if len(false_positives) > 0:
            for idx, (_, row) in enumerate(false_positives.head(10).iterrows(), 1):
                f.write(f"### {idx}. `{row['filename']}`\n\n")
                f.write(f"**Ground Truth:** NO (doesn't fit)\n")
                f.write(f"**Prediction:** YES (predicted it fits)\n\n")
                f.write(f"**Reasoning:**\n> {str(row[reasoning_col])}\n\n")
                f.write("---\n\n")
        else:
            f.write("No false positives.\n\n")
        
        # False Negatives (predicted False, actual True)
        false_negatives = misclassifications[(misclassifications[pred_col] == False) & (misclassifications['gt_bool'] == True)]
        
        f.write(f"## False Negatives (Predicted NO, Actually YES): {len(false_negatives)} cases\n\n")
        
        if len(false_negatives) > 0:
            for idx, (_, row) in enumerate(false_negatives.head(10).iterrows(), 1):
                f.write(f"### {idx}. `{row['filename']}`\n\n")
                f.write(f"**Ground Truth:** YES (fits)\n")
                f.write(f"**Prediction:** NO (predicted it doesn't fit)\n\n")
                f.write(f"**Reasoning:**\n> {str(row[reasoning_col])}\n\n")
                f.write("---\n\n")
        else:
            f.write("No false negatives.\n\n")
        
        f.write("\n")

print(f"✓ FIT category analysis complete!")
print(f"\nGenerated files:")
print(f"  - fit_metrics_comparison_all_models.txt")
print(f"  - fit_worst_misclassifications.md")
