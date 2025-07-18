from fastapi import APIRouter
from schemas.user import UserCreate
from fastapi import Body
from sqlalchemy.orm import Session
from services.user_service import *

router = APIRouter()

@router.get("/hello")
def hello_world(payload: list[dict], db: Session = Depends(get_db)):
    created = []
    for entry in payload:
        user_data = UserCreate(name=entry["name"], email=entry["email"])
        user = create_user(db, user_data)
    return "Hello World"