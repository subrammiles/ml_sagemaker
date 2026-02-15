from sklearn.datasets import load_iris
import pandas as pd

def load_data():
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data["target"] = iris.target
    return data

if __name__ == "__main__":
    df = load_data()
    df.to_csv("data/iris_raw.csv", index=False)
    print("Iris data saved")
