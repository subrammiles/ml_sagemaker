import boto3

sm = boto3.client("sagemaker")

sm.delete_pipeline(PipelineName="AbalonePipeline")
print("Pipeline deleted")
