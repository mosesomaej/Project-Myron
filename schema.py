from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

class MyBaseModel(BaseModel):
    class Config:
        orm_mode = True

class People(MyBaseModel):
    uuid: Optional[UUID] = uuid4()
    Name: str
    Survived: bool
    Pclass: int
    Sex: str
    Age: float
    Siblings_Spouses_Aboard: int
    Parents_Children_Aboard: int
    Fare: float

class DbUpdateRequest(MyBaseModel):
    Name: Optional[str]
    Survived: Optional[bool]
    Pclass: Optional[int]
    Sex: Optional[str]
    Age: Optional[int]
    Siblings_Spouses_Aboard: Optional[int]
    Parents_Children_Aboard: Optional[int]
    Fare: Optional[float]