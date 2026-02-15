#
customer_kmeans_sagemaker/
│
├── src/
│   ├── data_generator.py
│   ├── preprocess.py
│   ├── encode_recordio.py
│   └── data/
│
├── scripts/
│   ├── upload_s3.py
│   ├── train_sagemaker.py
│   ├── deploy_sagemaker.py
│   └── delete_endpoint.py
│
└── config.py

⚠️ Notice:

No train.py

No inference.py

Why?

Because this uses built-in SageMaker K-Means container, not custom training code.

src/encode_recordio.py K-Means requires RecordIO-Protobuf.

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