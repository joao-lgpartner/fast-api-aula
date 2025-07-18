from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#localhost se for interno
# ip se for externo
# DATABASE_URL = "postegres+asyncppg://user:password@localhost/dbname"
DATABASE_URL = "sqlite:///./biblioteca.db"
engine = create_engine(DATABASE_URL, echo=True, future=True, connect_args={"check_same_thread":False})

sessionlocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False) #autocommit=False)

class Base(DeclarativeBase): pass


