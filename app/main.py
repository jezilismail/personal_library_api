from fastapi import FastAPI, Query, Path
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

# POST books
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


# GET books
def find_book_by_id(book_id: str):
    req_book = filter(lambda book: book.book_id == book_id, Library).__next__()
    # not implemented exception handling for book_id not found
    return req_book

@app.get("/get-books/{book_id}")
async def get_book(
    book_id: Annotated[
        str, 
        Path(
            title="Id of the requesting book", 
            pattern="^bk[0-9][0-9][0-9]"
        )
    ]):
    
    book = find_book_by_id(book_id)    
    return book

@app.get("/get-books/")
async def get_books(
        start_indx: Annotated[int | None, Query(alias="start")] = 0, 
        end_indx: Annotated[int | None, Query(alias="end")] = 5
    ):

    return Library[start_indx : end_indx]


