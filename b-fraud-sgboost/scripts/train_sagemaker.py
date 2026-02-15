import sagemaker
from sagemaker.estimator import Estimator
import config

sess = sagemaker.Session()

role = sagemaker.get_execution_role()

estimator = Estimator(
    entry_point="train.py",
    source_dir="src",
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    image_uri=sagemaker.image_uris.retrieve(
        framework="xgboost",
        region=sess.boto_region_name,
        version="1.5-1"
    ),
    output_path=f"s3://{config.S3_BUCKET}/fraud/output",
    sagemaker_session=sess
)

estimator.fit({
    "train": f"s3://{config.S3_BUCKET}/fraud/train/",
    "validation": f"s3://{config.S3_BUCKET}/fraud/validation/"
})
