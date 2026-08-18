from sqlalchemy.orm import Session
from Model import Employee
from Schemas import EmployeeCreate
from datetime import date

def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(
        name=employee.name,
        department=employee.department,
        salary=employee.salary,
        joining_date=employee.joining_date
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: EmployeeCreate):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    db_employee.name = employee.name
    db_employee.department = employee.department
    db_employee.salary = employee.salary
    db_employee.joining_date = employee.joining_date
    db.commit()
    db.refresh(db_employee)

    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

def get_employees_by_department(db: Session, department: str):
    return db.query(Employee).filter(Employee.department == department).all()

def get_highest_salary_employee(db: Session):
    return db.query(Employee).order_by(Employee.salary.desc()).first()

def get_employees_with_raise(db: Session, employee_id: int, raise_percentage: float):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        employee.salary += int(employee.salary * (raise_percentage / 100))
        db.commit()
        db.refresh(employee)
    return employee


