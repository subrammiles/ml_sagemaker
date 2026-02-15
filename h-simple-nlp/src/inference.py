import json
import numpy as np
import tensorflow as tf
import joblib
import os

def model_fn(model_dir):
    model = tf.keras.models.load_model(model_dir)
    vectorizer = joblib.load(os.path.join(model_dir, "vectorizer.pkl"))
    return {"model": model, "vectorizer": vectorizer}


def input_fn(request_body, content_type):
    if content_type == "application/json":
        data = json.loads(request_body)
        return data["texts"]
    raise ValueError("Unsupported content type")


def predict_fn(input_data, bundle):
    model = bundle["model"]
    vectorizer = bundle["vectorizer"]

    X = vectorizer.transform(input_data).toarray().astype(np.float32)
    predictions = model.predict(X)

    return (predictions > 0.5).astype(int)


def output_fn(prediction, accept):
    return json.dumps(prediction.tolist()), accept


# Local test mode
if __name__ == "__main__":
    bundle = model_fn("model")

    test_texts = [
        "Win a free prize",
        "Team meeting tomorrow",
        "Hello Ravi, any update on the deployment"
    ]

    X = bundle["vectorizer"].transform(test_texts).toarray().astype(np.float32)
    preds = bundle["model"].predict(X)

    for text, pred in zip(test_texts, preds):
        print(text, "=>", "Spam" if pred > 0.5 else "Not Spam")
