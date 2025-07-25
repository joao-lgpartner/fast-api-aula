from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[int] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=True)
    year: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="book")
    
from app.model.user import User