from src.repositories.author_repo import AuthorRepo
import logging

logger = logging.getLogger(__name__)


class AuthorService:
    def __init__(self, repo: AuthorRepo):
        self.repo = repo

    async def create_author(self, **book_pub):
        try:
            author_id = await self.repo.add(**book_pub)
            logger.info('Данные пошли в слой репозитория')
            return await self.repo.get_by_id(author_id)
        except Exception:
            logger.error('Проблема в сервисном слое')
            raise

    async def get_by_id(self, authors_id: int):
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

    async def filter_author_ser(self, **authors_filter):
        try:
            authors = await self.repo.filter_author(**authors_filter)
            logger.info('Данные в сервисном слое успешно')
            return authors
        except Exception as e:
            logger.error(f'У нас ошибка в сервисном слое {e}')
            raise
