import sagemaker
from sagemaker.estimator import Estimator

training_job_name = "your-training-job-name"

estimator = Estimator.attach(training_job_name)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium"
)

response = predictor.predict({
    "sepal length (cm)": 5.1,
    "sepal width (cm)": 3.5,
    "petal length (cm)": 1.4,
    "petal width (cm)": 0.2
})

print("Prediction:", response)
