import os
import json
import requests

api_key = os.environ.get("GEMINI_API_KEY", "")
output_file = "files/batch-3salref2s9g8dyn7s9l1dlovy8xrygqcbiqg"

# Try downloading with the downloadUri from metadata + alt=media + key
url = f"https://generativelanguage.googleapis.com/v1beta/{output_file}:download?alt=media&key={api_key}"
print(f"Trying URL: {url}")
r = requests.get(url)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    print("Success! Head of content:")
    print("\n".join(r.text.strip().split("\n")[:3]))
else:
    print(r.text)
