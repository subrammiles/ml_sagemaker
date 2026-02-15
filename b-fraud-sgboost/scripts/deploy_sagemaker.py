import sagemaker
from sagemaker.estimator import Estimator

training_job_name = "your-training-job-name"

estimator = Estimator.attach(training_job_name)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium"
)

response = predictor.predict({
    "amount": 245.60,
    "hour": 23,
    "distance_km": 1200,
    "txns_last_24h": 7
})

print(response)
