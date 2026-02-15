import boto3
import sagemaker
import config

session = sagemaker.Session()
bucket = session.default_bucket()

input_data_uri = sagemaker.s3.S3Uploader.upload(
    local_path="src/data/abalone-dataset.csv",
    desired_s3_uri=f"s3://{bucket}/abalone"
)

print("Uploaded to:", input_data_uri)
