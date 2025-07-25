from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    books: Mapped[List["Book"]] = relationship(back_populates="user", cascade="all,delete")

from app.model.book import Book