from db.database import Work_db

import logging

bd = Work_db()

logger = logging.getLogger(__name__)

class Book:
    def add_book(
        self,
        author_id: int,
        namebook: str,
        genre: str,
        pages: int,
        publisher_id: int
        ):
        with bd.get_conn() as conn:
            cursor = conn.execute(
                '''
                INSERT INTO books (author_id, namebook, genre, pages, publisher_id)
                VALUES (?, ?, ?, ?, ?)
                ''', (author_id, namebook, genre, pages, publisher_id)
            )
            conn.commit()
            if cursor:
                logger.info(f'Книга успешна добавлена')
                return cursor.lastrowid
            else:
                logger.error('Проиозошла ошибка')

    def get_by_id(self, book_id: int):
        with bd.get_conn() as conn:
            row = conn.execute(
                'SELECT id, author_id, namebook, genre, pages, publisher_id FROM books WHERE id = ?',
                (book_id,)
            ).fetchone()
        return row
        
    def delete(self, book_id: int):
        with bd.get_conn() as conn:
            cursor = conn.execute(
                'DELETE FROM books WHERE id = ? ', 
                 (book_id,)
            )    
            conn.commit()
            deleted = cursor.rowcount > 0 
            if deleted:
                logger.info(f'Данные с id {book_id} успешно удалились')
            else:
                logger.error(f'Данные с id {book_id} не найдены или произошла ошибка')
            return deleted

    def update(self, book_id: int, 
        author_id: int,
        namebook: str,
        genre: str,
        pages: int,
        publisher_id: int
               ):
        with bd.get_conn() as conn:
            conn.execute(
                '''
                UPDATE books 
                SET author_id = ?, namebook = ?, genre = ?, 
                pages = ?, publisher_id = ?
                WHERE id = ?
                ''', 
                ( author_id, namebook, genre, pages, publisher_id, book_id)
            )
            conn.commit()
        return self.get_by_id(book_id)
