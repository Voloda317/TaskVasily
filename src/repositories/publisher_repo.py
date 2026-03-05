from db.database import Work_db

import logging

repo = Work_db()

logger = logging.getLogger(__name__)


class PublicherRepository: 

    def add(self, country: str, city: str, 
            year_publicher: int
            ):
        with repo.get_conn() as conn:
            cursor = conn.execute(
                '''
                INSERT INTO publisher (country, city, year_publicher)
                VALUES (?, ?, ?)
                ''', 
                (country, city, year_publicher)
            )
            conn.commit()
            return cursor.lastrowid

    def get_by_id(self, publisher_id: int):
        with repo.get_conn() as conn:
            cursor = conn.execute(
                '''
                SELECT id, country, city, year_publisher
                FROM publisher WHERE id == ?
                ''', 
                (publisher_id,)
            )
            conn.commit()
            if cursor:
                logger.info('Книгу с id {publisher_id} вывели')
                return cursor
            else:
                logger.error('У нас ошибка')

    def delete(self, publisher_id: int):
        with repo.get_conn() as conn:
            cursor = conn.execute(
                '''
                DELETE FROM authors WHERE id = ?
                ''', 
                (publisher_id,)
            )
            conn.commit()
            delete = cursor.rowcount > 0
            if delete:
                logger.info(f'Уделение по id {publisher_id} успешно прошло')
            else:
                logger.error('У нас с тобой ошибка')

    def update(self, publisher_id: int, country: str, 
               city: str, year_publisher: str, 
               ):
        with repo.get_conn() as conn:
            conn.execute(
                '''
                UPDATE publisher
                SET country = ?, city = ?, year_publisher = ?
                WHERE id = ? 
                ''', 
                (country, city, year_publisher, publisher_id)
            )
            conn.commit()
            return self.get_by_id(publisher_id)
        