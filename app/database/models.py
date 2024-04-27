from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from decimal import Decimal
from datetime import datetime

class LohkoBase(SQLModel):
    nimi:str
    #mittatulos: str
    
class LohkoDB(LohkoBase, table=True):
    id: int = Field(default=None, primary_key=True)

class LohkoCreate(LohkoBase):
    pass

class AnturitBase(SQLModel):
    nimi:str
    lohko_ID: int
    lampotila: Decimal = Field(default=0, max_digits=3, decimal_places=1)
    virhetila: bool = False


class AnturiDB(AnturitBase, table=True):
    id: int = Field(default=None, primary_key=True)
    lohko_ID: int
    lampotila: Decimal = Field(default=0, max_digits=3, decimal_places=1)
    virhetila: bool = False


class AnturiCreate(AnturitBase):
    pass

class MittatulosBase(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    anturi_ID: int
    lampotila: Decimal = Field(default=0, max_digits=3, decimal_places=1)
    aikaleima: datetime

class Lohkotiedot(SQLModel):
    nimi: str
    id: int
    lohko_ID: int
    lampotila: Decimal
    virhetila: bool

class Antureidentiedot(SQLModel):
    id: int
    lohko_ID: int
    virhetila: bool
