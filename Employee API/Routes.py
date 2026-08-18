from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import CRUD
import Schemas
from Database import SessionLocal

router=APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/employees")
def create_employee(employee: Schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return CRUD.create_employee(db, employee)


@router.get("/employees/all")
def read_employees(db: Session = Depends(get_db)):
    return CRUD.get_employees(db)

@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Schemas.EmployeeCreate, db: Session = Depends(get_db)):
    employee_info = CRUD.get_employee(db, employee_id)
    if not employee_info:
        raise HTTPException(status_code=404, detail="Employee not found")
    return CRUD.update_employee(db, employee_id, employee)

@router.get("/employees/highest-salary")
def read_highest_salary_employee(db: Session = Depends(get_db)):
    employee = CRUD.get_highest_salary_employee(db)
    return employee


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee_info = CRUD.get_employee(db, employee_id)
    if not employee_info:
        raise HTTPException(status_code=404, detail="Employee not found")
    return CRUD.delete_employee(db, employee_id)


@router.get("/employees/{department}")
def read_employees_by_department(department: str, db: Session = Depends(get_db)):
    employees = CRUD.get_employees_by_department(db, department)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found in this department")
    return employees

@router.get("/employees/{employee_id}/raise")
def read_employees_with_raise(employee_id: int, db: Session = Depends(get_db), raise_percentage: float = 10.0):
    employees = CRUD.get_employees_with_raise(db, employee_id, raise_percentage)
    if not employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees