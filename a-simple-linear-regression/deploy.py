import os
import subprocess
import sagemaker
from sagemaker.estimator import Estimator
from sagemaker.local import LocalSession


RUN_ENV = os.environ.get("RUN_ENV", "local")


if RUN_ENV == "local":
    print("Running in LOCAL mode using public Docker image...")

    subprocess.run(["docker", "build", "-t", "sklearn-local", "."])

    subprocess.run(["docker", "run", "--rm", "sklearn-local"])

else:
    print("Running in AWS SageMaker mode...")

    role = sagemaker.get_execution_role()
    session = sagemaker.Session()

    estimator = Estimator(
        entry_point="train.py",
        role=role,
        instance_count=1,
        instance_type="ml.m5.large",
        image_uri=sagemaker.image_uris.retrieve(
            framework="sklearn",
            region=session.boto_region_name,
            version="1.2-1"
        ),
        sagemaker_session=session
    )

    estimator.fit({"train": "s3://your-bucket/path"})
