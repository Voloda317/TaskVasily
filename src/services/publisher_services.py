from src.repositories.publisher_repo import PublisherRepo

import logging

logger = logging.getLogger(__name__)

class PublisherService:
    def __init__(self, repo:PublisherRepo):
        self.repo = repo 

    async def create_publisher(self, **publisher_pub):
        try:
            publisher_id = await self.repo.add(**publisher_pub)
            logger.info('Запись проходит успешно')
            return await self.get_by_id(publisher_id)
        except:
            logger.error('У нас ошибка')
            raise

    async def get_by_id(self, publisher_id:int):
        publisher  = await self.repo.get_by_id(publisher_id)
        if publisher :
            logger.info('Все проходит успешно')
            return publisher
        else: 
            logger.error('У нас ошибка')

    async def delete(self, publisher_id:int): 
        pub = await self.repo.delete(publisher_id)
        if pub: 
            logger.info('Удаление книши прошло успешно')
            return pub
        else: 
            logger.error('У нас ошибка')

    async def update(self, publisher_id, **publisher_pub):
        await self.repo.update(publisher_id, **publisher_pub)
        return await self.repo.get_by_id(publisher_id)

    async def filter(self, **filters):
        try:
            publisher_filter = await self.filter(**filters)
            logger.info('Данные в сервисе прошли успешно')
            return publisher_filter
        except Exception as e:
            logger.error(f'Проблема с данными в сервисе, ошибка {e}')
            raise
