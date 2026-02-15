import argparse
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
)

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--epochs", type=int, default=3)
parser.add_argument("--train_batch_size", type=int, default=32)
parser.add_argument("--model_name", type=str)
args = parser.parse_args()

# Load dataset
train_file = "/opt/ml/input/data/train/imdb_train.jsonl"

dataset = load_dataset(
    "json",
    data_files={"train": train_file}
)

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained(args.model_name)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding=True
    )

tokenized_dataset = dataset.map(tokenize, batched=True)

# Model
model = AutoModelForSequenceClassification.from_pretrained(
    args.model_name
)

# Training arguments
training_args = TrainingArguments(
    output_dir="/opt/ml/model",
    num_train_epochs=args.epochs,
    per_device_train_batch_size=args.train_batch_size,
    logging_steps=50,
    save_strategy="epoch"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"]
)

trainer.train()
trainer.save_model("/opt/ml/model")
tokenizer.save_pretrained("/opt/ml/model")
