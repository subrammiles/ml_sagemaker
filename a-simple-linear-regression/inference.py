import os
import sys
import joblib
import pandas as pd


MODEL_PATH = os.environ.get("MODEL_PATH", "./model/model.joblib")


def load_model():
    return joblib.load(MODEL_PATH)


def predict(input_data):
    model = load_model()
    df = pd.DataFrame([input_data])
    return model.predict(df)[0]


if __name__ == "__main__":
    # Example usage:
    # python inference.py 1200
    size = float(sys.argv[1])
    result = predict({"size": size})
    print(f"Predicted price: {result}")
