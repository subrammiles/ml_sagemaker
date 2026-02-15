import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess():

    X = np.load("data/pca_raw.npy")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X).astype("float32")

    np.save("data/pca_scaled.npy", X_scaled)
    joblib.dump(scaler, "data/scaler.pkl")

    print("Preprocessing complete (scaled float32 saved)")

if __name__ == "__main__":
    preprocess()
