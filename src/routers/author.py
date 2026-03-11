from fastapi import APIRouter

from src.services.author import AuthorService
from src.repositories.author_repo import AuthorRepo
from src.db.config import db

import logging

logger = logging.getLogger(__name__)

repo = AuthorRepo(db)
service = AuthorService(repo)

router = APIRouter(prefix='/author', tags=['Author'])


@router.post('/')
async def create_author(birth_year: int, name: str):
    try:
        author = await service.create_author(
            birth_year=birth_year,
            name=name
        )
        logger.info('Автор успешно создан')
        return author
    except Exception:
        logger.error('Ошибка при создании автора')
        raise


@router.get('/{author_id}')
async def get_author(author_id: int):
    try:
        author = await service.search_id(author_id)
        logger.info(f'Автор с id {author_id} найден')
        return author
    except Exception:
        logger.error(f'Ошибка при получении автора с id {author_id}')
        raise


@router.delete('/{author_id}')
async def delete_author(author_id: int):
    try:
        author = await service.delete(author_id)
        logger.info(f'Автор с id {author_id} успешно удалён')
        return author
    except Exception:
        logger.error(f'Не удалось удалить автора с id {author_id}')
        raise


@router.put('/{author_id}')
async def update_author(authors_id: int, birth_year: int, name: str):
    try:
        author = await service.update(
            authors_id=authors_id,
            birth_year=birth_year,
            name=name
        )

        logger.info(f'Автор с id {authors_id} успешно обновлён')
        return author
    except Exception:
        logger.error(f'Не удалось обновить автора с id {authors_id}')
        raise
