import os
import yaml


def export_secrets(file_path):
    with open(file_path, "r") as file:
        secrets = yaml.safe_load(file)
        for key, value in secrets.items():
            os.environ[key] = str(value)
            print(f"export {key}={value}")


export_secrets("secrets.yaml")
