from app.database import users_collection
from bson import ObjectId


class UserRepository:

    def __init__(self, db):
        self.collection = db["users"]

    def create_user(self, user):
        return self.collection.insert_one(user)

    def get_users(self):
        return list(self.collection.find())

    def get_user(self, user_id):
        return self.collection.find_one({"id": user_id})

