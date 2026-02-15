import boto3

sm = boto3.client("sagemaker")

jobs = sm.list_training_jobs(NameContains="cartpole-ray")
print(jobs)

print("Clean manually in console if needed")
