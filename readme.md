# project

ml_sagemaker/
│
├── docker/
│   └── Dockerfile
│
├── projects/
│   └── a-simple-linear-regression/
│       ├── train.py
│       ├── inference.py
│       ├── requirements.txt
│       └── data/
│
├── scripts/
│   ├── train_local.py
│   ├── train_sagemaker.py
│   ├── infer_local.py
│   └── deploy_sagemaker.py
│
└── config.py

| Script              | Purpose                     |
| ------------------- | --------------------------- |
| train_local.py      | Train inside Docker locally |
| train_sagemaker.py  | Train on SageMaker          |
| inference.py        | Load model + predict        |
| deploy_sagemaker.py | Deploy endpoint             |




🔹 Local Training
set PROJECT_NAME=a-simple-linear-regression
python scripts/train_local.py

🔹 Local Inference
set PROJECT_NAME=a-simple-linear-regression
python scripts/infer_local.py

🔹 SageMaker Training
set PROJECT_NAME=a-simple-linear-regression
set SAGEMAKER_ROLE_ARN=arn:aws:iam::YOUR_ACCOUNT:role/YOUR_ROLE
python scripts/train_sagemaker.py

🔹 SageMaker Deploy & Inference
set PROJECT_NAME=a-simple-linear-regression
set SAGEMAKER_ROLE_ARN=arn:aws:iam::YOUR_ACCOUNT:role/YOUR_ROLE
python scripts/deploy_sagemaker.py