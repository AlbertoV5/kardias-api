import fastapi

from app.ml.models.kmeans import kmeans_model, get_cluster_data
from app.ml.pre_processing.kmeans import pre_process_kmeans 
from app.models.ml_schemas import PatientPredictKMeans, KMeansClusterResult, KMeansClusterData

router = fastapi.APIRouter()


@router.post("/", response_model=KMeansClusterResult, status_code=200)
async def predict_kmeans_clusters(request: PatientPredictKMeans):
    """Predict K Means cluster."""
    # Do pre-processing
    patient_data = pre_process_kmeans(request)
    # Predict
    prediction = kmeans_model.predict(patient_data)
    return {"cluster": prediction[0]}


@router.get("/",response_model=list[KMeansClusterData], status_code=200)
async def read_kmeans_clusters():
    """Get the Pre-trained Cluster Info."""
    return get_cluster_data()