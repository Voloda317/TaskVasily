from src.repositories.books import BookRepository
from src.models.models import Book
import logging

logger = logging.getLogger(__name__)

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, book_data: dict):
        book_id = self.repository.add(book_data)
        new_book = self.repository.get_by_id(book_id)
        if new_book is None:
            logger.error('Не удалось создать книгу')
        else:
            logger.info(f'Книга создана с id {book_id}')
        return new_book

    def get_all_books(self):
        books = self.repository.get_all()
        if books:
            logger.info(f'Найдено книг: {len(books)}')
        else:
            logger.warning('Список книг пуст')
        return books

    def get_book(self, book_id: int):
        book = self.repository.get_by_id(book_id)
        if book:
            logger.info(f'Книга с id {book_id} найдена')
        else:
            logger.warning(f'Книга с id {book_id} не найдена')
        return book

    def delete(self, book_id: int):
        deleted = self.repository.delete(book_id)
        if deleted:
            logger.info(f'Книга с id {book_id} удалена')
        else:
            logger.warning(f'Книга с id {book_id} не найдена, удаление не выполнено')
        return deleted
    
    def update(self, book_id:int, book_data: dict):
        updates =  self.repository.update(book_id, book_data)
        if updates:
            logger.info(f'Книга с id {book_id}, обновилась')
        else:
            logger.error(f'Неизвестная ошибка')
        return updates
    