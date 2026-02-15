import os
import sys
import sagemaker
from sagemaker.estimator import Estimator


# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config

session = sagemaker.Session()
role = sagemaker.get_execution_role()

training_job_name = os.environ.get("TRAINING_JOB_NAME")



# Attach to completed training job
estimator = Estimator.attach(training_job_name)


# Deploy endpointv
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium"
)

predictor = estimator.deploy(
    serverless_inference_config=serverless_config
)

# Test prediction
result = predictor.predict([[1200]])
print("Prediction:", result)
