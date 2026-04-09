from pydantic import BaseModel

# Schema for sending user data in responses
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True
