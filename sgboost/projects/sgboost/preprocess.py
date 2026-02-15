import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


PROJECT_NAME = os.environ.get("PROJECT_NAME", config.DEFAULT_PROJECT)

def preprocess(data_path="fraud_raw.csv"):

    data = pd.read_csv(data_path)

    X = data.drop("label", axis=1)
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    train_df = pd.concat(
        [
            y_train.reset_index(drop=True),
            pd.DataFrame(X_train_scaled, columns=X.columns)
        ],
        axis=1
    )

    test_df = pd.concat(
        [
            y_test.reset_index(drop=True),
            pd.DataFrame(X_test_scaled, columns=X.columns)
        ],
        axis=1
    )

    train_df.to_csv("train_xgb.csv", index=False, header=False)
    test_df.to_csv("test_xgb.csv", index=False, header=False)

    print("Preprocessing complete")


if __name__ == "__main__":
    preprocess()
