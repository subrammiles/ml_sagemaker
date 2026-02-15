import os
import subprocess
import sys

# Add project root to path BEFORE importing config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config

PROJECT_NAME = os.environ.get("PROJECT_NAME", config.DEFAULT_PROJECT)

print("Running LOCAL training...")

# Build Docker image
subprocess.run([
    "docker", "build",
    "-t", config.DOCKER_IMAGE_NAME,
    "-f", "docker/Dockerfile",
    "--build-arg", f"PROJECT_NAME={PROJECT_NAME}",
    "."
], check=True)

# Run container
subprocess.run([
    "docker", "run",
    "--rm",
    "-v", f"{os.getcwd()}/projects/{PROJECT_NAME}:/app",
    config.DOCKER_IMAGE_NAME
], check=True)

print("Local training completed successfully.")
