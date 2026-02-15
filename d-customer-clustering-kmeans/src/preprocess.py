import pandas as pd
import numpy as np

def preprocess(data_path="data/customers.csv"):

    data = pd.read_csv(data_path)

    data_np = data.values.astype(np.float32)

    np.save("data/customers.npy", data_np)

    print("Preprocessing complete (float32 numpy saved)")

if __name__ == "__main__":
    preprocess()
