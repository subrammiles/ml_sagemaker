import sagemaker
from sagemaker.pytorch import PyTorch

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

estimator = PyTorch(
    entry_point="train_cartpole.py",
    source_dir="src",
    role=role,
    framework_version="2.0",
    py_version="py310",
    instance_type="ml.m5.large",
    instance_count=1,
    base_job_name="cartpole-ray",
    requirements_file="requirements.txt"
)

estimator.fit()
