from sqlalchemy.orm import Session
from Model import Expense
from Schemas import ExpenseCreate
from datetime import date

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session):
    return db.query(Expense).all()

def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def update_expense(db: Session, expense_id: int, expense: ExpenseCreate, amount: float):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    new_amount = (
        expense.amount + amount if amount > 0 else expense.amount - abs(amount))
    db_expense.amount = new_amount
    db_expense.date = date.today()
    db.commit()
    db.refresh(db_expense)

    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense