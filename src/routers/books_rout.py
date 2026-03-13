from fastapi import APIRouter, Depends
from fastapi.params import Depends

from src.repositories.books_repo import Book
from src.services.books_services import BookService
from src.db.config import db
from src.model.books_model import BookCreate, BookResponse, BookUpdate, BookFilter
import logging

logger = logging.getLogger(__name__)

repo = Book(db)
service = BookService(repo)

router = APIRouter(prefix='/books', tags=['Books'])


@router.post('/', response_model=BookResponse)
async def create_book(book_data: BookCreate):
    try:
        book = await service.create_book(**book_data.model_dump())
        logger.info('Создание книги прощло успешно')
        return book
    except Exception:
        logger.error('Ошибка при создании книги')
        raise

@router.get('/{book_id}', response_model=BookResponse)
async def get_book(book_id:int):
    try:
        book = await service.get_by_id(book_id)
        logger.info(f'Поиск книги с id {book_id} успешно')
        return book
    except Exception:
        logger.error('Ошибка при создании книги')
        raise

@router.delete('/{book_id}')
async def delete(book_id:int):
    try:
        book = await service.delete(book_id)
        logger.info(f'Удаление по id {book_id} прошло успешно')
        return book
    except Exception:
        logger.error(f'Удаление по id {book_id} закончилось ошибкой')
        raise

@router.put('/{book_id}', response_model=BookResponse)
async def update(book_id: int, book_data: BookUpdate):
    try:
        book = await service.update(
            book_id=book_id,
            **book_data.model_dump(exclude_unset=True)
        )
        logger.info(f'Обновление книги с id {book_id} прошло успешно')
        return book
    except Exception:
        logger.error(f'Ошибка при обновлении книги {book_id}')
        raise

@router.get('/', response_model=list[BookResponse])
async def filter_book(filters: BookFilter = Depends()):
    try:
        book = await service.filter_book(
            **filters.model_dump(exclude_unset=True)
        )
        logger.info('Данные прошли успешно')
        return book
    except Exception as e:
        logger.error(f'Проблем с данными, ошибка {e}')
        raise

