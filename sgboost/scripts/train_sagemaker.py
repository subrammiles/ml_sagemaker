import os
import sagemaker
from sagemaker.estimator import Estimator

import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config

print("Running SageMaker training...")

session = sagemaker.Session()
region = session.boto_region_name

role = sagemaker.get_execution_role()
PROJECT_NAME = os.environ.get("PROJECT_NAME", config.DEFAULT_PROJECT)

if not role:
    raise ValueError("SAGEMAKER_ROLE_ARN environment variable not set")

# Upload training data to S3
s3_input_path = session.upload_data(
    path=f"./projects/{PROJECT_NAME}/data",
    key_prefix=f"{PROJECT_NAME}/training-data"
)

# Create Estimator
estimator = Estimator(
    entry_point="train.py",
    source_dir=f"projects/{PROJECT_NAME}",
    role=role,
    instance_count=config.SAGEMAKER_INSTANCE_COUNT,
    instance_type=config.SAGEMAKER_INSTANCE_TYPE,
    image_uri=sagemaker.image_uris.retrieve(
        framework=config.FRAMEWORK_NAME,
        region=region,
        version=config.FRAMEWORK_VERSION
    ),
    sagemaker_session=session
)

# Start training job
estimator.fit({"train": s3_input_path})

print("SageMaker training job completed.")
print("Model artifact stored at:", estimator.model_data)
