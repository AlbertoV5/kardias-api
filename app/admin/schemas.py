from pydantic import BaseModel


class UserData(BaseModel):
    """Response Model for User data for authentication."""

    id: int
    username: str

    class Config:
        orm_mode = True
