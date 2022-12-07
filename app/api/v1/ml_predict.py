import fastapi
from fastapi import HTTPException

from app.ml.models.kmeans import (
    kmeans_model,
    get_cluster_data,
    get_linreg_rachs_staydays,
)
from app.ml.pre_processing.kmeans import pre_process_kmeans
from app.models.ml_schemas import (
    PatientPredictKMeans,
    KMeansClusterResult,
    KMeansFullData,
)

router = fastapi.APIRouter()


@router.post("/kmeans/predict", response_model=KMeansClusterResult, status_code=200)
async def predict_kmeans_clusters(request: PatientPredictKMeans):
    """Predict K Means cluster."""
    # Do pre-processing
    try:
        patient_data = pre_process_kmeans(request)
    except KeyError as e:
        raise HTTPException(422, "Not a valid diagnosis or procedure, please see /docs")

    # Predict
    prediction = kmeans_model.predict(patient_data)
    return {"cluster": prediction[0]}


@router.get("/kmeans/clusters", response_model=KMeansFullData, status_code=200)
async def read_kmeans_clusters():
    """Get the Average values of the KMeans Clusters."""
    data = get_cluster_data()
    linreg = get_linreg_rachs_staydays(data)
    return {"clusters": data.to_dict(orient="records"), "linear_regression": linreg}
