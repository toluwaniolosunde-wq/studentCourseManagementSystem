from pydantic import BaseModel


class Grade(BaseModel):
    student_id: str
    course_id: str
    grade:str


