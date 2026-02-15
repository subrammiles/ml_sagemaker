# ML SageMaker Practice Repository

This repository is structured to practice Machine Learning workflows 
using both:

- 🖥 Local Docker execution
- ☁️ AWS SageMaker training (optional)

The goal is to simulate a real-world ML platform structure where multiple 
projects share a common execution framework.

---

# 📁 Project Structure

ml_sagemaker/
│
├── docker/
│   └── Dockerfile
│
├── a-simple-linear-regression/
│   ├── train.py
│   └── requirements.txt
│
├── b-sgboost/
│   ├── train.py
│   └── requirements.txt
│
└── run.py

---

# 🧩 Components Explained

## 1️⃣ docker/

Contains the **common Docker environment**.

### Dockerfile
- Uses a base Python image.
- Mounts a selected project folder at runtime.
- Installs project-specific dependencies (if `requirements.txt` exists).
- Executes `train.py`.

This design allows all projects to reuse the same container image.

---

## 2️⃣ Project Folders

Each ML example lives inside its own folder.

Example:
- `a-simple-linear-regression`
- `b-sgboost`

Each project contains:

### train.py
The model training script.
- Loads data
- Trains model
- Saves model artifact

### requirements.txt
Project-specific dependencies.

This allows:
- Different frameworks per project
- Clean separation of concerns
- No global dependency conflicts

---

## 3️⃣ run.py

This is the entry point of the system.

It supports:

### LOCAL mode
- Builds Docker image (if needed)
- Mounts selected project folder
- Runs training inside container

### AWS mode (optional)
- Uploads data to S3
- Launches SageMaker training job
- Optionally deploys endpoint

---

# 🚀 How It Works (Local Mode)

1. You run:

   python run.py

2. The system:
   - Builds Docker image
   - Mounts selected project as `/app`
   - Installs project dependencies (if any)
   - Executes `train.py`

3. Training completes inside container.

---

# ☁️ How It Works (AWS Mode)

1. Set environment:

   set RUN_ENV=aws
   set SAGEMAKER_ROLE_ARN=<your-role>

2. Run:

   python run.py

3. The system:
   - Uploads local data to S3
   - Uses SageMaker Scikit-Learn container
   - Starts cloud training job

---

# 🎯 Design Philosophy

This repository follows a simplified MLOps architecture:

- One shared execution engine (Docker)
- Multiple independent ML projects
- Environment-driven execution (local or cloud)
- Clear separation between:
  - Infrastructure (docker/)
  - ML logic (project folders)
  - Orchestration (run.py)

---

# 🔄 Adding a New Project

1. Create new folder:

   c-new-model/

2. Add:
   - train.py
   - requirements.txt

3. Run:

   set PROJECT_NAME=c-new-model
   python run.py

No Docker changes required.

---

# 🏗 Future Improvements

Possible extensions:

- CLI arguments instead of environment variables
- Experiment tracking (MLflow)
- Model versioning
- Automated Docker caching
- CI/CD integration

---

# 📌 Summary

This repository simulates a small ML platform that:

- Supports multiple ML projects
- Uses a shared container runtime
- Can scale from local development to cloud training

It is designed for learning MLOps patterns and system structure.


# How To Run
🔹 Local Mode
set RUN_ENV=local
set PROJECT_NAME=a-simple-linear-regression
python run.py

🔹 AWS Mode

Before running:

set RUN_ENV=aws
set PROJECT_NAME=a-simple-linear-regression
set SAGEMAKER_ROLE_ARN=arn:aws:iam::YOUR_ACCOUNT:role/YOUR_ROLE
python run.py