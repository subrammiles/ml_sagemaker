import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input-data", type=str, default="/opt/ml/processing/input")
    args = parser.parse_args()

    input_file = os.path.join(args.input_data, "abalone-dataset.csv")
    df = pd.read_csv(input_file)

    X = df.drop("rings", axis=1)
    y = df["rings"]

    categorical_features = ["sex"]
    numeric_features = [
        "length", "diameter", "height",
        "whole_weight", "shucked_weight",
        "viscera_weight", "shell_weight",
    ]

    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ])

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )

    X_train = preprocessor.fit_transform(X_train)
    X_val = preprocessor.transform(X_val)
    X_test = preprocessor.transform(X_test)

    train_df = pd.DataFrame(X_train.toarray() if hasattr(X_train, "toarray") else X_train)
    train_df["rings"] = y_train.values

    val_df = pd.DataFrame(X_val.toarray() if hasattr(X_val, "toarray") else X_val)
    val_df["rings"] = y_val.values

    test_df = pd.DataFrame(X_test.toarray() if hasattr(X_test, "toarray") else X_test)
    test_df["rings"] = y_test.values

    os.makedirs("/opt/ml/processing/train", exist_ok=True)
    os.makedirs("/opt/ml/processing/validation", exist_ok=True)
    os.makedirs("/opt/ml/processing/test", exist_ok=True)

    train_df.to_csv("/opt/ml/processing/train/train.csv", index=False, header=False)
    val_df.to_csv("/opt/ml/processing/validation/validation.csv", index=False, header=False)
    test_df.to_csv("/opt/ml/processing/test/test.csv", index=False, header=False)
