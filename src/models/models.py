from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    book: str
    author: str
    year: int 
    publication: str

class BookCreate(Book):
    pass

class BookOut(Book):
    id: int

class BookUpdate(BaseModel):
    book: Optional[str] = None 
    author: Optional[str] = None 
    year: Optional[int] = None 
    publication: Optional[str] = None 
