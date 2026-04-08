from pydantic import BaseModel


class Grade(BaseModel):
    id : str
    enrollment_id: str
    course_id: str
    score:float


