from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=50)
    phone: str = Field(max_length=15, pattern=r'[0-9*#+]+$')
    passport: str = Field(max_length=10, min_length=10, pattern=r'^\d*$')