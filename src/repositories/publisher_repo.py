from db.database import Connect

import logging


logger = logging.getLogger(__name__)


class PublicherRepo: 
    def __init__(self, db:Connect):
        self.db = db

    async def add(self, country: str, city: str, 
            year_publicher: int
            ):
        async for cur in self.db.cursor():
            await cursor = cur.execute(
                '''
                INSERT INTO publisher (country, city, year_publicher)
                VALUES (?, ?, ?)
                ''', 
                (country, city, year_publicher)
            )
            return cur.lastrowid

    async def get_by_id(self, publisher_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                SELECT id, country, city, year_publisher
                FROM publisher WHERE id == ?
                ''', 
                (publisher_id,)
            )
            if cur:
                logger.info('Книгу с id {publisher_id} вывели')
                return cur
            else:
                logger.error('У нас ошибка')

    async def delete(self, publisher_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                DELETE FROM authors WHERE id = ?
                ''', 
                (publisher_id,)
            )
            delete = cur.rowcount > 0
            if delete:
                logger.info(f'Уделение по id {publisher_id} успешно прошло')
            else:
                logger.error('У нас с тобой ошибка')

    async def update(self, publisher_id: int, country: str, 
               city: str, year_publisher: str, 
               ):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                UPDATE publisher
                SET country = ?, city = ?, year_publisher = ?
                WHERE id = ? 
                ''', 
                (country, city, year_publisher, publisher_id)
                )
        