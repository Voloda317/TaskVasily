import sqlite3
from contextlib import contextmanager
from typing import List, Optional
from src.models.models import Book, BookUpdate, BookCreate, BookOut
import logging

logger = logging.getLogger(__name__)

DATABASE_NAME = 'books.db'

class BookRepository:
    def __init__(self, db_path: str = DATABASE_NAME):
        self.db_path = db_path

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def create_table(self):
        try:
            with self.get_connection() as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        book TEXT NOT NULL,
                        author TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        publication TEXT NOT NULL
                    )
                ''')
                conn.commit()
            logger.info('Таблица успешно создана')
        except Exception as e:
            logger.error(f'Не удалось создать таблицу: {e}')

    def add(self, book_data: dict):
        with self.get_connection() as conn:
            cursor = conn.execute(
                '''
                INSERT INTO books (book, author, year, publication)
                VALUES (:book, :author, :year, :publication)
                ''', book_data
            )
            conn.commit()
            return cursor.lastrowid

    def get_all(self):
        with self.get_connection() as conn:
            rows = conn.execute(
                'SELECT id, book, author, year, publication FROM books'
            ).fetchall()
            books = [BookOut(**row) for row in rows]
            logger.info(f'Найдено книг: {len(books)}')
            return books

    def get_by_id(self, book_id: int):
        with self.get_connection() as conn:
            row = conn.execute(
                'SELECT id, book, author, year, publication FROM books WHERE id = ?',
                (book_id,)
            ).fetchone()
            if row:
                book = Book(**row)
                logger.info(f'Книга с id {book_id} найдена')
                return book
            logger.warning(f'Книга с id {book_id} не найдена')
            return None

    def delete(self, book_id: int):
        with self.get_connection() as conn:
            cursor = conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()
            deleted = cursor.rowcount > 0
            if deleted:
                logger.info(f"Книга с id {book_id} удалена")
            else:
                logger.warning(f"Книга с id {book_id} не найдена, удаление не выполнено")
            return deleted
        
    def update(self, book_id: int, book_data: dict):
        with self.get_connection() as conn:
            conn.execute(
                '''
                UPDATE books
                SET book = :book, author = :author, year = :year, publication = :publication
                WHERE id = :id
                ''',
                {**book_data, "id": book_id}
            )
            conn.commit()
            return self.get_by_id(book_id)
            