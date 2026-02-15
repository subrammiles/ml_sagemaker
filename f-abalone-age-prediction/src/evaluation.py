import json
import os
import tarfile
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":

    model_path = "/opt/ml/processing/model/model.tar.gz"
    test_path = "/opt/ml/processing/test"
    output_path = "/opt/ml/processing/evaluation"

    with tarfile.open(model_path) as tar:
        tar.extractall(path=".")

    booster = xgb.Booster()
    booster.load_model("xgboost-model")

    test_df = pd.read_csv(os.path.join(test_path, os.listdir(test_path)[0]), header=None)

    X_test = test_df.iloc[:, :-1]
    y_test = test_df.iloc[:, -1]

    dtest = xgb.DMatrix(X_test)
    predictions = booster.predict(dtest)

    mse = mean_squared_error(y_test, predictions)

    report = {
        "regression_metrics": {
            "mse": {"value": mse}
        }
    }

    os.makedirs(output_path, exist_ok=True)

    with open(os.path.join(output_path, "evaluation.json"), "w") as f:
        json.dump(report, f)
