from sqlalchemy.orm import Session
from model import Book
from schemas import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book
def get_books(db: Session):
    return db.query(Book).all()


def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()

    if not db_book:
        return None

    db_book.title = book.title
    db_book.author = book.author

    db.commit()
    db.refresh(db_book)

    return db_book
def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()

    if not db_book:
        return None

    db.delete(db_book)
    db.commit()

    return db_book