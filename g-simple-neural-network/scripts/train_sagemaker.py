import sagemaker
from sagemaker.tensorflow import TensorFlow
import config

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

estimator = TensorFlow(
    entry_point="train.py",
    source_dir="src",
    role=role,
    instance_count=1,
    instance_type="ml.t3.micro",  # cheap
    framework_version="2.11",
    py_version="py39",
    script_mode=True,
)

estimator.fit()
