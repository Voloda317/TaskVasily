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
        logger.error("Не удалось создать книгу (сервис вернул None)")
    return new_book

@app.get('/books/{book_id}', response_model=BookOut)
async def get_book(book_id: int):
    logger.info(f'Начинаем работу с поиск книги по id')
    book = service.get_book(book_id)
    if book is None:
        logger.warning(f'У нас ошибка')
    return book

@app.patch('/books/{book_id}', response_model=BookOut)
async def update_book(book_id: int, book_update: BookUpdate):
    update_data = book_update.model_dump(exclude_unset=True)
    if not update_data:
        logger.warning("Попытка обновления без полей")
    updated_book = service.update(book_id, update_data)
    if updated_book is None:
        logger.warning(f"Книга с id={book_id} не найдена для обновления")
    return updated_book

@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    logger.info(f"Попытка удаления книги id={book_id}")
    deleted = service.delete(book_id)
    if not deleted:
        logger.warning(f"Книга с id={book_id} не найдена для удаления")
    return {"deleted": True}
