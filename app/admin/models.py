from sqlalchemy import (
    Column,
    Integer,
    String,
    Sequence,
    SMALLINT
)
from app.db.setup import Base


class User(Base):

    __tablename__ = "_user"
    
    id = Column(Integer, Sequence("_user"), primary_key=True)
    username = Column(String(32), nullable=False)
    key = Column(String(128), nullable=False)
    tier = Column(SMALLINT, nullable=False)