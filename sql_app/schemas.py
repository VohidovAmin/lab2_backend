from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Union, Annotated

class Trip(BaseModel):
    id: Annotated[int, Field(gt=0)]
    driver_id: Annotated[int, Field(gt=0)]
    experience: datetime

    class Config:
        from_attributes = True

# Driver schemas
class Driver(BaseModel):
    id: Annotated[int, Field(gt=0)]
    last_name: Annotated[str, Field(max_length=30)]
    first_name: Annotated[str, Field(max_length=30)]
    patronymic: Annotated[str, Field(max_length=30)]
    passport: Annotated[str, Field(max_length=10, min_length=10, pattern=r'^\d*$')]
    experience: date
    
    trips: list[Trip] = []

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "last_name": "Balaev",
                "first_name": "Kirill",
                "patronymic": "Guramovich",
                "passport": "0123456789",
                "experience": "2024-01-06"
            }
        }

class CreateDriver(Driver):
    id: None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "last_name": "Balaev",
                "first_name": "Kirill",
                "patronymic": "Guramovich",
                "passport": "0123456789",
                "experience": "2024-01-06"
            }
        }

class UpdateDriver(Driver):
    pass

class PatchDriver(Driver):
    id: Annotated[int, Field(gt=0)]
    last_name: Annotated[Union[str, None], Field(max_length=30)] = None
    first_name: Annotated[Union[str, None], Field(max_length=30)] = None
    patronymic: Annotated[Union[str, None], Field(max_length=30)] = None
    passport: Annotated[Union[str, None], Field(max_length=10, min_length=10, pattern=r'^\d*$')] = None
    experience: Union[date, None] = None

# User schemas
class User(BaseModel):
    id: Annotated[int, Field(gt=0)] 
    last_name: Annotated[str, Field(max_length=30)]
    first_name: Annotated[str, Field(max_length=30)]
    patronymic: Annotated[str, Field(max_length=30)]
    group: Annotated[str, Field(max_length=10)]

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "id": "1",
                "last_name": "Balaev",
                "first_name": "Kirill",
                "patronymic": "Guramovich",
                "group": "4.105-1"
            }
        }

class CreateUser(User):
    id: None = None
    
    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "last_name": "Balaev",
                "first_name": "Kirill",
                "patronymic": "Guramovich",
                "group": "4.105-1"
            }
        }

class UpdateUser(User):
    pass

class PatchUser(User):
    id: Annotated[int, Field(gt=0)]
    last_name: Annotated[Union[str, None], Field(max_length=30)] = None
    first_name: Annotated[Union[str, None], Field(max_length=30)] = None
    patronymic: Annotated[Union[str, None], Field(max_length=30)] = None
    group: Annotated[Union[str, None], Field(max_length=10)] = None