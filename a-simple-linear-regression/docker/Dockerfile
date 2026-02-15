FROM python:3.10

WORKDIR /app

ARG PROJECT_NAME

COPY projects/${PROJECT_NAME}/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY projects/${PROJECT_NAME}/ .

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python"]
CMD ["train.py"]
