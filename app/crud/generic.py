"""
Logic for querying the clean table.
"""
from typing import Optional

from sqlalchemy.sql import delete, func
from sqlalchemy.future import select
from sqlalchemy.dialects.postgresql import insert, Insert
from sqlalchemy import Column
from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult

from app.models.definitions import (
    GenericModel,
    GenericSchema,
    is_primary_schema_list,
    is_secondary_schema_list,
    is_tertiary_schema_list,
    is_primary_model,
    is_secondary_model,
    is_terciary_model,
)


def get_database_model_primary_key(model: GenericModel) -> tuple[Column, list]:
    """Get primary key Column and name(s) as list.

    Args:
        model (GenericDatabaseModel): Any model.

    Returns:
        tuple[Column, list]: Column and list of names of PK columns.
    """
    if is_primary_model(model):
        return model.patient_id, [model.patient_id.name]
    elif is_secondary_model(model):
        return model.token, [model.token.name]
    elif is_terciary_model(model):
        return model.patient_id, [model.patient_id.name, model.token.name]
    else:
        raise ValueError(
            "Database model is not classified, please see models/definitions."
        )


def get_records_ids(records: list[GenericSchema]) -> set:
    """Get a set of ids from given Pydantic models list.

    Args:
        records (list[GenericModel]): Pydantic models list.

    Returns:
        set: Set.
    """
    if is_primary_schema_list(records):
        return set(record.patient_id for record in records)
    elif is_secondary_schema_list(records):
        return set(record.token for record in records)
    elif is_tertiary_schema_list(records):
        return set(record.patient_id for record in records)
        # return set((record.patient_id, record.token) for record in records)
    else:
        raise ValueError("Data model is not classified, please see models/definitions.")


async def get_ordered(
    db: AsyncSession, model: GenericModel, offset: int, limit: int
) -> AsyncScalarResult:
    """Get records ordered by patient_id ascending with given pagination.

    Args:
        db (AsyncSession): Database session.
        model (GenericDatabaseModel): Generic db model.
        offset (int): offset.
        limit (int): limit.

    Returns:
        AsyncScalarResult: List of models.
    """
    primary_key, _ = get_database_model_primary_key(model)
    return await db.scalars(
        select(model).order_by(primary_key).offset(offset).limit(limit)
    )


async def get_by_ids(
    db: AsyncSession, model: GenericModel, ids: set
) -> Optional[AsyncScalarResult]:
    """Get records by set of ids.

    Args:
        db (AsyncSession): Database session.
        model (GenericDatabaseModel): Generic db model.
        ids (set): set of patient_ids.

    Returns:
        AsyncScalarResult | None: Found records or none if none were found.
    """
    primary_key, _ = get_database_model_primary_key(model)
    count = await db.scalar(select(func.count(primary_key)).where(primary_key.in_(ids)))
    if count == 0:
        return None
    return await db.scalars(
        select(model).where(primary_key.in_(ids)).order_by(primary_key)
    )


async def create_all(
    db: AsyncSession, model: GenericModel, records: list[GenericSchema]
) -> None:
    """Create many records.

    Args:
        db (AsyncSession): Database session.
        model (GenericDatabaseModel): Generic db model.
        records (list[data.Clean]): List of Clean records.

    Returns:
        int: Length of Clean records list.
    """
    query: Insert = insert(model).values([clean.dict() for clean in records])
    await db.execute(query.on_conflict_do_nothing())
    await db.commit()


async def delete_all(db: AsyncSession, model: GenericModel, ids: set) -> None:
    """Delete many records by id.

    Args:
        db (AsyncSession): Database session.
        model (GenericDatabaseModel): Generic db model.
        ids (set): Set of ids.
    """
    primary_key, _ = get_database_model_primary_key(model)
    result = await db.execute(delete(model).where(primary_key.in_(ids)))
    await db.flush(result)


async def update_all(
    db: AsyncSession, model: GenericModel, records: list[GenericSchema]
) -> None:
    _, names = get_database_model_primary_key(model)
    query: Insert = insert(model).values([clean.dict() for clean in records])
    cols = {c.name: c for c in query.excluded if c.name not in names}
    await db.execute(query.on_conflict_do_update(index_elements=names, set_=cols))
    await db.commit()


async def upsert_all(
    db: AsyncSession, model: GenericModel, records: list[GenericSchema]
) -> None:
    """Insert or Update many records.

    https://stackoverflow.com/questions/55368162/bulk-upsert-with-sqlalchemy-postgres

    Args:
        db (AsyncSession): Database session.
        model (GenericDatabaseModel): Generic db model.
        records (list[BaseModel]): List of Clean records.
    """
    # Primary and Secondary Tables (can't delete).
    if is_primary_model(model) or is_secondary_model(model):
        return await update_all(db, model, records)
    # Terciary Tables (must delete or discontinued records persist).
    await delete_all(db, model, get_records_ids(records))
    await create_all(db, model, records)
