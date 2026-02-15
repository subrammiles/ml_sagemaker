import numpy as np
import os

def generate_data():

    os.makedirs("data", exist_ok=True)

    X = np.array([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0]
    ])

    y = np.array([1, 1, 0, 0])

    np.save("data/X.npy", X)
    np.save("data/y.npy", y)

    print("Data saved")

if __name__ == "__main__":
    generate_data()
