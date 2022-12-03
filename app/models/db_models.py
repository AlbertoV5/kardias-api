"""
SQLAlchemy Models
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    SmallInteger,
    Date,
)
from app.db.setup import Base



class CleanDB(Base):

    __tablename__ = "clean"

    patient_id = Column(Integer, nullable=False, primary_key=True)
    gender = Column(SmallInteger, nullable=False)
    state = Column(String, nullable=False)
    municipality = Column(String, nullable=False)
    altitude = Column(Integer, nullable=False)
    age_days = Column(Integer, nullable=False)
    weight_kg = Column(Float, nullable=False)
    height_cm = Column(Float, nullable=False)
    appearance = Column(String, nullable=False)
    diagnosis_general = Column(String, nullable=False)
    cx_previous = Column(Integer, nullable=False)
    diagnosis_main = Column(String, nullable=False)
    date_birth = Column(Date, nullable=False)
    date_procedure = Column(Date, nullable=False)
    surgical_procedure = Column(String, nullable=False)
    rachs = Column(Integer, nullable=False)
    stay_days = Column(Integer, nullable=False)
    expired = Column(SmallInteger, nullable=False)


class PatientDB(Base):

    __tablename__ = "patient"

    patient_id = Column(Integer, nullable=False, primary_key=True)
    gender = Column(SmallInteger, nullable=False)
    age_days = Column(Integer, nullable=False)
    weight_kg = Column(Float, nullable=False)
    height_cm = Column(Float, nullable=False)
    cx_previous = Column(Integer, nullable=False)
    date_birth = Column(Date, nullable=False)
    date_procedure = Column(Date, nullable=False)
    rachs = Column(Integer, nullable=False)
    stay_days = Column(Integer, nullable=False)
    expired = Column(SmallInteger, nullable=False)


class OriginDB(Base):

    __tablename__ = "origin"

    token = Column(String(100), nullable=False, primary_key=True)
    state = Column(String(100), nullable=False)
    municipality = Column(String(100), nullable=False)
    altitude = Column(Integer, nullable=False)


class AppearanceDB(Base):

    __tablename__ = "appearance"

    token = Column(String(100), nullable=False, primary_key=True)
    appearance = Column(String(100), nullable=False)
    keywords = Column(String(100), nullable=False)


class DiagnosisGeneralDB(Base):

    __tablename__ = "diagnosis_general"

    token = Column(String(200), nullable=False, primary_key=True)
    diagnosis_general = Column(String(400), nullable=False)
    keywords = Column(String(400), nullable=False)


class DiagnosisMainDB(Base):

    __tablename__ = "diagnosis_main"

    token = Column(String(200), nullable=False, primary_key=True)
    diagnosis_main = Column(String(400), nullable=False)
    keywords = Column(String(400), nullable=False)


class SurgicalProcedureDB(Base):

    __tablename__ = "surgical_procedure"

    token = Column(String(200), nullable=False, primary_key=True)
    surgical_procedure = Column(String(400), nullable=False)
    keywords = Column(String(400), nullable=False)


class PatientOriginDB(Base):

    __tablename__ = "patient_origin"

    patient_id = Column(
        Integer, ForeignKey("patient.patient_id"), nullable=False, primary_key=True
    )
    token = Column(
        String(200), ForeignKey("origin.token"), nullable=False, primary_key=True
    )


class PatientAppearanceDB(Base):

    __tablename__ = "patient_appearance"

    patient_id = Column(
        Integer, ForeignKey("patient.patient_id"), nullable=False, primary_key=True
    )
    token = Column(
        String(200), ForeignKey("appearance.token"), nullable=False, primary_key=True
    )


class PatientDiagnosisGeneralDB(Base):

    __tablename__ = "patient_diagnosis_general"

    patient_id = Column(
        Integer, ForeignKey("patient.patient_id"), nullable=False, primary_key=True
    )
    token = Column(
        String(200),
        ForeignKey("diagnosis_general.token"),
        nullable=False,
        primary_key=True,
    )


class PatientDiagnosisMainDB(Base):

    __tablename__ = "patient_diagnosis_main"

    patient_id = Column(
        Integer, ForeignKey("patient.patient_id"), nullable=False, primary_key=True
    )
    token = Column(
        String(200),
        ForeignKey("diagnosis_main.token"),
        nullable=False,
        primary_key=True,
    )


class PatientSurgicalProcedureDB(Base):

    __tablename__ = "patient_surgical_procedure"

    patient_id = Column(
        Integer, ForeignKey("patient.patient_id"), nullable=False, primary_key=True
    )
    token = Column(
        String(200),
        ForeignKey("surgical_procedure.token"),
        nullable=False,
        primary_key=True,
    )
