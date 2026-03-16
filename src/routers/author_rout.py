from fastapi import APIRouter
from fastapi.params import Depends

from src.services.author_services import AuthorService
from src.repositories.author_repo import AuthorRepo
from src.db.config import db
from src.model.authors_model import AuthorsCreate, AuthorsResponse, AuthorsUpdate, FilterAuthor

import logging

logger = logging.getLogger(__name__)

repo = AuthorRepo(db)
service = AuthorService(repo)

router = APIRouter(prefix='/author', tags=['Author'])


@router.post('/',  response_model=AuthorsResponse)
async def create_author(author_data: AuthorsCreate):
    try:
        author = await service.create_author(**author_data.model_dump())
        logger.info('Данные пошли в сервис')
        return author
    except Exception:
        logger.error('Ошибка при создании автора')
        raise


@router.get('/{author_id}', response_model=AuthorsResponse)
async def get_author(author_id: int):
    try:
        author = await service.get_by_id(author_id)
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


@router.put('/{author_id}', response_model=AuthorsResponse)
async def update_author(author_id: int,  author_data: AuthorsUpdate):
    try:
        author = await service.update(
            authors_id=author_id,
            **author_data.model_dump(exclude_unset=True)
        )

        logger.info(f'Автор с id {author_id} успешно обновлён')
        return author
    except Exception:
        logger.error(f'Не удалось обновить автора с id {author_id}')
        raise

@router.get('/', response_model=list[AuthorsResponse])
async def filter_author_rout(authors_fil: FilterAuthor = Depends()):
    try:
        authors = await service.filter_author_ser(**authors_fil.model_dump(exclude_unset=True))
        logger.info('В эндпоитах все хорошо')
        return authors
    except Exception as e:
        logger.error(f'У нас ошибка {e}')
        raise