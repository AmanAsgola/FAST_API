from datetime import date
from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: int
    joining_date: date

class Employee(EmployeeCreate):
    id: int

    model_config={
        "from_attributes": True
    }