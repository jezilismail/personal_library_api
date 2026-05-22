from fastapi import FastAPI
from app.api.routes import books

app = FastAPI(
    title="Personal Library API",
    description="A simple CRUD app to store and manage books"
)

app.include_router(books.router)