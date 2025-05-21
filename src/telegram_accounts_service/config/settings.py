from pathlib import Path
from datetime import timezone
from typing import Optional
import sys

from pydantic import Field, HttpUrl
from pydantic_settings import SettingsConfigDict, BaseSettings


# ---------------------------------------------
# Base directory for locating env files and logs
# ---------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

SECRETS_DIR = BASE_DIR / "secrets"
APP_SECRETS_DIR = SECRETS_DIR / "app"

# ---------------------------------------------
# Static settings / constants
# ---------------------------------------------

DEBUG: bool = True
TIMEZONE = timezone.utc

# ---------------------------------------------
# Environment: Core Application & Database
# ---------------------------------------------

class Env(BaseSettings):
    # PostgreSQL configuration
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_DATABASE: str

    model_config = SettingsConfigDict(
        env_file=APP_SECRETS_DIR / ".env",
    )


# ---------------------------------------------
# Environment: Microservice URLs
# ---------------------------------------------

class ServiceUrlsEnv(BaseSettings):
    # Optional service base URLs
    USERS_SERVICE_URL: Optional[HttpUrl] = Field(default=None)
    AUTH_SERVICE_URL: Optional[HttpUrl] = Field(default=None)

    model_config = SettingsConfigDict(
        env_file=APP_SECRETS_DIR / ".service-urls.env",
    )


# ---------------------------------------------
# Environment Instances
# ---------------------------------------------

env = Env()
service_urls = ServiceUrlsEnv()


# ---------------------------------------------
# Database URLs (build elsewhere if needed)
# ---------------------------------------------

ASYNC_DATABASE_URL = f"postgresql+asyncpg://{env.POSTGRESQL_USER}:{env.POSTGRESQL_PASSWORD}@{env.POSTGRESQL_HOST}:{env.POSTGRESQL_PORT}/{env.POSTGRESQL_DATABASE}"
SYNC_DATABASE_URL = f"postgresql+psycopg2://{env.POSTGRESQL_USER}:{env.POSTGRESQL_PASSWORD}@{env.POSTGRESQL_HOST}:{env.POSTGRESQL_PORT}/{env.POSTGRESQL_DATABASE}"

# ---------------------------------------------
# Microservice URLs (optional values)
# ---------------------------------------------

AUTH_SERVICE_URL = service_urls.AUTH_SERVICE_URL


# ---------------------------------------------
# Logging Configuration
# ---------------------------------------------

LOG_DEBUG_SETTINGS = [
    {
        "sink": sys.stdout,
        "format": "<green>{time: YYYY:MM:DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>",
        "colorize": True,
        "level": "DEBUG",
    },
    {
        "sink": BASE_DIR / "logs/debug.log",
        "level": "INFO",
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
        "rotation": "7 days",
        "retention": "1 month",
        "compression": "zip",
    }
]

LOG_PRODUCTION_SETTINGS = [
    {
        "sink": BASE_DIR / "logs/app.log",
        "level": "INFO",
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
        "rotation": "7 days",
        "retention": "1 month",
        "compression": "zip",
        "enqueue": True
    }
]
