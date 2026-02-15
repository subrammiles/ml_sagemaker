import os
import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train(model_dir):

    X = np.load("data/X.npy")
    y = np.load("data/y.npy")

    model = Sequential([
        Dense(4, activation="relu", input_shape=(2,)),
        Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    model.fit(X, y, epochs=100, verbose=0)

    os.makedirs(model_dir, exist_ok=True)
    model.save(model_dir)

    print("Model saved to", model_dir)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model-dir",
        type=str,
        default=os.environ.get("SM_MODEL_DIR", "model")
    )

    args = parser.parse_args()

    train(args.model_dir)
