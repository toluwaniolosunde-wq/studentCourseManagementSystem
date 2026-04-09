from pydantic import BaseModel
from typing import Optional
from app.models.grades import Grades


class EnrollmentResponse(BaseModel):
    student_id: int
    course_id: int
    grade: Optional[Grades] = None