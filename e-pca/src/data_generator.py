import numpy as np

def generate_data():

    X = np.array([
        [2.5, 2.4, 1.2],
        [0.5, 0.7, 0.3],
        [2.2, 2.9, 1.0],
        [1.9, 2.2, 0.9],
        [3.1, 3.0, 1.3]
    ], dtype="float32")

    np.save("data/pca_raw.npy", X)
    print("PCA raw data saved")

if __name__ == "__main__":
    generate_data()
