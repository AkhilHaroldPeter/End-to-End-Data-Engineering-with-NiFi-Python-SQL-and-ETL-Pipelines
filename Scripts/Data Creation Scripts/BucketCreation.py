import boto3
from botocore.exceptions import ClientError
import os

# Set up a conditional check for MotoServer or Production AWS S3
USE_MOTO_SERVER = "true"

if USE_MOTO_SERVER:
    # Use MotoServer endpoint
    s3 = boto3.client('s3',
                      endpoint_url="http://127.0.0.1:10001",  # MotoServer URL
                      aws_access_key_id="fakeAccessKey",
                      aws_secret_access_key="fakeSecretKey",
                      region_name="us-west-2")
else:
    # Use Production AWS S3
    s3 = boto3.client('s3',
                      aws_access_key_id="<your_access_key>",
                      aws_secret_access_key="<your_secret_key>",
                      region_name="us-west-2")

# Function to create a bucket with region specification
def create_bucket(bucket_name):
    try:
        # Check if the bucket already exists (AWS S3 or MotoServer behavior)
        response = s3.list_buckets()
        existing_buckets = [bucket['Name'] for bucket in response['Buckets']]
        if bucket_name in existing_buckets:
            print(f"Bucket '{bucket_name}' already exists.")
        else:
            # Specify region explicitly during bucket creation
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
            )
            print(f"Bucket '{bucket_name}' created.")
    except ClientError as e:
        print(f"Error: {e}")

# Test bucket creation
bucket_name = "my-test-bucket" #"my-test-bucket-generic"
create_bucket(bucket_name)

# Test by listing buckets
response = s3.list_buckets()
print("Buckets:", response['Buckets'])
