from fastapi import APIRouter

from app.services import user_services

router = APIRouter()


from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "All users"}

# @router.post("/users")
# def create_user(user):
#     user_id = user_services.create_user(user.dict())
#     return {"message": "User created", "id": user_id}
#
#
# @router.get("/users")
# def get_users():
#     return user_services.get_all_users()