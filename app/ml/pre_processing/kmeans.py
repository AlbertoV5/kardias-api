from app.models.ml_schemas import PatientPredictKMeans
import pandas as pd

from app.ml.models.kmeans import kmeans_scaler


ENCODED_COLUMNS = [
    'CIA', 'CIV', 'Estenosis', 'PCA',
    'Other_Diagnosis', 'Coartacion Aortica', 'Tetralogia de Fallot',
    'Atresia', 'Post-Surgical Procedure', 'Hipoplasia',
    'Parche comunicacion interauricular CIA', 'Vena cava inferior parche',
    'Other_Procedure', 'Cierre de Conducto Arterioso',
    'Reparacion de Canal AV', 'Reparacion de Tetralogia de Fallot',
    'Procedimiento de Glenn', 'Reparacion de arco aortico',
    'Fistula sistemico pulmonar', 'Procedimiento de Fontan'
]
EXCLUDE = {"diagnosis_main", "surgical_procedure"}


def pre_process_kmeans(patient: PatientPredictKMeans):
    """Use categorical variables as 1, 0 or more."""
    # Combine Numerical and Categorical
    df = pd.DataFrame(columns=[k for k in ENCODED_COLUMNS])
    df = pd.concat([pd.DataFrame([patient.dict(exclude=EXCLUDE)]), df])
    df = df.fillna(0)
    # Increase Categorical
    for diagnosis, procedure in zip(patient.diagnosis_main, patient.surgical_procedure):
        df[diagnosis] = df[diagnosis] + 1
        df[procedure] = df[procedure] + 1
    # Use Scaler (trained)
    X_scaled = kmeans_scaler.transform(df)
    return X_scaled[0].reshape(1, -1)
