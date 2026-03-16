from socketserver import BaseServer

from pydantic import BaseModel
from typing import Optional

class AuthorsModel(BaseModel):
    birth_year: int
    name: str

class AuthorsCreate(AuthorsModel):
    pass

class AuthorsResponse(AuthorsModel):
    id: int

class AuthorsUpdate(BaseModel):
    birth_year: Optional[int] = None
    name: Optional[str] = None

class FilterAuthor(BaseModel):
    id: Optional[int] = None
    birth_year: Optional[int] = None
    name: Optional[str] = None
