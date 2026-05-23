from fastapi import FastAPI
from app.api.routes import books, library

app = FastAPI(
    title="Personal Library API",
    description="A simple CRUD app to store and manage books"
)

app.include_router(books.router)
app.include_router(library.router)