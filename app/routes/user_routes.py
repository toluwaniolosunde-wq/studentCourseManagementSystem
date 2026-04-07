from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services import user_services

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: UserCreate):
    user_id = user_services.create_user(user.dict())
    return {"message": "User created", "id": user_id}


@router.get("/")
def get_users():
    return user_services.get_all_users()