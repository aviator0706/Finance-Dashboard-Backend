from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

class User(BaseModel):
    name: str = Field(..., min_length=2)
    role: Literal["admin", "analyst", "viewer"]
    active: bool = True


class Record(BaseModel):
    amount: float = Field(..., gt=0)
    type: Literal["income", "expense"]
    category: str = Field(..., min_length=1)
    date: date
    note: str = Field(..., min_length=1)