import subprocess
import os

def run_local_training():

    os.makedirs("local_model", exist_ok=True)

    subprocess.run([
        "python",
        "src/train.py",
        "--data-dir",
        "data",
        "--model-dir",
        "local_model"
    ], check=True)

if __name__ == "__main__":
    run_local_training()
