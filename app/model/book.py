from ..db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user import User

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[int] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=True)
    # user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    # user: Mapped["User"] = relationship(back_populates="book")
    