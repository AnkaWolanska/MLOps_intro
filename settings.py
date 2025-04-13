# settings.py
from pydantic_settings import BaseSettings
from pydantic import validator, ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value: str) -> str:
        allowed_values = {"dev", "test", "prod"}
        if value in allowed_values:
            return value
        raise ValidationError(
            f"Invalid environment: {value}. Must be one of {allowed_values}."
        )
