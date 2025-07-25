from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.book import *
from app.services.book_service import *

from app.db.database import get_db, Session

router = APIRouter(prefix="/book", tags=["Book"])

@router.post("/{user_id}", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_new_book(user_id: int, book: BookCreate, db: Session = Depends(get_db)):
    try:
        return create_book(db, user_id=user_id)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))

@router.get("", response_model=list[BookRead])
def list_books(db: Session = Depends(get_db)):
    try:
        return get_all_books(db)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))

@router.get("/{book_id}", response_model=BookRead)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    try:
        return get_book(db, book_id)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
    
@router.put("/{book_id}", response_model=BookRead)
def update_book_info(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    try:
        updated = update_book(db, book_id, book)
        if not updated:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
    
@router.delete("/{book_id}")
def delete_user_info(book_id: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_book(db, book_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
