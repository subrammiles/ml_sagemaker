from sagemaker.huggingface import HuggingFace
import sagemaker

role = sagemaker.get_execution_role()

hf_estimator = HuggingFace(
    entry_point="train.py",
    source_dir="code",
    instance_type="ml.g4dn.xlarge",   # cheaper GPU
    instance_count=1,
    role=role,
    transformers_version="4.17",
    pytorch_version="1.10",
    py_version="py38",
    hyperparameters={
        "epochs": 3,
        "train_batch_size": 32,
        "model_name": "distilbert-base-uncased"
    }
)

hf_estimator.fit({
    "train": "s3://YOUR_BUCKET/imdb/train"
})
