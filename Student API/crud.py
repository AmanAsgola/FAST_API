from sqlalchemy.orm import Session
from model import Student
from schema import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student= Student(
        name=student.name, 
        age=student.age, 
        email=student.email
        )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return student

def get_students(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student=db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.email = student.email
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student=db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        db.refresh(db_student)
    return db_student