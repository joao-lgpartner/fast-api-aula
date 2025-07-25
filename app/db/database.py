from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

#localhost se for interno
# ip se for externo
# DATABASE_URL = "postegres+asyncppg://user:password@localhost/dbname"
DATABASE_URL = "sqlite:///./biblioteca.db"
engine = create_engine(DATABASE_URL, echo=True, future=True, connect_args={"check_same_thread":False})

Sessionlocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False) #autocommit=False)

class Base(DeclarativeBase): pass

def get_db():
    db: Session = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

