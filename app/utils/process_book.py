from app.schemas.models import Book, BookDeleteResponse
import json

# create new id 
def make_new_id(last_id: int):
    zeros ='0000'
    new_id = str(last_id + 1)
    dg = len(new_id) if len(new_id) < len(zeros) else len(zeros)
    new_id = 'bk' + zeros[:-dg] + new_id
    return new_id

# add new book to data.json and return book+id
# dependency: make_new_id()
def add_new_book(book: Book):
    with open('app/db/data.json', 'r') as data:
        books = json.load(data)
        if len(books):
            new_id = make_new_id(int(books[-1]["book_id"][2:]))
        else:
            new_id = make_new_id(0)
        new_book = {"book_id": new_id, **book.model_dump()}
        books.append(new_book)
    
    with open('app/db/data.json', 'w') as file:
        file.write(json.dumps(books))

    return new_book

# return the int value in str book_id
def convert_id(book_id: str):
    id = int(book_id[2:])
    return id

# dependancy: convert_id()
# return library data + book_indx of requested book_id
def get_books_indx(book_id: str):
    with open('app/db/data.json', 'r') as data:
        books = json.load(data)
        id_lst = list(map(lambda book: convert_id(book["book_id"]), books))
        req_id = convert_id(book_id)
        book_indx = id_lst.index(req_id) if req_id in id_lst else None

    if book_indx != None:
        return (books, book_indx) 
    else: return None
    
# find book by id and return book
# dependancy: get_books_indx()
def find_book_by_id(book_id: str):
    result = get_books_indx(book_id)
    if result:
        (books, book_indx) = result
        req_book = books[book_indx] if book_indx != None else None
        return req_book
    return result

# update book by id and return updated book
# dependancy: get_books_indx()
def update_book_by_id(book_id: str, book: Book):
    result = get_books_indx(book_id)
    if result:
        (books, book_indx) = result
        books[book_indx] = {"book_id": book_id, **book.model_dump()}
    else: return None
    updated_book = books[book_indx]
    
    with open('app/db/data.json', 'w') as file:
        file.write(json.dumps(books))

    return updated_book

# delete book from data.json by book_id
# dependancy: get_books_indx()
def delete_book_by_id(book_id: str) -> BookDeleteResponse | None:
    result = get_books_indx(book_id)
    if result:
        (books, book_indx) = result
        books.pop(book_indx)
    else: return None

    with open('app/db/data.json', 'w') as file:
        file.write(json.dumps(books))
        
    return BookDeleteResponse(message="Book deleted successfully.", book_id=book_id)