import os
import subprocess
import sagemaker
from sagemaker.estimator import Estimator
import config


RUN_ENV = os.environ.get("RUN_ENV", config.DEFAULT_ENV)
PROJECT_NAME = os.environ.get("PROJECT_NAME", config.DEFAULT_PROJECT)


if RUN_ENV == "local":
    print("Running in LOCAL mode...")

    subprocess.run([
        "docker", "build",
        "-t", config.DOCKER_IMAGE_NAME,
        "-f", "docker/Dockerfile",
        "."
    ])

    subprocess.run([
        "docker", "run",
        "--rm",
        "-v", f"{os.getcwd()}/{PROJECT_NAME}:/app",
        config.DOCKER_IMAGE_NAME
    ])


else:
    print("Running in AWS SageMaker mode...")

    session = sagemaker.Session()
    region = session.boto_region_name

    role = os.environ.get("SAGEMAKER_ROLE_ARN")

    s3_input_path = session.upload_data(
        path=f"./{PROJECT_NAME}/data",
        key_prefix=f"{PROJECT_NAME}/training-data"
    )

    estimator = Estimator(
        entry_point="train.py",
        source_dir=PROJECT_NAME,
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

    estimator.fit({"train": s3_input_path})
