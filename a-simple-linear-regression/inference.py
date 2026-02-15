import os
import sys
import joblib
import numpy as np


def load_model():
    """
    Load model for both local and SageMaker environments
    """

    # If running inside SageMaker
    sm_model_dir = os.environ.get("SM_MODEL_DIR")

    if sm_model_dir:
        model_path = os.path.join(sm_model_dir, "model.joblib")
        print("Loading model from SageMaker model directory...")
    else:
        model_path = os.path.join("model", "model.joblib")
        print("Loading model from local model directory...")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")

    model = joblib.load(model_path)
    return model


def predict(size_value):
    model = load_model()

    input_data = np.array([[float(size_value)]])
    prediction = model.predict(input_data)

    return prediction[0]


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python inference.py <size>")
        sys.exit(1)

    size_input = sys.argv[1]

    result = predict(size_input)

    print(f"Predicted price for size {size_input} = {result}")
