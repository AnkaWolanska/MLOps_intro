# filepath: /Users/ankawolanska/Documents/lab_01_MLOps_intro/MLOps_intro/api/models/iris.py
from pydantic import BaseModel


class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictResponse(BaseModel):
    prediction: str
