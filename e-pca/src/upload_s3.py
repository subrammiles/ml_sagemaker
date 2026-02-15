import sagemaker
import config

session = sagemaker.Session()
bucket = config.S3_BUCKET
prefix = "pca-low-cost"

s3_path = session.upload_data(
    path="src/data/pca_train.recordio",
    bucket=bucket,
    key_prefix=f"{prefix}/train"
)

print("Uploaded to:", s3_path)
