import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
import requests

# Setup directory paths
data_dir = Path(r"c:\Users\prath\Downloads\ve\data")

# Configuration of Jobs
GEMINI_ROBOTICS_JOBS = {
    1: "batches/3salref2s9g8dyn7s9l1dlovy8xrygqcbiqg",
    2: "batches/514sudec8mavkf940tolzcfu3jok00vqy517",
    3: "batches/xjr0c0cubo8fch6ccqva7xm5og034g2k7i6i",
}

def revert_batch_csvs():
    """
    Cleans up the original batch_*.csv files by dropping any extra reasoning trace columns.
    """
    print("\n" + "="*80)
    print("REVERTING EXTRA COLUMNS FROM BATCH CSV FILES")
    print("="*80)
    
    cols_to_drop = ["openai_reasoning_trace", "gemini_reasoning_trace", "gemini-robotics_reasoning_trace"]
    
    for batch_num in [1, 2, 3]:
        csv_path = data_dir / f"batch_{batch_num}.csv"
        if not csv_path.exists():
            print(f"File {csv_path.name} not found. Skipping.")
            continue
            
        try:
            df = pd.read_csv(csv_path)
            cols_present = [col for col in cols_to_drop if col in df.columns]
            if cols_present:
                print(f"Dropping columns {cols_present} from {csv_path.name}...")
                df = df.drop(columns=cols_present)
                df.to_csv(csv_path, index=False)
                print(f"Successfully reverted {csv_path.name} to original schema.")
            else:
                print(f"{csv_path.name} is already clean (no extra columns found).")
        except Exception as e:
            print(f"Error reverting {csv_path.name}: {e}")

def extract_reasoning_and_value(text):
    """
    Cleans markdown wraps from text, parses nested JSON, and extracts
    reasoning and final_answer.
    """
    if not text:
        return None, None
        
    text_cleaned = text.strip()
    if text_cleaned.startswith("```json"):
        text_cleaned = text_cleaned[7:]
    elif text_cleaned.startswith("```"):
        text_cleaned = text_cleaned[3:]
        
    if text_cleaned.endswith("```"):
        text_cleaned = text_cleaned[:-3]
        
    text_cleaned = text_cleaned.strip()
    
    try:
        data = json.loads(text_cleaned)
        reasoning = data.get("reasoning")
        final_answer = data.get("final_answer")
        return reasoning, final_answer
    except Exception as e:
        # Return raw text if JSON parsing fails
        return None, text

