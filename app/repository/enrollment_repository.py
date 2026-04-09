from app.database import enrollments_collection


class EnrollmentRepository:

    def __init__(self, db):
        self.collection = db["enrollments"]

    def enroll_student(self, enrollment):
        return self.collection.insert_one(enrollment)

    def get_student_courses(self, student_id):
        return list(self.collection.find({"student_id": student_id}))

    def get_course_students(self, course_id):
        return list(self.collection.find({"course_id": course_id}))

    def assign_grade(self, student_id, course_id, grade):
        return self.collection.update_one(
            {"student_id": student_id, "course_id": course_id},
            {"$set": {"grade": grade}}
        )