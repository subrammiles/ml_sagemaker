import os
import subprocess
import sys

# Add root path BEFORE importing config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config

PROJECT_NAME = os.environ.get("PROJECT_NAME", config.DEFAULT_PROJECT)

print("Running LOCAL inference...")

# Build Docker image
subprocess.run([
    "docker", "build",
    "-t", config.DOCKER_IMAGE_NAME,
    "-f", "docker/Dockerfile",
    "--build-arg", f"PROJECT_NAME={PROJECT_NAME}",
    "."
], check=True)

# Run inference with volume mount (IMPORTANT)
subprocess.run([
    "docker", "run",
    "--rm",
    "-v", f"{os.getcwd()}/projects/{PROJECT_NAME}:/app",
    config.DOCKER_IMAGE_NAME,
    "inference.py", "1200"
], check=True)

print("Local inference completed.")
