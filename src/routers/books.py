
from fastapi import APIRouter


from src.repositories.books_repo import Book
from src.services.books import Book
import logging

loger = logging.getLogger(__name__)

router = APIRouter(prefix='/books', tags='Books')

@router.post('/')
async def create_book(
        self,
        author_id: int,
        namebook: str,
        genre: str,
        pages: int,
        publisher_id: int
        ):
    