import boto3
import os

def lambda_handler(event, context):
    # Retrieve the S3 bucket name and object key from the event
    bucket_name = '975050064431-bucket-dev'
    object_key = 'lambda.py'
    
    # Retrieve a parameter from Parameter Store
    ssm_client = boto3.client('ssm')
    parameter_name = os.getenv('sample')
    parameter = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    parameter_value = parameter['Parameter']['Value']
    
    # Interact with S3
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=parameter_value)
    
    return {
        'statusCode': 200,
        'body': f'Successfully stored parameter value in S3 object {object_key} in bucket {bucket_name}'
    }
