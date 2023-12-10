from fastapi import APIRouter, status, Response, Path
from typing import Union, List
from models.user import User
from models.defaultResponse import DefaultResponse
from utils import get_user_by_id

router = APIRouter(
    prefix="/api", 
    tags=["user"]
)

all_users = [
    User(id=1, name="Кирилл", phone="+12345678", passport="0012345678"),
    User(id=2, name="Виталий", phone="+7912323456", passport="1234567891"),
    User(id=3, name="Пётр", phone="+234521346", passport="4745330876"),
    User(id=4, name="Давид", phone="+51325346", passport="4530432911"),
    User(id=5, name="Яков", phone="+92346541", passport="4451595022"),
    User(id=6, name="Антон", phone="+3123345", passport="4224736385")
]

responses = {
    status.HTTP_404_NOT_FOUND: {"model": DefaultResponse, "description": "Item not found"}
}

@router.get("/users/", response_model=Union[List[User], None], status_code=status.HTTP_200_OK)
def read_users():
    return all_users

@router.get("/users/{id}", response_model=Union[User, DefaultResponse], responses={**responses, status.HTTP_200_OK: {"model": User}})
def get_user(id: int, response: Response):
    user: User = get_user_by_id(id, all_users)
    if user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")
    
    return user   

@router.post("/users", response_model=DefaultResponse, status_code=status.HTTP_200_OK)
def create_user(user: User):    
    all_users.append(user)

    return DefaultResponse(success=True, message="User successfully created") 

@router.put("/users", response_model=Union[User, DefaultResponse], responses={**responses, status.HTTP_200_OK: {"model": User}})
def update_user(user: User, response: Response):
    exists_user: User = get_user_by_id(user.id, all_users)
    if exists_user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")
    
    exists_user.name = user.name
    exists_user.phone = user.phone
    exists_user.passport = user.passport 

    return exists_user

@router.delete("/users/{id}", response_model=DefaultResponse, responses={**responses, status.HTTP_200_OK: {"model": DefaultResponse}})
def remove_user(id: int, response: Response):
    user: User = get_user_by_id(id, all_users)
    if user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")
    
    all_users.remove(user)

    return DefaultResponse(success=True, message="User successfully removed") 