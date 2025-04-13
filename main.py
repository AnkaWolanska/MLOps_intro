import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs_from_yaml(file_path: str):
    """Load secrets from a YAML file and export them as environment variables."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Secrets file '{file_path}' not found.")
    with open(file_path, "r") as file:
        secrets = yaml.safe_load(file)
        for key, value in secrets.items():
            os.environ[key] = str(value)


def export_envs(environment: str):
    """Load environment variables from .env file."""
    env_file = f".env.{environment}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file '{env_file}' not found.")
    load_dotenv(env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    try:
        export_envs(args.environment)
        export_envs_from_yaml("secrets.yaml")
        settings = Settings()
        print("APP_NAME: ", settings.APP_NAME)
        print("ENVIRONMENT: ", settings.ENVIRONMENT)
        print("API_KEY: ", os.getenv("api_key"))
    except Exception as e:
        print(f"Error: {e}")
