from sagemaker import image_uris
from sagemaker.estimator import Estimator
import sagemaker
import config

session = sagemaker.Session()
role = sagemaker.get_execution_role()

container = image_uris.retrieve(
    framework="kmeans",
    region=session.boto_region_name
)

kmeans = Estimator(
    image_uri=container,
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    output_path=f"s3://{config.S3_BUCKET}/unsupervised-kmeans/output",
    sagemaker_session=session
)

kmeans.set_hyperparameters(
    k=2,
    feature_dim=2,
    mini_batch_size=5
)

kmeans.fit({
    "train": f"s3://{config.S3_BUCKET}/unsupervised-kmeans/train/"
})
