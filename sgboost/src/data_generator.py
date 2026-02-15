import numpy as np
import pandas as pd


def generate_data(n=5000):
    np.random.seed(42)

    data = pd.DataFrame({
        "amount": np.random.exponential(scale=100, size=n),
        "hour": np.random.randint(0, 24, size=n),
        "distance_km": np.random.exponential(scale=50, size=n),
        "txns_last_24h": np.random.poisson(lam=2, size=n),
    })

    data["label"] = (
        (data["amount"] > 300) |
        (data["distance_km"] > 200) |
        (data["txns_last_24h"] > 6)
    ).astype(int)

    return data


if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/fraud_raw.csv", index=False)
    print("Data generated")
