from datasets import load_dataset
import json
import os

def prepare():

    os.makedirs("data", exist_ok=True)

    dataset = load_dataset("imdb")

    with open("data/imdb_train.jsonl", "w", encoding="utf-8") as f:
        for item in dataset["train"]:
            record = {
                "label": int(item["label"]),
                "text": item["text"]
            }
            f.write(json.dumps(record) + "\n")

    print("Training JSONL created")

if __name__ == "__main__":
    prepare()
