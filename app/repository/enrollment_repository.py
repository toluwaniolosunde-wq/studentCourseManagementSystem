from app.database import enrollments_collection


class EnrollmentRepository:

    def __init__(self):
        self.collection = enrollments_collection

    def enroll_student(self, data: dict):
        return self.collection.insert_one(data)

    def find_by_student(self, student_id: str):
        return list(self.collection.find({"student_id": student_id}))

    def find_by_course(self, course_id: str):
        return list(self.collection.find({"course_id": course_id}))

    def find_by_student_and_course(self, student_id: str, course_id: str):
        return self.collection.find_one({
            "student_id": student_id,
            "course_id": course_id
        })

    def delete_enrollment(self, student_id: str, course_id: str):
        return self.collection.delete_one({
            "student_id": student_id,
            "course_id": course_id
        })