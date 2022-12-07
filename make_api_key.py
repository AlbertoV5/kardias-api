"""Enter a new password, hash it and store it in the database."""
from sqlalchemy import create_engine
from hashlib import blake2b
from getpass import getpass
import os


# DB
DB_HOST = os.environ["kardias_db_host"]
DB_PASS = os.environ["kardias_db_pass"]
DB_USER = os.environ["kardias_db_user"]
DB_SALT = os.environ["kardias_db_salt"]
DB_PATH = f"{DB_USER}:{DB_PASS}@{DB_HOST}:5432/kardias"
# DB_PATH = "postgres@localhost:5432/kardias-2"

engine = create_engine(f"postgresql://{DB_PATH}")
table = "_user"
username = input("Enter an username (max 32 chars)\n")
key = "key"
key2 = "key2"
while key != key2:
    key = getpass("Enter a password\n")
    key2 = getpass("Verify password\n")
    print("Passwords dont match" if key != key2 else "OK!")

key = blake2b(key.encode("utf-8"), salt=DB_SALT.encode("utf-8")).hexdigest()
tier = input("Enter tier (max 32 chars)\n")
engine.execute(
    f"INSERT INTO {table} (username, key, tier) VALUES ('{username}', '{key}', {tier});"
)
