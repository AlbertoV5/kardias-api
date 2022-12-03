"""Define constants and categories for runtime checks."""
from typing import Callable, Protocol, Any
from sqlalchemy import Column


from app.models.db_schemas import (
    Clean,
    Patient,
    Origin,
    PatientOrigin,
    Appearance,
    PatientAppearance,
    DiagnosisGeneral,
    PatientDiagnosisGeneral,
    DiagnosisMain,
    PatientDiagnosisMain,
    SurgicalProcedure,
    PatientSurgicalProcedure,
)
from app.models.db_models import (
    CleanDB,
    PatientDB,
    OriginDB,
    PatientOriginDB,
    AppearanceDB,
    PatientAppearanceDB,
    DiagnosisGeneralDB,
    PatientDiagnosisGeneralDB,
    DiagnosisMainDB,
    PatientDiagnosisMainDB,
    SurgicalProcedureDB,
    PatientSurgicalProcedureDB,
)


class GenericSchema(Protocol):
    """Any Pydantic Model"""

    def dict(self, *args, **kwargs) -> Any:
        ...


class PrimarySchema(Protocol):
    """Model with patient_id"""

    patient_id: int
    dict: Callable[..., dict]


class SecondarySchema(Protocol):
    """Model with token"""

    token: str
    dict: Callable[..., dict]


class TertiarySchema(Protocol):
    """Model with both patient_id and token"""

    patient_id: int
    token: str
    dict: Callable[..., dict]


class GenericModel(Protocol):
    """Any Model with any Primary Key and Columns"""


class PrimaryModel(Protocol):
    """Patient Model with patient_id Primary Key"""

    patient_id: Column


class SecondaryModel(Protocol):
    """Term Model with token Primary Key"""

    token: Column


class TertiaryModel(Protocol):
    """Map Model with both patient_id and token Keys"""

    patient_id: Column
    token: Column


PRIMARY_SCHEMAS = {Clean, Patient}
SECONDARY_SCHEMAS = {
    Appearance,
    Origin,
    DiagnosisGeneral,
    DiagnosisMain,
    SurgicalProcedure,
}
TERTIARY_SCHEMAS = {
    PatientAppearance,
    PatientOrigin,
    PatientDiagnosisGeneral,
    PatientDiagnosisMain,
    PatientSurgicalProcedure,
}
PRIMARY_MODELS = {CleanDB, PatientDB}
SECONDARY_MODELS = {
    AppearanceDB,
    OriginDB,
    DiagnosisGeneralDB,
    DiagnosisMainDB,
    SurgicalProcedureDB,
}
TERCIARY_MODELS = {
    PatientAppearanceDB,
    PatientOriginDB,
    PatientDiagnosisGeneralDB,
    PatientDiagnosisMainDB,
    PatientSurgicalProcedureDB,
}


def is_primary_schema_list(
    model_list: list[GenericSchema],
) -> bool:
    """Assumes that all elements in list are the same model."""
    return type(model_list[0]) in PRIMARY_SCHEMAS


def is_secondary_schema_list(
    model_list: list[GenericSchema],
) -> bool:
    """Assumes that all elements in list are the same model."""
    return type(model_list[0]) in SECONDARY_SCHEMAS


def is_tertiary_schema_list(
    model_list: list[GenericSchema],
) -> bool:
    """Assumes that all elements in list are the same model."""
    return type(model_list[0]) in TERTIARY_SCHEMAS


def is_primary_model(
    model: GenericModel,
) -> bool:
    """Whether or not the model is in the Patient Models set."""
    return model in PRIMARY_MODELS


def is_secondary_model(
    model: GenericModel,
) -> bool:
    """Whether or not the model is in the Term Models set."""
    return model in SECONDARY_MODELS


def is_terciary_model(
    model: GenericModel,
) -> bool:
    """Whether or not the model is in the Map Models set."""
    return model in TERCIARY_MODELS


class SchemaModelPair:
    """Data class for holding data and database models."""

    def __init__(self, data: GenericSchema, db: GenericModel):
        self.Data = data
        """Pydantic model"""
        self.DB = db
        """Alchemy model"""


"""List of columns for multiple term normalization for Origins"""
COLUMNS_MODELS = {
    "appearance": (
        SchemaModelPair(Appearance, AppearanceDB),
        SchemaModelPair(PatientAppearance, PatientAppearanceDB),
    ),
    "diagnosis_general": (
        SchemaModelPair(DiagnosisGeneral, DiagnosisGeneralDB),
        SchemaModelPair(PatientDiagnosisGeneral, PatientDiagnosisGeneralDB),
    ),
    "diagnosis_main": (
        SchemaModelPair(DiagnosisMain, DiagnosisMainDB),
        SchemaModelPair(PatientDiagnosisMain, PatientDiagnosisMainDB),
    ),
    "surgical_procedure": (
        SchemaModelPair(SurgicalProcedure, SurgicalProcedureDB),
        SchemaModelPair(PatientSurgicalProcedure, PatientSurgicalProcedureDB),
    ),
}
"""Lookup table for column name to Alchemy and Pydantic Models. All Non-Primary Tables."""
ORIGINS_COLUMNS = ["state", "municipality", "altitude"]
"""Columns related to the Origin Models."""
ORIGINS_MODELS = {
    column: (SchemaModelPair(Origin, OriginDB), SchemaModelPair(PatientOrigin, PatientOriginDB))
    for column in ORIGINS_COLUMNS
}
"""Lookup table for all the columns related to the Origin Models."""
