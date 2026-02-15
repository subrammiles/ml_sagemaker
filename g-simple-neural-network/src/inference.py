import json
import numpy as np
import tensorflow as tf

def model_fn(model_dir):
    return tf.keras.models.load_model(model_dir)


def input_fn(request_body, content_type):
    if content_type == "application/json":
        data = json.loads(request_body)
        return np.array(data)
    raise ValueError("Unsupported content type")


def predict_fn(input_data, model):
    predictions = model.predict(input_data)
    return (predictions > 0.5).astype(int)


def output_fn(prediction, accept):
    return json.dumps(prediction.tolist()), accept


# Local test mode
if __name__ == "__main__":
    model = model_fn("model")

    test_data = np.array([
        [1, 1],
        [0, 0],
        [1, 0]
    ])

    predictions = model.predict(test_data)

    print("Predictions:")
    for i, p in enumerate(predictions):
        print(test_data[i], "=>", round(float(p)))
