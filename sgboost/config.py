import os

# ===============================
# Docker (Local Mode)
# ===============================

DOCKER_IMAGE_NAME = "ml-base"

# ===============================
# AWS / SageMaker
# ===============================

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

SAGEMAKER_INSTANCE_TYPE = "ml.m5.large"
SAGEMAKER_INSTANCE_COUNT = 1

FRAMEWORK_NAME = "sklearn"
FRAMEWORK_VERSION = "1.2-1"

# ===============================
# S3 Settings
# ===============================

S3_BUCKET = os.environ.get("S3_BUCKET")  # Optional
