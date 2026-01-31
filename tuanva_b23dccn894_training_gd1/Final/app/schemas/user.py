from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserBase(BaseModel):
    email:str
    full_name:str

class UserCreate(UserBase):
    password:str
    role:UserRole = UserRole.USER

class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None
    email: str | None = None

class UserInDBBase(UserBase):
    id: int

    class Config: 
        orm_mode = True
    
class User(UserInDBBase):
    pass