import os
import sagemaker
from sagemaker.estimator import Estimator
import config

session = sagemaker.Session()
role = os.environ.get("SAGEMAKER_ROLE_ARN")

estimator = Estimator.attach("your-training-job-name")

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large"
)

result = predictor.predict([[1200]])
print(result)
