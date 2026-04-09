from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str
    role: str


@router.post("/users")
def create_user(user: UserCreate):
    return {"message": "User created", "user": user}