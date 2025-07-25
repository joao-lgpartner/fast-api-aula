from sqlalchemy.orm import Session
from app.model.book import Book
from app.schemas.book import BookCreate, BookRead, BookUpdate

def create_book(db: Session, book_data: BookCreate, user_id: int):
    book = Book(**book_data.model_dump(), user_id=user_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_all_books(db: Session):
    return db.query(Book).all

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, user_data: BookUpdate):
    book = get_book(db, book_id)

    if book:
        for field, value in user_data.model_dump(exclude_unset=True).items():
            setattr(book, field, value)
        db.commit()
        db.refresh(book)
        return book
    
def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)

    if book:
        db.delete(book)
        db.commit()
    
    return book