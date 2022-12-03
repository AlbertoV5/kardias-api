from sqlalchemy import (
    Column,
    Integer,
    String,
    Sequence,
)
from app.db.setup import Base


class ApiKeys(Base):

    __tablename__ = "_api_keys"

    id = Column(Integer, Sequence("_api_keys"), primary_key=True)
    username = Column(String(32), nullable=False)
    key = Column(String(128), nullable=False)