from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from sql_app import models, schemas, crud
from models.defaultResponse import DefaultResponse
from sql_app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api", 
    tags=["driver"]
)

responses = {
    status.HTTP_404_NOT_FOUND: {"model": DefaultResponse, "description": "Item not found"}
}

@router.get("/drivers/", response_model=Union[List[schemas.Driver], None], status_code=status.HTTP_200_OK)
def read_drivers(db: Session = Depends(get_db)):
    all_drivers = crud.get_drivers(db)
    return all_drivers