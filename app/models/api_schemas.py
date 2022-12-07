from pydantic import BaseModel
from datetime import date
from typing import Optional


class CleanRequestID(BaseModel):
    """Request Model for Clean data from ID"""

    patient_id: list[int]


class RangeNumber(BaseModel):
    """Filter Model for Floats"""

    min: float
    max: float


class RangeInteger(BaseModel):
    """Filter Model for Integers"""

    min: int
    max: int


class RangeDate(BaseModel):
    """Filter Model for Dates"""

    min: date
    max: date


class PatientFilter(BaseModel):

    gender: RangeInteger = RangeInteger(min=0, max=1)
    age_days: RangeInteger = RangeInteger(min=0, max=36500)
    weight_kg: RangeNumber = RangeNumber(min=0, max=200)
    height_cm: RangeNumber = RangeNumber(min=0, max=2000)
    cx_previous: RangeNumber = RangeNumber(min=0, max=10)
    date_birth: RangeDate = RangeDate(min=date(1900, 1, 1), max=date(2100, 1, 1))
    date_procedure: RangeDate = RangeDate(min=date(2000, 1, 1), max=date(2100, 1, 1))
    rachs: RangeInteger = RangeInteger(min=1, max=6)
    stay_days: RangeInteger = RangeInteger(min=0, max=500)
    expired: RangeInteger = RangeInteger(min=0, max=1)


class BaseRequest(BaseModel):
    """Request model for pagination / filter base."""

    amount: int = 20
    page: int = 0


class PatientRequest(BaseRequest):
    """Request Model for Patient Data."""

    columns: PatientFilter


class OriginFilter(BaseModel):
    state: list[str] = []
    municipality: list[str] = []
    altitude: RangeInteger = RangeInteger(min=0, max=5000)


class OriginRequest(BaseRequest):
    """Request Model for Origin Data"""

    columns: OriginFilter


class AppearanceFilter(BaseModel):
    appearance: list[str] = []


class AppearanceRequest(BaseRequest):
    """Request Model for Appearance Data"""

    columns: AppearanceFilter


class DiagnosisGeneralFilter(BaseModel):
    diagnosis_general: list[str] = []


class DiagnosisGeneralRequest(BaseRequest):
    """Request Model for Diagnosis General Data"""

    columns: DiagnosisGeneralFilter


class DiagnosisMainFilter(BaseModel):
    diagnosis_main: list[str] = []


class DiagnosisMainRequest(BaseRequest):
    """Request Model for Diagnosis Main Data"""

    columns: DiagnosisMainFilter


class SurgicalProceduresFilter(BaseModel):
    surgical_procedure: list[str] = []


class SurgicalProcedureRequest(BaseRequest):
    """Request Model for Surgical Procedure Data"""

    columns: SurgicalProceduresFilter


# COUNTS


class AppearanceCount(BaseModel):
    appearance: str
    count: int


class OriginCount(BaseModel):
    state: str
    municipality: str
    altitude: int
    count: int


class StateCount(BaseModel):
    state: str
    count: int


class DiagnosisMainCount(BaseModel):
    diagnosis_main: str
    count: int


class DiagnosisGeneralCount(BaseModel):
    diagnosis_general: str
    count: int


class SurgicalProcedureCount(BaseModel):
    surgical_procedure: str
    count: int


# Patient Extra Data


class PatientRequestByID(BaseModel):

    patient_id: list[int]


class PatientAppearanceResponse(BaseModel):

    patient_id: int
    appearance: str


class PatientOriginResponse(BaseModel):

    patient_id: int
    state: str
    municipality: str
    altitude: int


class PatientDiagnosisMainResponse(BaseModel):

    patient_id: int
    diagnosis_main: list[str]


class PatientDiagnosisGeneralResponse(BaseModel):

    patient_id: int
    diagnosis_general: list[str]


class PatientSurgicalProcedureResponse(BaseModel):

    patient_id: int
    surgical_procedure: list[str]
