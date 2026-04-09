from pydantic import BaseModel
from typing import Optional

class EnrollmentResponse(BaseModel):
    student_id: int
    course_id: int
    grade: Optional[str] = None