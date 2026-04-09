from pydantic import BaseModel


class Enrollment(BaseModel):
    student_id : str
    course_id : str