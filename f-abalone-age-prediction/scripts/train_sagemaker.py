from sagemaker import image_uris
from sagemaker.estimator import Estimator
import sagemaker
import config

session = sagemaker.Session()
role = sagemaker.get_execution_role()

container = image_uris.retrieve(
    framework="pca",
    region=session.boto_region_name
)

pca = Estimator(
    image_uri=container,
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    output_path=f"s3://{config.S3_BUCKET}/pca-low-cost/output",
    sagemaker_session=session
)

pca.set_hyperparameters(
    feature_dim=3,
    num_components=1,
    mini_batch_size=5
)

pca.fit({
    "train": f"s3://{config.S3_BUCKET}/pca-low-cost/train/"
})
