import subprocess
import os

os.makedirs("model", exist_ok=True)

subprocess.run([
    "python",
    "src/train.py",
    "--model-dir",
    "model"
], check=True)
