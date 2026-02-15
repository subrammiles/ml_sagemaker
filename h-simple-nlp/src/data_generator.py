import os
import json

def generate_data():

    os.makedirs("data", exist_ok=True)

    texts = [
        "Win money now",
        "Limited offer click now",
        "Congratulations you won",
        "Meeting at 10am",
        "Lunch tomorrow",
        "Project update attached"
    ]

    labels = [1, 1, 1, 0, 0, 0]

    dataset = {"texts": texts, "labels": labels}

    with open("data/spam_data.json", "w") as f:
        json.dump(dataset, f)

    print("Dataset saved")

if __name__ == "__main__":
    generate_data()
