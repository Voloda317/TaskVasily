from src.repositories.author_repo import AuthorRepo

import logging

logger = logging.getLogger(__name__)


class AuthorService:
    def __init__(self, repo: AuthorRepo):
        self.repo = repo

    async def create_author(self, **book_pub):
        create = await self.repo.add(**book_pub)
        return create

    async def search_id(self, authors_id: int):
        search = await self.repo.get_by_id(authors_id)
        if search:
            logger.info('Поиск прошел успешно')
            return search
        else:
            logger.error('У нас произошла ошибка')
            return None

    async def delete(self, authors_id: int):
        delet = await self.repo.delete(authors_id)
        if delet:
            logger.info('Запись прошла успешно')
            return delet
        else:
            logger.error('У нас прошла ошибка')
            return None

    async def update(self, authors_id: int, **book_pub):
        await self.repo.update(authors_id=authors_id, **book_pub)
        return await self.repo.get_by_id(authors_id)
