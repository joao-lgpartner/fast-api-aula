from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.user import *
from app.services.user_service import *

from app.db.database import get_db, Session

router = APIRouter(prefix="/user", tags=["User"])

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
    
@router.get("", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    try:
        return get_all_users(db)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))

@router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_user(db, user_id)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
    
@router.put("/{user_id}", response_model=UserRead)
def update_user_info(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        updated = update_user(db, user_id, user)
        if not updated:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
    
@router.delete("/{user_id}")
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_user(db, user_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, details=str(e))
