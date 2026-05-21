from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI(
    title="Personal Library API",
    description="A simple CRUD app to store and manage books"
)

class Book(BaseModel):
    book_name: str
    author_name: str
    price: int | None = 0
    genre: str | None = 'Generic'

class BookCreate(BaseModel):
    book_id: str
    book: Book

Library: list[BookCreate] = []

def create_new_id():
    last_id = int(Library[-1].book_id[2:]) if len(Library) else 0
    new_book_id = last_id + 1
    i = 3 - len(str(new_book_id))
    new_book_id = 'bk' + ('0' * i if i > 0 else '') + str(new_book_id)

    return new_book_id

def add_new_book(book: Book):
    book_id = create_new_id()
    new_book = BookCreate(book_id=book_id, book=book)
    Library.append(new_book)

    return {"message": "Book created successfully.", "book": {"book_id": book_id, **book.model_dump()}}


@app.post("/add-books/")
async def add_books(
    books: list[Book], 
    count: Annotated[
        int | None, 
        Query(
            title="Number of books", 
            description="This query parameter represents the number of books in the request body and is required if multiple books are to be added at a time, value can only range from 2 - 9, it should be left empty if only one book is being added.", 
            gt=1, 
            lt=10
        )
    ] = None):

    if count and len(books) == count:
        result = []
        for book in books:
            result.append(add_new_book(book)["book"])        
        return {"message": "Success", "books": result}
    
    if not count and len(books) == 1:
        result = add_new_book(books[0])
        return result
    
    if len(books) > 1 and not count or len(books) != count:
        return {"message": "Number of books does not match the count in query!"}
    
    return {"message": "Error adding books!"}

# @app.get("/books")
# async def get_books():
#     return {"library": library}



# @app.post("/books")
# async def add_book(book: Book):
#     # case 1: empty values
#     if not (book.book_id and book.name):
#         return {"message": "Book `name` and `book_id` cannot be empty!"}
    
#     # case 2: duplicate id
#     if len(library) and book.book_id in [item["book_id"] for item in library]:
#         return {"message": "A book with same `book_id` already exists!"}
    
#     # case 3: book_id format validation
#     if book.book_id[:2] != 'bk' or not book.book_id[2:].isdigit():
#         return {"message": "Invalid `book_id`!"} 
    
#     library.append({**book.model_dump()})

#     return {"message": f"New book added successfully", "library": library}
