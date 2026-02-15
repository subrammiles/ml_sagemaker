import sagemaker
import config

session = sagemaker.Session()
bucket = config.S3_BUCKET
prefix = "unsupervised-kmeans"

s3_train_path = session.upload_data(
    path="src/data/customers.recordio",
    bucket=bucket,
    key_prefix=f"{prefix}/train"
)

print("Uploaded to:", s3_train_path)
