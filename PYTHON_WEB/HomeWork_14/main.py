"""
Головний модуль для запуску FastAPI додатку.

"""

from fastapi import FastAPI
from app.routers import contacts,users
from app import database

# Створення екземпляра FastAPI

app = FastAPI()

# Підключення роутерів до основного додатку

app.include_router(contacts.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)