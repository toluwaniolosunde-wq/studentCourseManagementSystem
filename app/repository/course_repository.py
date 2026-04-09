from app.database import courses_collection
from bson import ObjectId


async def create_course(course):
    result = await courses_collection.insert_one(course)
    return str(result.inserted_id)


async def get_all_courses():
    courses = []
    async for course in courses_collection.find():
        course["id"] = str(course["_id"])
        courses.append(course)
    return courses


async def get_course(course_id):
    course = await courses_collection.find_one({"_id": ObjectId(course_id)})
    if course:
        course["id"] = str(course["_id"])
    return course