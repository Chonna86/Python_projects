from fastapi import FastAPI
from app.routers import contacts

app = FastAPI()

app.include_router(contacts.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)