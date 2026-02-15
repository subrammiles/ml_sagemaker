# How To Run
🔹 Local Mode
set RUN_ENV=local
set PROJECT_NAME=a-simple-linear-regression
python run.py

set PROJECT_NAME=a-simple-linear-regression
python infer_local.py


🔹 AWS Mode

Before running:

set RUN_ENV=aws
set PROJECT_NAME=a-simple-linear-regression
set SAGEMAKER_ROLE_ARN=arn:aws:iam::YOUR_ACCOUNT:role/YOUR_ROLE
python run.py