from fastapi import UploadFile, HTTPException
from fastapi.responses import PlainTextResponse
import fastapi

from app.s3.setup import upload_csv_to_bucket, get_list_of_csv_files, get_csv_file


router = fastapi.APIRouter()


@router.put("/", status_code=202)
async def create_upload_csv_file(file: UploadFile):
    """Upload a CSV file to S3 bucket."""
    await upload_csv_to_bucket(file)
    return {"Filename": f"{file.filename}"}


@router.get("/", status_code=202)
async def read_csv_files_list():
    """Upload a CSV file to S3 bucket."""
    files = await get_list_of_csv_files()
    return {"Files": files}


@router.get("/{filename}", status_code=202, response_class=PlainTextResponse)
async def read_csv_file(filename: str):
    """Read CSV file from bucket"""
    file = await get_csv_file(filename)
    return file
