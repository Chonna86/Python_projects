
from fastapi import FastAPI
from app.database import engine
from app import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)