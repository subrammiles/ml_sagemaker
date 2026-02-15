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
            data["amount"],
            data["hour"],
            data["distance_km"],
            data["txns_last_24h"]
        ]])

        return features

    raise ValueError("Unsupported content type")


def predict_fn(input_data, bundle):
    model = bundle["model"]
    scaler = bundle["scaler"]

    input_scaled = scaler.transform(input_data)

    prob = model.predict_proba(input_scaled)[:, 1]
    prediction = (prob > 0.5).astype(int)

    return prediction


def output_fn(prediction, accept):
    return json.dumps(int(prediction[0])), accept


# LOCAL TEST MODE


if __name__ == "__main__":
    import sys

    bundle = model_fn("local_model")

    input_json = sys.argv[1]
    features = input_fn(input_json, "application/json")
    prediction = predict_fn(features, bundle)

    print("Prediction:", int(prediction[0]))