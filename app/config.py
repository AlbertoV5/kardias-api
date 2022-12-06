"""Environment Variables"""
import os


# DB
DB_HOST = os.environ["kardias_db_host"]
DB_PASS = os.environ["kardias_db_pass"]
DB_USER = os.environ["kardias_db_user"]
DB_SALT = os.environ["kardias_db_salt"]
DB_PATH = f"{DB_USER}:{DB_PASS}@{DB_HOST}:5432/kardias"
# DB_PATH = "postgres@localhost:5432/kardias-2"

# S3
S3_BUCKET = "kardias-data"
MAX_CSV_FILE_SIZE_BYTES = 2000000  # 2 MB
