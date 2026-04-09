from fastapi import APIRouter
from app.schema.requests.enrollment import EnrollmentCreate

router = APIRouter()

@router.post("/enrollments")
def enroll_student(enrollment: EnrollmentCreate):
    return {"message": "Student enrolled"}


@router.post("/assign-grade")
def assign_grade(student_id: int, course_id: int, grade: str):
    return {"message": "Grade assigned"}

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):
    return {"student_id": student_id}

