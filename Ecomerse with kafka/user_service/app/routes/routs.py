from types import Annotated
from fastapi import APIRouter ,Depends
from app.controlers.crud_user import user_add
from app.models.user_models import UserModel

router = APIRouter()

@router.get("/users")
def get_user():
    ...
@router.post("/add user")
def add_user( user: Annotated [UserModel,Depends(user_add)]):
    return user
    ...
@router.put("/update user")
def update_user():
    ...
@router.delete("/delete_user") 
def delete_user():
    ...           