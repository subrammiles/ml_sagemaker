#
iris_sagemaker/
│
├── src/
│   ├── train.py
│   ├── inference.py
│   ├── preprocess.py
│   ├── data_loader.py
│   └── data/
│
├── scripts/
│   ├── train_local.py
│   ├── train_sagemaker.py
│   └── deploy_sagemaker.py
│
└── config.py


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