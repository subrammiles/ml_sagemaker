abalone_pipeline_sagemaker/
│
├── src/
│   ├── preprocessing.py
│   ├── evaluation.py
│   └── data/
│
├── scripts/
│   ├── upload_data.py
│   ├── build_pipeline.py
│   ├── run_pipeline.py
│   ├── monitor_pipeline.py
│   └── cleanup.py
│
└── config.py


Notice:

No train.py

No inference.py

Because training uses built-in XGBoost container
and orchestration uses SageMaker Pipelines DAG

# HOW TO RUN LOCALLY 

Step 1 — Generate data:

python src/data_generator.py


Step 2 — Preprocess:

python src/preprocess.py


Step 3 — Train:

python scripts/train_local.py


Step 4 — Inference:

python scripts/infer_local.py


Final DAG (Production Flow)
AbaloneProcess
        ↓
AbaloneTrain
        ↓
AbaloneEval
        ↓
   Condition (MSE ≤ 6.0)
        ├── RegisterModel
        ├── CreateModel
        └── BatchTransform