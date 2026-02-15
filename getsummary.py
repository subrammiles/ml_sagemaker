import boto3

sm = boto3.client("sagemaker")

jobs = sm.list_training_jobs(
    SortBy="CreationTime",
    SortOrder="Descending",
    MaxResults=5
)

for j in jobs["TrainingJobSummaries"]:
    print(j["TrainingJobName"], j["TrainingJobStatus"])