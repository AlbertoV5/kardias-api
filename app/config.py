"""Environment Variables"""
import os


# DB
DB_HOST = os.environ["kardias_db_host"]
DB_PASS = os.environ["kardias_db_pass"]
DB_USER = os.environ["kardias_db_user"]
DB_SALT = os.environ["kardias_db_salt"]
# DB_PATH = "postgres@localhost:5432/kardias-2"
DB_PATH = f"{DB_USER}:{DB_PASS}@{DB_HOST}:5432/kardias"