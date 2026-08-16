from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import CRUD
import Schemas
from Database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/expenses")
def create_expense(expense: Schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return CRUD.create_expense(db, expense)

@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db)): 
    return CRUD.get_expenses(db)

@router.get("/expenses/{expense_id}")
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = CRUD.get_expense(db, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/expenses/{expense_id}/{amount}")
def update_expense(expense_id: int, amount: float, expense: Schemas.ExpenseCreate, db: Session = Depends(get_db)):
    updated_expense = CRUD.update_expense(db, expense_id, expense, amount)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):  
    deleted_expense = CRUD.delete_expense(db, expense_id)
    if not deleted_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
        return {
            "message": "Expense deleted successfully",
            "expense": deleted_expense
        }