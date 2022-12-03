import boto3
from app.config import S3_BUCKET
from fastapi import UploadFile
from tempfile import NamedTemporaryFile


S3 = boto3.client('s3')

async def upload_csv_to_bucket(file: UploadFile, max_size: int):
    """
    Load a File to S3. Makes sure that size doesn't exceeds given max_size.
    https://github.com/tiangolo/fastapi/issues/362
    """
    real_file_size = 0
    with NamedTemporaryFile(delete=False) as temp:
        for chunk in file.file:
            real_file_size += len(chunk)
            if real_file_size > max_size:
                return None
            temp.write(chunk)
    # S3
    with open(temp.name, "rb") as data:
        S3.upload_fileobj(data, S3_BUCKET, file.filename)
    return True
