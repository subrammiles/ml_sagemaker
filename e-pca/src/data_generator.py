import numpy as np
import pandas as pd

def generate_data():

    data = pd.DataFrame({
        "annual_spend": [500, 520, 3000, 2800, 1500],
        "visits_per_month": [2, 1, 15, 12, 7]
    })

    return data

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/customers.csv", index=False)
    print("Customer data saved")
