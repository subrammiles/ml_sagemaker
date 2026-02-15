# project
ml_sagemaker/
│
├── src/
│   ├── train.py
│   ├── inference.py
│   ├── preprocess.py
│   └── data/
│
├── scripts/
│   ├── train_local.py
│   ├── train_sagemaker.py
│   └── deploy_sagemaker.py
│
└── config.py



| Script              | Purpose                     |
| ------------------- | --------------------------- |
| train_local.py      | Train inside Docker locally |
| train_sagemaker.py  | Train on SageMaker          |
| inference.py        | Load model + predict        |
| deploy_sagemaker.py | Deploy endpoint             |


# HOW TO RUN LOCALLY 

Step 1 — Generate data:

python src/data_generator.py


Step 2 — Preprocess:

python src/preprocess.py


Step 3 — Train:

python scripts/train_local.py


Step 4 — Inference:

python scripts/infer_local.py
