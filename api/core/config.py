from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")


PROJECT_NAME = "scout-api"
VERSION = "0.0.1"
API_PREFIX = "/api"
SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")


POSTGRES_USER = config("API_USER", cast=str)
POSTGRES_PASSWORD = config("API_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("API_SERVER", cast=str, default="db")
POSTGRES_PORT = config("API_PORT", cast=str, default="5432")
POSTGRES_DB = config("API_DB", cast=str)


DATABASE_URL = config(
    "DATABASE_URL",
    default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

