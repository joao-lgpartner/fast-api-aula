from pydantic import BaseModel, EmailStr
from typing import List, Optional
from book import BookRead

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    # books: List[BookRead] = []
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None