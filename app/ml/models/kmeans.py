from pathlib import Path
import pandas as pd
import pickle


from app.models.ml_schemas import PatientPredictKMeans, KMeansClusterData


PATH = Path("app/ml/models/") 

with open(PATH / f"kmeans_{10}_a_{'2022-12-07'}.pkl", "rb") as f:
    kmeans_model = pickle.load(f)


with open(PATH / f"kmeans_scaler.pkl", "rb") as f:
    kmeans_scaler = pickle.load(f)


def get_cluster_data() -> list[KMeansClusterData]:
    df = pd.read_csv(PATH / "kmeans_10_data.csv")
    df = df.rename(columns={"Cluster": "cluster"})
    df['cluster'] = [i for i in range(df.shape[0])]
    return df.to_dict(orient="records")