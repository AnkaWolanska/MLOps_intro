from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value: str) -> str:
        allowed_values = {"dev", "test", "prod"}
        if value in allowed_values:
            return value
        raise ValueError(
            f"Invalid environment: {value}. Must be one of {allowed_values}."
        )
