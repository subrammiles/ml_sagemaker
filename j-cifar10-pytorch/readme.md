cifar10_pytorch_sagemaker/
│
├── src/
│   ├── train.py
│   ├── inference.py
│   └── data/
│
├── scripts/
│   ├── train_sagemaker.py
│   ├── deploy_sagemaker.py
│   ├── predict_image.py
│   └── delete_endpoint.py
│
└── config.py

Notice:

train.py runs inside SageMaker GPU container

inference.py runs inside endpoint container

Notebook just orchestrates

# HOW TO RUN LOCALLY 

Step 1 — Generate data:

python src/data_generator.py


Step 2 — Preprocess:

python src/preprocess.py


Step 3 — Train:

python scripts/train_local.py


Step 4 — Inference:

python scripts/infer_local.py

🎯 End-to-End Flow

From your architecture diagram 

9DeepLearning+Pytourch

:

Notebook
   ↓
SageMaker GPU Training
   ↓
S3 Model Artifact
   ↓
Deploy Endpoint
   ↓
Real-Time API


Input:

32×32 RGB image

Output:

Class (0–9)

airplane

car

cat

dog

ship

etc.

💰 Cost Strategy (Very Important)
Stage	Instance	Notes
Training	ml.g4dn.xlarge	GPU but cheaper
Inference	ml.t2.medium	CPU enough
Cleanup	Delete endpoint immediately	

Never leave endpoint running.