from sagemaker.estimator import Estimator

training_job_name = "your-training-job-name"

estimator = Estimator.attach(training_job_name)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large"
)

print("Endpoint deployed")
