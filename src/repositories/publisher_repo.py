from src.db.database import Conect
import logging
from src.model.publisher_model import PublisherFilter
from typing import Optional
logger = logging.getLogger(__name__)

class PublisherRepo:
    def __init__(self, db: Conect):
        self.db = db

    async def add(self, country: str, city: str, year_publisher: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                INSERT INTO publishers (country, city, year_publisher)
                VALUES (%s, %s, %s)
                ''',
                (country, city, year_publisher)
            )
            return cur.lastrowid

    async def get_by_id(self, publisher_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                SELECT id, country, city, year_publisher
                FROM publishers
                WHERE id = %s
                ''',
                (publisher_id,)
            )
            row = await cur.fetchone()

            if row:
                return {
                    "id": row[0],
                    "country": row[1],
                    "city": row[2],
                    "year_publisher": row[3]
                }
            return None

    async def delete(self, publisher_id: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                DELETE FROM publishers
                WHERE id = %s
                ''',
                (publisher_id,)
            )
            deleted = cur.rowcount > 0
            return deleted

    async def update(self, publisher_id: int, country: str, city: str, year_publisher: int):
        async for cur in self.db.cursor():
            await cur.execute(
                '''
                UPDATE publishers
                SET country = %s, city = %s, year_publisher = %s
                WHERE id = %s
                ''',
                (country, city, year_publisher, publisher_id)
            )


    async def filter_pub(self, id: Optional[int] = None,
        country: Optional[str] = None,
        city: Optional[str] = None,
        year_publisher: Optional[int] = None):
        query = (
            '''
            SELECT id, country, city, year_publisher
            FROM publishers
            WHERE 1=1
            '''
        )
        param = []
        if id:
            query += ' AND id = %s'
            param.append(id)
        if country:
            query += ' AND country = %s'
            param.append(country)
        if city:
            query += ' AND city = %s'
            param.append(city)
        if year_publisher:
            query += ' AND year_publisher = %s'
            param.append(year_publisher)

        async for cur in self.db.cursor():
            await cur.execute(query, param)
            rows = await cur.fetchall()
            publishers = []
            for row in rows:
                publishers.append({
                    'id': row[0],
                    'country': row[1],
                    'city': row[2],
                    'year_publisher': row[3]
                })
            return publishers



