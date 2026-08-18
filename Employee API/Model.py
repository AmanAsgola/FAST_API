from sqlalchemy import Column, Integer, String, DateTime
from Database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    salary = Column(Integer)
    joining_date = Column(DateTime)



