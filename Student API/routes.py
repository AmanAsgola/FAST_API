from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schema
from database import SessionLocal

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students")
def create_student(student: schema.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/students/{student_id}")
def update_student(student_id: int, student: schema.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)): 
    deleted_student = crud.delete_student(db, student_id)
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
