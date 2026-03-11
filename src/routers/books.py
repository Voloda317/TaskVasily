from fastapi import APIRouter

from src.repositories.books_repo import Book
from src.services.books import BookService
from src.db.config import db
import logging

logger = logging.getLogger(__name__)

repo = Book(db)
service = BookService(repo)

router = APIRouter(prefix='/books', tags=['Books'])


@router.post('/')
async def create_book(
    namebook: str,
    genre: str,
    pages: int,
    publisher_id: int
):
    try:
        book = await service.create_book(
            namebook=namebook,
            genre=genre,
            pages=pages,
            publisher_id=publisher_id
        )
        logger.info('Создание книги прощло успешно')
        return book
    except Exception:
        logger.error('Ошибка при создании книги')
        raise

@router.get('/{book_id}')
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

@router.put('/{book_id}')
async def update(
    book_id: int,
    author_id: int,
    namebook: str,
    genre: str,
    pages: int,
    publisher_id: int
):
    try:
        book = await service.update(
            book_id=book_id,
            author_id=author_id,
            namebook=namebook,
            genre=genre,
            pages=pages,
            publisher_id=publisher_id
        )

        logger.info(f'Обновление книги с id {book_id} прошло успешно')
        return book

    except Exception:
        logger.error(f'Ошибка при обновлении книги {book_id}')
        raise
