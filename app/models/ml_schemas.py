from pydantic import BaseModel


class PatientPredictKMeans(BaseModel):
    gender: int
    age_days: int
    weight_kg: float
    height_cm: float
    cx_previous: int
    rachs: int
    diagnosis_main: list[str]
    surgical_procedure: list[str]


class KMeansClusterResult(BaseModel):

    cluster: int


class KMeansClusterData(BaseModel):

    cluster: int
    n_patients: float
    stay_days: float
    rachs: float
    cx_previous: float
    age_days: float


class KMeansFullData(BaseModel):

    clusters: list[KMeansClusterData]
    linear_regression: list[float]
