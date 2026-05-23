from fastapi import APIRouter, Query, HTTPException, status
from typing import Annotated
from app.utils.process_library import get_books
from app.schemas.models import BookData, Genres

router = APIRouter()

@router.get("/library/", response_model=list[BookData])
async def get_library(
        max_price: Annotated[float | None, Query(gt=0)] = None,
        min_price: Annotated[float | None, Query(ge=0)] = None,
        genres: Annotated[list[Genres], Query()] = [],
        page: Annotated[int, Query(title="Pagination index", ge=1)] = 1
    ):
    result = get_books(max_price, min_price, genres, page)
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    
    return result