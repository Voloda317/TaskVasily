from pydantic import BaseModel
from typing import Optional

class PublisherModel(BaseModel):
    country: str
    city: str
    year_publisher: int

class PublisherCreate(PublisherModel):
    pass

class PublisherResponse(PublisherModel):
    id: int

class PublisherUpdate(BaseModel):
    country: Optional[str]
    city: Optional[str]
    year_publisher: Optional[int]


class PublisherFilter(BaseModel):
    id: Optional[int] = None
    country: Optional[str] = None
    city: Optional[str] = None
    year_publisher: Optional[int] = None
