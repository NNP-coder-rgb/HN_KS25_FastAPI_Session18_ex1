from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Models.student import Student
from app.Models.course import Course
from app.Models.enrollment import Enrollment
from app.Schemas.enrollment import EnrollmentCreate
from app.Schemas.student import StudentCoursesResponse, CourseBrief

def enroll_student(db: Session, payload: EnrollmentCreate):
    student = db.query(Student).filter(Student.id == payload.student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    course = db.query(Course).filter(Course.id == payload.course_id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    if student.status != "ACTIVE":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student is inactive")

    if course.status != "OPEN":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Course is closed")

    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == payload.student_id,
        Enrollment.course_id == payload.course_id
    ).first()
    if existing_enrollment: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Student is already enrolled in this course"
        )

    current_enrollments_count = db.query(Enrollment).filter(Enrollment.course_id == payload.course_id).count()
    if current_enrollments_count >= course.max_students:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Course has reached maximum capacity"
        )

    new_enrollment = Enrollment(
        student_id=payload.student_id,
        course_id=payload.course_id
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment

def get_courses_by_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    enrollments = db.query(Enrollment).filter(Enrollment.student_id == student_id).all()
    
    courses_list = [
        CourseBrief(id=enroll.course.id, name=enroll.course.name)
        for enroll in enrollments
    ]

    return StudentCoursesResponse(
        student_id=student.id,
        full_name=student.full_name,
        courses=courses_list
    )