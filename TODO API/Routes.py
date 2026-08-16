from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import CRUD
import schemas
from database import SessionLocal

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/todos")
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return CRUD.create_todo(db, todo)

@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return CRUD.get_todos(db)       

@router.get("/todos/{title}")
def get_todo(title: str, db: Session = Depends(get_db)):
    todo = CRUD.get_todo(db, title)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
@router.put("/todos/{todo_id}") 
def update_todo(todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    updated_todo = CRUD.update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = CRUD.delete_todo(db, todo_id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {
        "message": "Todo deleted successfully",
        "todo": deleted_todo
    }

@router.get("/todos/completed/{completed}")
def get_todos_by_completed(completed: bool, db: Session = Depends(get_db)):
    todos = CRUD.get_todos_by_completed(db, completed)
    return todos