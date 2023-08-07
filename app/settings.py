from functools import lru_cache
import os
import logging

from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    LOG_LEVEL: int = logging.INFO
    LOG_FILE: str = "../logs/todolist-rest-api"
    GET_LOGGER: str = "todolist-rest-api"
    ORIGINS: list
    CORS_ALLOW_METHODS: list
    CORS_ALLOW_HEADERS: list
    DATETIME_FORMAT: str

    class Config:
        env_file = os.environ.get('ENV_FILE', '.env')
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()