import subprocess
import os
import config

PROJECT_NAME = os.environ.get("PROJECT_NAME", config.DEFAULT_PROJECT)

subprocess.run([
    "docker", "build",
    "-t", config.DOCKER_IMAGE_NAME,
    "-f", "docker/Dockerfile",
    "--build-arg", f"PROJECT_NAME={PROJECT_NAME}",
    "."
])

subprocess.run([
    "docker", "run",
    "--rm",
    config.DOCKER_IMAGE_NAME,
    "python", "inference.py", "1200"
])
