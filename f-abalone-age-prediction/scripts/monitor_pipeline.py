import boto3

sm = boto3.client("sagemaker")

executions = sm.list_pipeline_executions(
    PipelineName="AbalonePipeline"
)

print(executions)
