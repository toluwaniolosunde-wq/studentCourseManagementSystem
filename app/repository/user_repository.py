from mimetypes import init

from app.database import users_collection
from bson import ObjectId


async def create_user(user):
    result = await users_collection.insert_one(user)
    return str(result.inserted_id)


async def get_all_users():
    users = []
    async for user in users_collection.find():
        user["id"] = str(user["_id"])
        users.append(user)
    return users


async def get_user(user_id):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["id"] = str(user["_id"])
    return user

git init
git add .
git commit -m "Initial commit"