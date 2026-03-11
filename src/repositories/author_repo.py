from src.db.database import Conect

import logging


logger = logging.getLogger(__name__)

class AuthorRepo:
    def __init__(self, db:Conect):
        self.db = db
        

    async def add(self, birth_year: int, name: str):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                INSERT INTO authors (birth_year, name)
                VALUES (%s, %s)
                ''', (birth_year, name)
            )
            if cur:
                logger.info('Данные успешнозагрущились')
                return cur.lastrowid
            else:
                logger.error('Какая-то проблема с данными')

    async def get_by_id(self, authors_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                SELECT id, birth_year, name FROM authors
                WHERE id = %s
                ''',
                (authors_id,)
            )
            row = await cur.fetchone()
            return row

    async def delete(self, authors_id):
        async for cur in self.db.cursor(): 
            await  cur.execute(
                '''
                DELETE FROM authors WHERE id = %s
                ''', 
                (authors_id,)
            )
            delete = cur.rowcount > 0
            if delete:
                logger.info('Данные по id {authors_id} успешно удалились')
                return delete
            else:
                logger.error('Прозошла ошибочка, смотри код')

    async def update(self, authors_id: int, birth_year: int, name: str):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                UPDATE authors
                SET birth_year = %s, name = %s
                WHERE id = %s
                ''',
                (birth_year, name, authors_id)
            )
        