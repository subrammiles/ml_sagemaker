FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install pandas scikit-learn joblib

CMD ["python", "train.py", "--train", "./data", "--model-dir", "./model"]
