import sagemaker
from sagemaker.pytorch import PyTorch

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

estimator = PyTorch(
    entry_point="train.py",
    source_dir="src",
    role=role,
    framework_version="2.0",
    py_version="py310",
    instance_count=1,
    instance_type="ml.g4dn.xlarge",
    output_path=f"s3://{sess.default_bucket()}/cnn/output",
    sagemaker_session=sess
)

estimator.fit()
