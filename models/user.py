from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    phone: str
    passport: str