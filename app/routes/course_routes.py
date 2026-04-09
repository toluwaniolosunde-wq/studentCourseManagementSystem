from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CourseCreate(BaseModel):
    title: str
    description: str
    facilitator_id: int


@router.post("/courses")
def create_course(course: CourseCreate):
    return {"message": "Course created", "course": course}


@router.get("/courses")
def get_courses():
    return {"message": "List of courses"}