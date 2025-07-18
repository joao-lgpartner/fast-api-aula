from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Projeto X")

app.include_router(router=router, prefix='/api/v1', tags=["Hello"])