from pydantic import BaseModel, Field

class Book(BaseModel):
    book_name: str
    author_name: str
    price: float | None = 0
    genres: list[str] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "book_name": "Harry Potter and the Sorcerer's Stone",
                    "author_name": "J.K. Rowling",
                    "price": 19.99,
                    "genres": ["Fantasy", "Adventure", "Young Adult"]
                }
            ]
        }
    }

class BookData(Book):
    book_id: str = Field(pattern="^bk[0-9][0-9][0-9][0-9]")

class BookDeleteResponse(BaseModel):
    message: str = "Book deleted successfully."
    book_id: str = Field(pattern="^bk[0-9][0-9][0-9][0-9]")
