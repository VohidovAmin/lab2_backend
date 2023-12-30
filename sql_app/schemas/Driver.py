from pydantic import BaseModel, Field
from datetime import date

class User(BaseModel):
    id: int = Field(gt=0)
    last_name: str = Field(max_length=30)
    first_name: str = Field(max_length=30)
    patronymic: str = Field(max_length=30)
    passport: str = Field(max_length=10, min_length=10, pattern=r'^\d*$')
    experience: date