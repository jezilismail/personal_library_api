from pathlib import Path
from app.schemas.models import Genres, BookData
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "db" / "data.json"

def filtered_by_price(min, max, library):
    filtered_lst = []
    if min != None and max == None:
        for book in library:
            if book["price"] >= min:
                filtered_lst.append(book)
    elif max != None and min == None: 
        for book in library:
            if book["price"] <= max:
                filtered_lst.append(book)
    else:
        for book in library:
            if book["price"] >= min and book["price"] <= max:
                filtered_lst.append(book)
    
    return filtered_lst

def filter_by_genre(genres, library):
    filtered_lst = []
    for book in library:
        if len(set(genres + book["genres"])) < len(genres) + len(book["genres"]):
            filtered_lst.append(book) 
    return filtered_lst

def get_books(max_price: float | None, min_price: float | None, genres: list[Genres], page: int):
    N = 5
    indx = (page - 1) * N
    with open(DATA_FILE, 'r') as data:
        library = json.load(data)
        if len(library) > 0:
            # price filter
            if min_price != None or max_price != None:
                library = filtered_by_price(min_price, max_price, library)
                if len(library) == 0:
                    return None
            
            # genre filter
            if genres != None and len(genres) > 0:
                library = filter_by_genre(genres, library)
                if len(library) == 0:
                    return None

            # pagination
            if indx >= len(library):
                return None
            books_in_page = library[indx : indx + 5]
        else: return None

    return books_in_page