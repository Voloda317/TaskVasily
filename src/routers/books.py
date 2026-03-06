from fastapi import APIRouter, Query 
from typing import List, Optional
import logging

from src.repositories.books import BookRepository
from src.services.books import BookService

router = APIRouter(prefix='/books', tags=['Books'])

logger = logging.getLogger(__name__)

repo = BookRepository()
service = BookService(repo)

@router.get('/', response_model=List[BookOut])
async def get_books():
    return service.get_book()

@router.post('/', response_model='BookOut')
async def create_book(book: BookCreate):
    new_book = service.create_book(book.model_dump())
    if new_book is None:
        logger.error("Не удалось создать книгу (сервис вернул None)")
    return new_book

@router.get('/search', response_model=List[BookOut])
async def search_book(
    book: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    publisher: Optional[str] = Query(None)
):
    filters = {}
    if book: filters['book'] = book
    if author: filters['author'] = author
    if year: filters['year'] = year
    if publisher: filters['publisher'] = publisher
    
    return service.search_for_book(filters)

@router.get('/{book_id}', response_model=BookOut)
async def get_book(book_id: int):
    book = service.get_book(book_id)
    return book

@router.patch('/{book_id}', response_model=BookOut)
async def update_book(book_id: int, book_update: BookUpdate):
    update_data = book_update.model_dump(exclude_unset=True)
    updated_book = service.update(book_id, update_data)
    return updated_book

@router.delete('/{book_id}')
async def delete_book(book_id: int):
    service.delete(book_id)
    return {"deleted": True}