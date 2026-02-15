import os
import argparse
import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score

def train(data_dir, model_dir):

    train_path = os.path.join(data_dir, "train.csv")
    print(f"Loading training data from {train_path}")

    train_data = pd.read_csv(train_path, header=None)

    y_train = train_data.iloc[:, 0]
    X_train = train_data.iloc[:, 1:]

    model = xgb.XGBClassifier(
        objective="binary:logistic",
        eval_metric="auc",
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        n_jobs=-1
    )

    # Check for validation channel (SageMaker)
    validation_dir = os.environ.get("SM_CHANNEL_VALIDATION")

    if validation_dir:
        val_path = os.path.join(validation_dir, "validation.csv")
        print(f"Loading validation data from {val_path}")

        val_data = pd.read_csv(val_path, header=None)
        y_val = val_data.iloc[:, 0]
        X_val = val_data.iloc[:, 1:]

        model.fit(
            X_train,
            y_train,
            eval_set=[(X_val, y_val)],
            verbose=True
        )
    else:
        model.fit(X_train, y_train)

    preds = model.predict_proba(X_train)[:, 1]
    auc = roc_auc_score(y_train, preds)

    print(f"Training AUC: {auc}")

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
