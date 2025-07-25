from fastapi import FastAPI
from app.api.routes import router
from app.api.user_routes import router as user_router
from app.api.book_routes import router as book_router

app = FastAPI(title="My API")
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)
app.include_router(router=router)
app.include_router(router=user_router, prefix="/api")
app.include_router(router=book_router, prefix="/api")
