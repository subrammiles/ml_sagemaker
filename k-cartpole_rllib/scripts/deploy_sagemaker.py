training_job_name = "your-training-job-name"

estimator = PyTorch.attach(training_job_name)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium",
    entry_point="inference.py"
)

print("Endpoint deployed")
