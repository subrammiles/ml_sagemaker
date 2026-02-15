import os
import json
import numpy as np
import argparse
import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
import joblib

def train(model_dir):

    with open("data/spam_data.json") as f:
        dataset = json.load(f)

    texts = dataset["texts"]
    labels = dataset["labels"]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts).toarray().astype(np.float32)
    y = np.array(labels, dtype=np.float32)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation="relu", input_shape=(X.shape[1],)),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    model.fit(X, y, epochs=50, verbose=0)

    os.makedirs(model_dir, exist_ok=True)
    model.save(model_dir)

    joblib.dump(vectorizer, os.path.join(model_dir, "vectorizer.pkl"))

    print("Model and vectorizer saved")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model-dir",
        type=str,
        default=os.environ.get("SM_MODEL_DIR", "model")
    )

    args = parser.parse_args()

    train(args.model_dir)
