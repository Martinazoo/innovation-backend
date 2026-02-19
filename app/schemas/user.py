from pydantic import BaseModel
from typing import Optional

class UserRegistration(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    bachelor_degree: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[str] = None       
    password: Optional[str] = None
    bachelor_degree: Optional[str] = None

class UserUpdatePosition(BaseModel):
    posX: float
    posY: float