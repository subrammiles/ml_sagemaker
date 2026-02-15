endpoint_name = "your-endpoint-name"

import boto3

client = boto3.client("sagemaker")
client.delete_endpoint(EndpointName=endpoint_name)

print("Endpoint deleted")
