import boto3

endpoint_name = "your-endpoint-name"

client = boto3.client("sagemaker")
client.delete_endpoint(EndpointName=endpoint_name)

print("Endpoint deleted")
