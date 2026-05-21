from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Personal Library API",
    description="A simple CRUD app to store and manage books"
)

class Book(BaseModel):
    book_id: str
    name: str


library = []

@app.get("/books")
async def get_books():
    return {"library": library}


@app.post("/books")
async def add_book(book: Book):
    # case 1: empty values
    if not (book.book_id and book.name):
        return {"message": "Book `name` and `book_id` cannot be empty!"}
    
    # case 2: duplicate id
    if len(library) and book.book_id in [item["book_id"] for item in library]:
        return {"message": "A book with same `book_id` already exists!"}
    
    # case 3: book_id format validation
    if book.book_id[:2] != 'bk' or not book.book_id[2:].isdigit():
        return {"message": "Invalid `book_id`!"} 
    
    library.append({**book.model_dump()})

    return {"message": f"New book added successfully", "library": library}
