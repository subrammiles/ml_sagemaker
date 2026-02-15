training_job_name = "your-training-job-name"

estimator = TensorFlow.attach(training_job_name)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium"
)

response = predictor.predict({
    "texts": ["Win big prize now"]
})

print(response)
