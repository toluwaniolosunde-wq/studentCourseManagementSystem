from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")

db = client["student_course_db"]

users_collection = db["users"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]