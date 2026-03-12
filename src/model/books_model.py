from pydantic import BaseModel
from typing import Optional

class BookModel(BaseModel):
    author_id: int
    namebook: str
    genre: str
    pages: int
    publisher_id: int

class BookCreate(BookModel):
    pass

class BookResponse(BookModel):
    id: int

class BookUpdate(BaseModel):
    author_id: Optional[int]
    namebook: Optional[str]
    genre: Optional[str]
    pages: Optional[int]
    publisher_id: Optional[int]