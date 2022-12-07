from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult, AsyncResult
from sqlalchemy.dialects.postgresql import array_agg
from sqlalchemy.future import select
from sqlalchemy.sql import Select, label
from sqlalchemy import Column

from app.models.api_schemas import PatientRequest, PatientRequestByID
from app.models.db_schemas import Patient
from app.models.db_models import PatientDB, PatientAppearanceDB, AppearanceDB
from app.models.definitions import SecondaryModel, TertiaryModel


async def get_patient_records(
    request: PatientRequest, db: AsyncSession
) -> list[Patient]:
    """Get all patient records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(PatientDB)
    for key, value in data.dict().items():
        sel = sel.where(PatientDB.__table__.c[key].between(value["min"], value["max"]))
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()


async def get_patient_appearance(request: PatientRequestByID, db: AsyncSession):
    """Get all appearances from a patient."""
    data = set(request.patient_id)
    sel: Select = select(PatientAppearanceDB.patient_id, AppearanceDB.appearance)
    sel = sel.where(PatientAppearanceDB.patient_id.in_(data))
    sel = sel.join(AppearanceDB, AppearanceDB.token == PatientAppearanceDB.token)
    result: AsyncScalarResult = await db.scalars(
        sel.order_by(PatientAppearanceDB.patient_id)
    )
    return result.all()


async def get_patient_extra(
    request: PatientRequestByID,
    model_patient: TertiaryModel,
    model_term: SecondaryModel,
    columns: list[Column],
    db: AsyncSession,
):
    """Get patient extra data from secondary and tertiary tables."""
    data = set(request.patient_id)
    sel: Select = select(*columns)
    sel = sel.where(model_patient.patient_id.in_(data))
    sel = sel.join(model_term, model_term.token == model_patient.token)
    result: AsyncResult = await db.execute(sel.order_by(model_patient.patient_id))
    return result.all()


async def get_patient_extra_agg(
    request: PatientRequestByID,
    model_patient: TertiaryModel,
    model_term: SecondaryModel,
    agg: Column,
    label_: str,
    db: AsyncSession,
):
    """Get patient extra data from secondary and tertiary tables."""
    data = set(request.patient_id)
    sel: Select = select(model_patient.patient_id, label(label_, array_agg(agg)))
    sel = sel.where(model_patient.patient_id.in_(data))
    sel = sel.join(model_term, model_term.token == model_patient.token)
    sel = sel.group_by(model_patient.patient_id)
    result: AsyncResult = await db.execute(sel.order_by(model_patient.patient_id))
    return result.all()
