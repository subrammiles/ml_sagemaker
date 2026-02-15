#
simple_nn_sagemaker/
│
├── src/
│   ├── data_generator.py
│   ├── train.py
│   ├── inference.py
│   └── data/
│
├── scripts/
│   ├── train_local.py
│   ├── train_sagemaker.py
│   ├── deploy_sagemaker.py
│   └── delete_endpoint.py
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