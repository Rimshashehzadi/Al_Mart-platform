from typing import Optional
from sqlmodel import SQLModel,Field # type: ignore
from pydantic import EmailStr

class UserBase(SQLModel):
    user_name:str
    phone_num:int = Field (max_digits=11)
    

class UserAuth(SQLModel):
    user_email: EmailStr
    user_password: str

class UserModel(UserAuth,UserBase):
    pass

class User(UserModel, table=True):
    user_id: Optional [int] = Field (int,primary_key = True)


    