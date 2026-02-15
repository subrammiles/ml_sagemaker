import sagemaker

sess = sagemaker.Session()
bucket = sess.default_bucket()

train_s3_path = sess.upload_data(
    path="src/data/imdb_train.jsonl",
    bucket=bucket,
    key_prefix="imdb/train"
)

print("Uploaded to:", train_s3_path)
