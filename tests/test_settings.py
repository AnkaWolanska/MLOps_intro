# filepath: /Users/ankawolanska/Documents/lab_01_MLOps_intro/MLOps_intro/tests/test_settings.py
from settings import Settings


def test_settings():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyApp (Testing)"
    assert settings.API_KEY == "fake-api-key-12345"


def test_environment_variable():
    settings = Settings()
    assert settings.ENVIRONMENT in {"dev", "test", "prod"}
