"""
Pydantic Models
"""
from pydantic import BaseModel
from datetime import date


class Clean(BaseModel):

    patient_id: int
    gender: int
    state: str
    municipality: str
    altitude: int
    age_days: int
    weight_kg: float
    height_cm: float
    appearance: str
    diagnosis_general: str
    cx_previous: int
    diagnosis_main: str
    date_birth: date
    date_procedure: date
    surgical_procedure: str
    rachs: int
    stay_days: int
    expired: int

    class Config:
        orm_mode = True


class Patient(BaseModel):

    patient_id: int
    gender: int
    age_days: int
    weight_kg: float
    height_cm: float
    cx_previous: int
    date_birth: date
    date_procedure: date
    rachs: int
    stay_days: int
    expired: int

    class Config:
        orm_mode = True


class Origin(BaseModel):

    token: str
    state: str
    municipality: str
    altitude: int

    class Config:
        orm_mode = True


class Appearance(BaseModel):

    token: str
    appearance: str
    keywords: str

    class Config:
        orm_mode = True


class DiagnosisGeneral(BaseModel):

    token: str
    diagnosis_general: str
    keywords: str

    class Config:
        orm_mode = True


class DiagnosisMain(BaseModel):

    token: str
    diagnosis_main: str
    keywords: str

    class Config:
        orm_mode = True


class SurgicalProcedure(BaseModel):

    token: str
    surgical_procedure: str
    keywords: str

    class Config:
        orm_mode = True


class PatientOrigin(BaseModel):

    patient_id: int
    token: str

    class Config:
        orm_mode = True


class PatientAppearance(BaseModel):

    patient_id: int
    token: str

    class Config:
        orm_mode = True


class PatientDiagnosisGeneral(BaseModel):

    patient_id: int
    token: str

    class Config:
        orm_mode = True


class PatientDiagnosisMain(BaseModel):

    patient_id: int
    token: str

    class Config:
        orm_mode = True


class PatientSurgicalProcedure(BaseModel):

    patient_id: int
    token: str

    class Config:
        orm_mode = True
