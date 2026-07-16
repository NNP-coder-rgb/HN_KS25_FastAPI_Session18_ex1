from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Schemas.enrollment import EnrollmentCreate, EnrollmentResponse
from app.Schemas.student import StudentCoursesResponse
from app.Services import enrollment_service

router = APIRouter()

@router.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def create_enrollment(payload: EnrollmentCreate, db: Session = Depends(get_db)):
    return enrollment_service.enroll_student(db=db, payload=payload)

@router.get("/students/{student_id}/courses", response_model=StudentCoursesResponse)
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    return enrollment_service.get_courses_by_student(db=db, student_id=student_id)