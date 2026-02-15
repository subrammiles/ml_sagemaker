import json
import joblib
import xgboost as xgb
import numpy as np

def model_fn(model_dir):
    model = xgb.XGBClassifier()
    model.load_model(f"{model_dir}/model.json")

    scaler = joblib.load("data/scaler.pkl")

    return {"model": model, "scaler": scaler}


def input_fn(request_body, content_type):
    if content_type == "application/json":
        data = json.loads(request_body)

        features = np.array([[
            data["sepal length (cm)"],
            data["sepal width (cm)"],
            data["petal length (cm)"],
            data["petal width (cm)"]
        ]])

        return features

    raise ValueError("Unsupported content type")


def predict_fn(input_data, bundle):
    model = bundle["model"]
    scaler = bundle["scaler"]

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    return prediction


def output_fn(prediction, accept):
    return json.dumps(int(prediction[0])), accept


if __name__ == "__main__":
    import sys

    bundle = model_fn("local_model")

    input_json = sys.argv[1]
    features = input_fn(input_json, "application/json")
    prediction = predict_fn(features, bundle)

    print("Prediction:", int(prediction[0]))
