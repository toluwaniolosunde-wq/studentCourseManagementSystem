from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserRequest(BaseModel):
    id: int
    name: str
    email: str
    role: str