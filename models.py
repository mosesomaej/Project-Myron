from sqlalchemy import Column, Integer, String, Float, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from typing import Union, Optional, Text
from uuid import UUID, uuid4

Base = declarative_base()

class People(Base):
    __tablename__ = "titatic"
    uuid = Column(String)
    Name = Column(String, primary_key=True)
    Survived = Column(String)
    Pclass= Column(Integer)
    Sex= Column(String)
    Age= Column(Numeric)
    Siblings_Spouses_Aboard= Column(Integer)
    Parents_Children_Aboard= Column(Integer)
    Fare= Column(Numeric)

