bert_sentiment_sagemaker/
│
├── src/
│   ├── prepare_data.py
│   └── data/
│
├── code/
│   └── train.py
│
├── scripts/
│   ├── upload_data.py
│   ├── train_sagemaker.py
│   ├── deploy_sagemaker.py
│   └── delete_endpoint.py
│
└── config.py
Notice:

No inference.py (HF container handles inference automatically)

Uses HuggingFace Estimator


Full Production Flow

From your document 

8Sentiment Analysis with Huggin…

:

Text
   ↓
Tokenizer (BERT)
   ↓
Transformer Model
   ↓
Sentiment (POSITIVE / NEGATIVE)


Input example:

{
  "inputs": "This movie was amazing!"
}


Output:

[
  {"label": "POSITIVE", "score": 0.98}
]

# HOW TO RUN LOCALLY 

Step 1 — Generate data:

python src/data_generator.py


Step 2 — Preprocess:

python src/preprocess.py


Step 3 — Train:

python scripts/train_local.py


Step 4 — Inference:

python scripts/infer_local.py


Model outputs:

Output	Meaning
0	Iris-setosa
1	Iris-versicolor
2	Iris-virginica