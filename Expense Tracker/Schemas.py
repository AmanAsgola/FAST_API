from datetime import date
from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: date
class Expense(ExpenseCreate):
    id: int

    model_config={
        "from_attributes": True
        
    }