import os
from pydantic import BaseSettings
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")


@lru_cache
def get_settings():
    return Settings()
