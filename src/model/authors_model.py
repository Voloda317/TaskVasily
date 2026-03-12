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
    birth_year: Optional[int]
    name: Optional[str]
