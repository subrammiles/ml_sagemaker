training_job_name = "your-training-job-name"

estimator = HuggingFace.attach(training_job_name)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.g4dn.xlarge"
)

response = predictor.predict({
    "inputs": "This movie was amazing! Highly recommend."
})

print(response)
