from app.database import courses_collection
from bson import ObjectId


class CourseRepository:

    def __init__(self, db):
        self.collection = db["courses"]

    def create_course(self, course):
        return self.collection.insert_one(course)

    def get_courses(self):
        return list(self.collection.find())

    def get_course(self, course_id):
        return self.collection.find_one({"id": course_id})