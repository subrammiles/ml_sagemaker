import subprocess
import json

# Sample transaction (same format as real API request)
sample_payload = json.dumps({
    "amount": 245.60,
    "hour": 23,
    "distance_km": 1200,
    "txns_last_24h": 7
})

print("Running local inference...")

subprocess.run([
    "python",
    "src/inference.py",
    sample_payload
], check=True)

print("Inference completed.")
