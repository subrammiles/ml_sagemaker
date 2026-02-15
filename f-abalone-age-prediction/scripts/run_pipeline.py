from build_pipeline import get_pipeline

pipeline = get_pipeline()

pipeline.upsert()
execution = pipeline.start()

print("Execution ARN:", execution.arn)
