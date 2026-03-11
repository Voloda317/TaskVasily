from src.db.database import Conect

import logging


logger = logging.getLogger(__name__)

class Book:
    def __init__(self, db: Conect):
        self.db = db


    async def add_book(
        self,
        namebook: str,
        genre: str,
        pages: int,
        publisher_id: int
        ):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                INSERT INTO books (namebook, genre, pages, publisher_id)
                VALUES (%s, %s, %s, %s)
                ''', (namebook, genre, pages, publisher_id)
            )
            if cur:
                logger.info(f'Книга успешна добавлена')
                return cur.lastrowid
            else:
                logger.error('Проиозошла ошибка')

    async def get_by_id(self, book_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                'SELECT id, author_id, namebook, genre, pages, publisher_id FROM books WHERE id = %s',
                (book_id,)
            ).fetchone()
        return cur
        
    async def delete(self, book_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                'DELETE FROM books WHERE id = %s', 
                 (book_id,)
            )    
            deleted = cur.rowcount > 0 
            if deleted:
                logger.info(f'Данные с id {book_id} успешно удалились')
                return deleted
            else:
                logger.error(f'Данные с id {book_id} не найдены или произошла ошибка')


    async def update(self, book_id: int, 
        author_id: int,
        namebook: str,
        genre: str,
        pages: int,
        publisher_id: int
               ):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                UPDATE books 
                SET author_id = %s, namebook = %s, genre = %s, 
                pages = %s, publisher_id = %s
                WHERE id = %s
                ''', 
                ( author_id, namebook, genre, pages, publisher_id, book_id)
            )
        return await self.get_by_id(book_id)