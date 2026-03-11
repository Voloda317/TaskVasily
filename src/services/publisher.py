from src.repositories.publisher_repo import PublicherRepo

import logging

logger = logging.getLogger(__name__)

class PublicherService: 
    def __init__(self, repo:PublicherRepo):
        self.repo = repo 

    async def create_publisher(self, **book_pub):
        pub = await self.repo.add(**book_pub)
        if pub: 
            logger.info('Запись проходит успешно')
            return pub
        else:
            logger.error('У нас ошибка')

    async def get_by_id(self, publisher_id:int):
        pub = await self.repo.get_by_id(publisher_id)
        if pub: 
            logger.info('Все проходит успешно')
        else: 
            logger.error('У нас ошибка')

    async def delete(self, publisher_id:int): 
        pub = await self.repo.delete(publisher_id)
        if pub: 
            logger.info('Удаление книши прошло успешно')
            return pub
        else: 
            logger.error('У нас ошибка')

    async def update(self, publisher_id, **book_pub): 
        await self.repo.update(publisher_id, **book_pub)
        return await self.repo.get_by_id(publisher_id)
    