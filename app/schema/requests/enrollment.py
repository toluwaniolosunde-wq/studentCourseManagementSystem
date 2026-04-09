from pydantic import BaseModel
from typing import Optional
from app.models.grades  import Grades


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class AssignGradeRequest(BaseModel):
    student_id: int
    course_id: int
    grade: Grades