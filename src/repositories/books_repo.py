from src.db.database import Conect
import logging
from typing import Optional


logger = logging.getLogger(__name__)

class Book:
    def __init__(self, db: Conect):
        self.db = db

    async def add_book(
        self,
        author_id: int,
        namebook: str,
        genre: str,
        pages: int,
        publisher_id: int
    ):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                INSERT INTO `books` (`author_id`, `namebook`, `genre`, `pages`, `publisher_id`)
                VALUES (%s, %s, %s, %s, %s)
                ''',
                (author_id, namebook, genre, pages, publisher_id)
            )
            result = cur.lastrowid
            print(result)
            return result

    async def get_by_id(self, book_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                SELECT id, author_id, namebook, genre, pages, publisher_id
                FROM books
                WHERE id = %s
                ''',
                (book_id,)
            )
            row = await cur.fetchone()

            if row:
                return {
                    "id": row[0],
                    "author_id": row[1],
                    "namebook": row[2],
                    "genre": row[3],
                    "pages": row[4],
                    "publisher_id": row[5]
                }
            return None

    async def delete(self, book_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                'DELETE FROM books WHERE id = %s',
                (book_id,)
            )
            return cur.rowcount > 0

    async def update(
        self,
        book_id: int,
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
                (author_id, namebook, genre, pages, publisher_id, book_id)
            )


    async def filter_book(self, id: Optional[int] = None,
        author_id: Optional[int] = None,
        namebook: Optional[str] = None,
        genre: Optional[str] = None,
        pages: Optional[int] = None,
        publisher_id: Optional[int] = None):
        query = '''
        SELECT id, author_id, namebook, genre, pages, publisher_id
        FROM books
        WHERE 1=1
        '''
        param = []
        if id: 
            query += 'AND id = %s'
            param.append(id)
        if author_id:
            query += 'AND author_id = %s'
            param.append(author_id)
        if namebook:
            query += 'AND namebook = %s'
            param.append(namebook)
        if genre:
            query += 'AND genre = %s'
            param.append(genre)
        if pages:
            query += 'AND pages = %s'
            param.append(pages)
        if publisher_id:
            query += 'AND publisher_id = %s'
            param.append(publisher_id)

        async for cur in self.db.cursor():
            await cur.execute(query, param)
            rows = await cur.fetchall()
            books = []
            for row in rows:
                books.append({
                    'id':row[0],
                    'author_id': row[1],
                    'namebook': row[2],
                    'genre': row[3],
                    'pages': row[4],
                    'publisher_id': row[5]
                })
            return books

