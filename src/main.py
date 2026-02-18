from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from typing import List
import logging

from src.repositories.books import BookRepository
from src.services.books import BookService
from src.models.models import BookCreate, BookOut, BookUpdate
from src.logers.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

repo = BookRepository()
service = BookService(repo)

@asynccontextmanager
async def lifespan(app: FastAPI):
    repo.create_table()
    logger.info('Сервер начал работу')
    yield
    logger.info('Сервер завершил работу')

app = FastAPI(lifespan=lifespan)

@app.get("/books", response_model=List[BookOut])
async def get_books():
    return service.get_all_books()

@app.post('/books', response_model=BookOut)
async def create_book(book: BookCreate):
    new_book = service.create_book(book.model_dump())
    if new_book is None:
        raise HTTPException(status_code=500, detail="Failed to create book")
    return new_book

@app.get('/books/{book_id}', response_model=BookOut)
async def get_book(book_id: int):
    book = service.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.patch('/books/{book_id}', response_model=BookOut)
async def update_book(book_id: int, book_update: BookUpdate):
    update_data = book_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    updated_book = service.update(book_id, update_data)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    deleted = service.delete(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"deleted": True}
