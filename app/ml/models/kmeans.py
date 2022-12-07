from pathlib import Path
import pandas as pd
import pickle


from app.models.ml_schemas import KMeansClusterData


PATH = Path("app/ml/models/")

with open(PATH / f"kmeans_{10}_a_{'2022-12-07'}.pkl", "rb") as f:
    kmeans_model = pickle.load(f)


with open(PATH / f"kmeans_scaler.pkl", "rb") as f:
    kmeans_scaler = pickle.load(f)


with open(PATH / f"kmeans_linear_regression.pkl", "rb") as f:
    kmeans_linreg = pickle.load(f)


def get_cluster_data() -> pd.DataFrame:
    X = pd.read_csv(PATH / "kmeans_10_data.csv").rename(columns={"Cluster": "cluster"})
    return X


def get_linreg_rachs_staydays(df):
    X = df["rachs"].values.reshape(-1, 1)
    return [round(i, 4) for i in kmeans_linreg.predict(X).reshape(1, -1)[0]]
