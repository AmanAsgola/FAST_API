from fastapi import FastAPI
from database import engine
from model import Base
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)