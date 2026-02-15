Project Architecture
pca_sagemaker/
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
│   ├── predict_sagemaker.py
│   └── delete_endpoint.py
│
└── config.py


⚠️ Notice:

No train.py

No inference.py

Because this uses the built-in PCA container (like K-Means).

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