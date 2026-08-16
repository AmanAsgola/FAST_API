from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.put("/books/{book_id}")
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id, book)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book


@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = crud.delete_book(db, book_id)

    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "message": "Book deleted successfully",
        "book": deleted_book
    }