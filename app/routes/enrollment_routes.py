from fastapi import APIRouter
from app.schema.requests.enrollment import EnrollmentCreate, AssignGradeRequest

router = APIRouter()

@router.post("/enrollments")
def enroll_student(enrollment: EnrollmentCreate):
    return {"message": "Student enrolled"}


@router.post("/assign-grade")
def assign_grade(data: AssignGradeRequest):
    return {
        "message": "Grade assigned",
        "student_id": data.student_id,
        "course_id": data.course_id,
        "grade": data.grade
    }

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):
    return {"student_id": student_id}

@router.get("/courses/{course_id}/students")
def get_course_students(course_id: int):
    return {"course_id": course_id, "students": []}

