from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

PROJECT_NAME = "karp"
VERSION = "0.1.0"
API_PREFIX = "/"

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

DB_USER = config("MARIADB_USER", cast=str)
DB_PASSWORD = config("MARIADB_PASSWORD", cast=Secret)
DB_SERVER = config("MARIADB_SERVER", cast=str, default="db")
DB_PORT = config("MARIADB_PORT", cast=str, default="3306")
DB_DATABASE = config("MARIADB_DATABASE", cast=str)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=DatabaseURL,
    default=f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DATABASE}"
)
