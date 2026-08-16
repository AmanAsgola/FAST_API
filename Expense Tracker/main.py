from fastapi import FastAPI
from Database import engine
from Model import Base
from Routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)