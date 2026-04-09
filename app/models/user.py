
from pydantic import BaseModel
from app.models.Role import Role


class User(BaseModel):
    id:str
    name: str
    email:str
    role: Role
