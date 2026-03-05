from db.database import Work_db

import logging

repo = Work_db()

logger = logging.getLogger(__name__)

class AuthorRepositiry:
    
    def add(self, birth_year: int, name: str):
        with repo.get_conn() as conn:
            cursor = conn.execute(
                '''
                INSERT INTO authors (birth_year, name)
                VALUES (?, ?)
                ''', (birth_year, name)
            )
            conn.commit()
            if cursor:
                logger.info('Данные успешнозагрущились')
                return cursor.lastrowid()
            else:
                logger.error('Какая-то проблема с данными') 

    def get_by_id(self, authors_id: int):
        with repo.get_conn as conn: 
            cursor = conn.execute(
                '''
                SELECT id, birth_year, name FROM authors
                WHERE id = ?
                ''', 
                (authors_id,)
            )
            conn.commit()
            if cursor:
                logger.info('Данные с id {id} успешно вывелись')
                return cursor
            else:
                logger.error('Пробла у нас')

    def delete(self, authors_id):
        with repo.get_conn() as conn: 
            cursor = conn.execute(
                '''
                DELETE FROM authors WHERE id = ?
                ''', 
                (authors_id,)
            )
            conn.commit()
            delete = cursor.rowcount > 0
            if delete:
                logger.info('Данные по id {authors_id} успешно удалились')
            else:
                logger.error('Прозошла ошибочка, смотри код')

    def update(self, author_id: int, birth_year: int, name: str): 
        with repo.get_conn() as conn: 
            conn.execute(
                '''
                UPDATE authors
                SET birth_year = ?, name = ?
                WHERE id = ?
                ''', 
                (birth_year, name, author_id)
            )
            conn.commit()
            return self.get_by_id(author_id)
        