from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"
DATABASE_USER = "postgres"
DATABASE_PASS = ""
DATABASE_NAME = ""

CONNECTION_STRING = (
    f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)
