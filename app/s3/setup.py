import boto3
from app.config import S3_BUCKET
from fastapi import UploadFile, HTTPException
from tempfile import NamedTemporaryFile
from pathlib import Path
from io import BytesIO

from app.config import MAX_CSV_FILE_SIZE_BYTES


VALID_SUFFIX = {".csv", ".CSV"}
S3 = boto3.client('s3')
S3_RESOURCE = boto3.resource('s3')


async def upload_csv_to_bucket(file: UploadFile, max_size: int = MAX_CSV_FILE_SIZE_BYTES):
    """
    Load a File to S3. Makes sure that size doesn't exceeds given max_size.
    Raise 422 if .csv is not in the name, 413 if file is too big. See app.config.
    https://github.com/tiangolo/fastapi/issues/362
    """
    # Check extension
    filepath = Path(file.filename)
    if filepath.suffix not in VALID_SUFFIX:
        raise HTTPException(422, f"File is extension is not in {VALID_SUFFIX}")
    # Check size
    real_file_size = 0
    with NamedTemporaryFile(delete=False) as temp:
        for chunk in file.file:
            real_file_size += len(chunk)
            if real_file_size > max_size:
                raise HTTPException(413, f"File exceeds max size: {MAX_CSV_FILE_SIZE_BYTES} bytes.")
            temp.write(chunk)
    # S3
    with open(temp.name, "rb") as data:
        S3.upload_fileobj(data, S3_BUCKET, file.filename)


async def get_list_of_csv_files():
    """Get list of files in bucket."""
    return [f.key for f in S3_RESOURCE.Bucket(S3_BUCKET).objects.all()]

async def get_csv_file(filename: str):
    """Get csv file by name. Raise 404 if not found."""
    s3_object = S3_RESOURCE.Bucket(S3_BUCKET).Object(filename)
    try:
        with BytesIO() as data:
            s3_object.download_fileobj(data)
            response = s3_object.get()
            return response['Body'].read()
    except:
        raise HTTPException(404, f"File {filename} not found.")