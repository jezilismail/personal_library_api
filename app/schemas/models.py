from pydantic import BaseModel, Field

class Book(BaseModel):
    book_name: str
    author_name: str
    price: int | None = 0
    genres: set[str] = set()

class BookCreate(BaseModel):
    book_id: str
    book: Book

class FetchParams(BaseModel):
    model_config = {"extra": "ignore"}

    start_indx: int | None = Field(ge=0, alias="start", default=0)
    end_indx: int | None = Field(lt=100, alias="end", default=5)