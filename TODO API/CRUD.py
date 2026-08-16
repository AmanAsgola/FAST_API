from sqlalchemy.orm import Session
from model import Todo
from schemas import TodoCreate

def create_todo(db: Session, todo:TodoCreate):
    db_todo= Todo(
        title=todo.title, 
        description=todo.description, 
        completed=todo.completed
        )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return todo

def get_todos(db: Session):
    return db.query(Todo).all()

def get_todo(db: Session, title: str):
    return db.query(Todo).filter(Todo.title == title).first()

def update_todo(db: Session, todo_id: int, todo: TodoCreate):
    db_todo=db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo=db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        db.refresh(db_todo)
    return db_todo

def get_todos_by_completed(db: Session, completed: bool):
    return db.query(Todo).filter(Todo.completed == completed).all()