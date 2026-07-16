from pydantic import BaseModel
from typing import List

class CourseBrief(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class StudentCoursesResponse(BaseModel):
    student_id: int
    full_name: str
    courses: List[CourseBrief]

    class Config:
        from_attributes = True