def retrieve_gemini_robotics():
    print("\n" + "="*80)
    print("RETRIEVING GEMINI-ROBOTICS (AI STUDIO) BATCH RESULTS")
    print("="*80)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable is not set. Skipping Gemini-Robotics retrieval.")
        return {}
        
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Error initializing Google GenAI client (Gemini-Robotics): {e}")
        print("We will attempt to retrieve via REST API as a fallback.")
        client = None
        
    for batch_num, job_id in GEMINI_ROBOTICS_JOBS.items():
        print(f"\nProcessing Batch {batch_num}...")
        try:
            content = None
            if client:
                try:
                    job = client.batches.get(name=job_id)
                    print(f"  Job name: {job.name}")
                    print(f"  State: {job.state}")
                    
                    output_file = None
                    if hasattr(job, 'output_info') and job.output_info:
                        output_file = getattr(job.output_info, 'output_file', None)
                    elif hasattr(job, 'dest') and job.dest:
                        output_file = job.dest
                        
                    if output_file:
                        print(f"  Downloading output file {output_file} from File API...")
                        file_to_download = output_file
                        if hasattr(output_file, 'file_name') and getattr(output_file, 'file_name'):
                            file_to_download = getattr(output_file, 'file_name')
                        elif isinstance(output_file, dict) and 'file_name' in output_file:
                            file_to_download = output_file['file_name']
                        elif not isinstance(output_file, str):
                            file_to_download = str(output_file)
                            
                        content_bytes = client.files.download(file=file_to_download)
                        content = content_bytes.decode('utf-8')
                except Exception as sdk_err:
                    print(f"  GenAI SDK method failed: {sdk_err}. Trying REST API fallback...")
                    client = None
                    
            if not client or not content:
                job_url = f"https://generativelanguage.googleapis.com/v1beta/{job_id}?key={api_key}"
                resp = requests.get(job_url)
                if resp.status_code != 200:
                    print(f"  Failed to get batch job details via REST (HTTP {resp.status_code}): {resp.text}")
                    continue
                    
                job_json = resp.json()
                metadata = job_json.get('metadata', {})
                response_data = job_json.get('response', {})
                
                print(f"  REST Job Status State: {metadata.get('state')}")
                
                output_file = None
                if 'responsesFile' in response_data:
                    output_file = response_data['responsesFile']
                elif 'output' in metadata and 'responsesFile' in metadata['output']:
                    output_file = metadata['output']['responsesFile']
                elif 'responsesFile' in metadata:
                    output_file = metadata['responsesFile']
                elif 'outputFile' in metadata:
                    output_file = metadata['outputFile']
                elif 'outputMetadata' in job_json and 'outputFile' in job_json['outputMetadata']:
                    output_file = job_json['outputMetadata']['outputFile']
                elif 'dest' in job_json:
                    output_file = job_json['dest']
                    
                if not output_file:
                    print(f"  No explicit output file found in REST response.")
                    continue
                    
                print(f"  Downloading output file {output_file} via REST API...")
                download_url = f"https://generativelanguage.googleapis.com/v1beta/{output_file}:download?alt=media&key={api_key}"
                download_resp = requests.get(download_url)
                
                if download_resp.status_code != 200:
                    download_url_fallback = f"https://generativelanguage.googleapis.com/v1beta/{output_file}:download?key={api_key}"
                    download_resp = requests.get(download_url_fallback)
                    
                if download_resp.status_code != 200:
                    print(f"  Standard download failed (HTTP {download_resp.status_code}). Trying metadata-fallback...")
                    metadata_url = f"https://generativelanguage.googleapis.com/v1beta/{output_file}?key={api_key}"
                    meta_resp = requests.get(metadata_url)
                    if meta_resp.status_code == 200:
                        meta_json = meta_resp.json()
                        download_uri = meta_json.get('uri') or meta_json.get('downloadUri')
                        if download_uri:
                            download_resp = requests.get(f"{download_uri}?key={api_key}")
                
                if download_resp.status_code != 200:
                    print(f"  Failed to download file via REST (HTTP {download_resp.status_code})")
                    continue
                    
                content = download_resp.text
                
            if not content:
                print(f"  Failed to retrieve content for Batch {batch_num}")
                continue
                
            extracted_records = []
            
            for line_idx, line in enumerate(content.strip().split("\n")):
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    key = record.get("key", "")
                    
                    if "|" in key:
                        filename, prompt = key.split("|", 1)
                    else:
                        filename = key
                        prompt = ""
                    
                    response_obj = record.get("response", {})
                    candidates = response_obj.get("candidates", [])
                    
                    reasoning_trace = None
                    predicted_value = None
                    
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        for part in parts:
                            if "text" in part:
                                raw_text = part.get("text")
                                r_trace, p_val = extract_reasoning_and_value(raw_text)
                                if r_trace:
                                    reasoning_trace = r_trace
                                if p_val is not None:
                                    predicted_value = p_val
                    
                    extracted_records.append({
                        "filename": filename,
                        "prompt": prompt,
                        "reasoning_trace": reasoning_trace,
                        "predicted_value": predicted_value
                    })
                except Exception as e:
                    print(f"  Skipping row {line_idx} in Batch {batch_num} output due to parsing error: {e}")
                    
            print(f"  Successfully extracted {len(extracted_records)} reasoning traces.")
            
            # Save standalone JSON file
            json_path = data_dir / f"gemini_robotics_reasoning_traces_batch_{batch_num}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(extracted_records, f, indent=2, ensure_ascii=False)
            print(f"  [SUCCESS] Saved standalone JSON: {json_path.name}")
            
            # Save standalone CSV file
            csv_path = data_dir / f"gemini_robotics_reasoning_traces_batch_{batch_num}.csv"
            df_new = pd.DataFrame(extracted_records)
            df_new.to_csv(csv_path, index=False)
            print(f"  [SUCCESS] Saved standalone CSV: {csv_path.name}")
            
        except Exception as e:
            print(f"  Failed to process Gemini-Robotics Batch {batch_num}: {e}")

if __name__ == "__main__":
    # 1. Clean up and revert extra columns from original batch CSVs
    revert_batch_csvs()
    
    # 2. Retrieve Gemini-Robotics reasoning traces and save to standalone files
    retrieve_gemini_robotics()
    
    print("\n[DONE] Script execution complete!")
