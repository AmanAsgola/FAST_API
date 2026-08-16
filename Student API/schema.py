from pydantic import BaseModel


class StudentCreate(BaseModel):
    name:str
    age:int
    course:str
    email:str

class Student(StudentCreate):
    id: int

    model_config = {
        "from_attributes": True
    }