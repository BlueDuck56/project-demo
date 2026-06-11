import boto3
from botocore.client import Config
import os
from dotenv import load_dotenv

load_dotenv()

B2_KEY_ID = os.getenv("B2_KEY_ID")
B2_APPLICATION_KEY = os.getenv("B2_APPLICATION_KEY")
B2_BUCKET = os.getenv("B2_BUCKET")
REGION = os.getenv("B2_REGION")

ENDPOINT_URL = f"https://s3.{REGION}.backblazeb2.com"

def upload_file(local_path: str, object_key: str, content_type: str = None):
    s3 = boto3.resource(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=B2_KEY_ID,
        aws_secret_access_key=B2_APPLICATION_KEY,
        config=Config(signature_version="s3v4"),
        region_name=REGION,
    )
    
    extra_args = {}
    if content_type:
        extra_args["ContentType"] = content_type

    s3.Bucket(B2_BUCKET).upload_file(local_path, object_key, ExtraArgs=extra_args)
    print(f"Uploaded {local_path} -> s3://{B2_BUCKET}/{object_key}")

