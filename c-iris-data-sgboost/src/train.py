import os
import argparse
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score

def train(data_dir, model_dir):

    train_path = os.path.join(data_dir, "train.csv")
    train_data = pd.read_csv(train_path, header=None)

    y_train = train_data.iloc[:, 0]
    X_train = train_data.iloc[:, 1:]

    model = xgb.XGBClassifier(
        objective="multi:softmax",
        num_class=3,
        eval_metric="mlogloss",
        n_estimators=50,
        max_depth=3
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_train)
    acc = accuracy_score(y_train, preds)

    print(f"Training Accuracy: {acc}")

    os.makedirs(model_dir, exist_ok=True)
    model.save_model(os.path.join(model_dir, "model.json"))

    print("Model saved")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data-dir",
        type=str,
        default=os.environ.get("SM_CHANNEL_TRAIN", "data")
    )

    parser.add_argument(
        "--model-dir",
        type=str,
        default=os.environ.get("SM_MODEL_DIR", "model")
    )

    args = parser.parse_args()
    train(args.data_dir, args.model_dir)
