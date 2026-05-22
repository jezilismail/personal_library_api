'''
endpoints:
post:/book/ -> takes individual book data and return new book id
get:/book/{book_id} -> fetch book by id and return the book
put:/book/{book_id} -> takes book data and id and update book by id and return updated book
delete:/book/{book_id} -> delete book by id and return success message + deleted book_id
'''

from fastapi import APIRouter, Body, Path, status, HTTPException
from typing import Annotated
from app.schemas.models import Book, BookData, BookDeleteResponse
from app.utils.process_book import add_new_book, find_book_by_id, update_book_by_id, delete_book_by_id

router = APIRouter()


# POST
@router.post("/book/", response_model=BookData, status_code=status.HTTP_201_CREATED)
async def post_book(book: Annotated[Book, Body(title="Add book to library")]):
    result = add_new_book(book)
    return result


# GET
@router.get("/book/{book_id}", response_model=BookData)
async def get_book(book_id: Annotated[str, Path(title="Book ID", pattern="^bk[0-9][0-9][0-9][0-9]")]):
    result = find_book_by_id(book_id)
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")
    return result


# PUT
@router.put("/book/{book_id}")
async def put_book(
    book_id: Annotated[
        str, 
        Path(
            title="Book ID", 
            pattern="^bk[0-9][0-9][0-9][0-9]"
        )
    ], 
    book: Annotated[
        Book, 
        Body(
            title="Update book in library"
        )
    ]):

    result = update_book_by_id(book_id, book)
    if result == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Book not found!"
        )
    return result


# DELETE
@router.delete("/book/{book_id}", response_model=BookDeleteResponse)
async def delete_book(book_id: Annotated[str, Path(title="Book ID", pattern="^bk[0-9][0-9][0-9][0-9]")]):
    result = delete_book_by_id(book_id)
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")
    return result