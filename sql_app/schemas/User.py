from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(gt=0)
    last_name: str = Field(max_length=30)
    first_name: str = Field(max_length=30)
    patronymic: str = Field(max_length=30)
    group: str = Field(max_length=10)