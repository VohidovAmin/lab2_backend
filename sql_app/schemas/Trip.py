from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: int = Field(gt=0)
    driver_id: int = Field(gt=0)
    experience: datetime