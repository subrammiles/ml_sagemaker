import numpy as np
import sagemaker.amazon.common as smac

def encode():

    X = np.load("data/pca_scaled.npy")

    with open("data/pca_train.recordio", "wb") as f:
        smac.write_numpy_to_dense_tensor(f, X)

    print("RecordIO file created")

if __name__ == "__main__":
    encode()
