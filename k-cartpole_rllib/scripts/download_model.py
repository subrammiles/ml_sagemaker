import tarfile
import boto3
import os

def download_model(s3_uri):

    bucket = s3_uri.split("/")[2]
    key = "/".join(s3_uri.split("/")[3:])

    os.makedirs("model", exist_ok=True)

    boto3.client("s3").download_file(bucket, key, "model/model.tar.gz")

    with tarfile.open("model/model.tar.gz") as tar:
        tar.extractall("model")

    print("Model downloaded and extracted")

# Usage:
# download_model(estimator.model_data)
