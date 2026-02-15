import argparse
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # SageMaker sets these automatically
    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR", "./model"))
    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN", "./data"))

    args = parser.parse_args()

    os.makedirs(args.model_dir, exist_ok=True)

    train_data = pd.read_csv(os.path.join(args.train, "train.csv"))

    X = train_data[["size"]]
    y = train_data["price"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

    print("Training completed successfully.")
