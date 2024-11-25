from pydantic import BaseModel
from typing import List
from enum import Enum

class Role(str,Enum):
    admin = "admin"
    user = "user"


class LoginDetails(BaseModel):
    email:str
    password:str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: Role

class ItemsModel(BaseModel):
    name: str
    category: str
    quantity: int

class GraphData(BaseModel):
    labels: List[str]
    values: List[int]

class UserUpdate(BaseModel):
    id: int
    element: str
    newValue: str
