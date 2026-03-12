from fastapi import APIRouter
from select import select

from src.db.config import db
from src.repositories.publisher_repo import PublisherRepo
from src.services.publisher_services import PublisherService
from src.model.publisher_model import PublisherCreate,PublisherResponse, PublisherUpdate

import logging

logger = logging.getLogger(__name__)

repo = PublisherRepo(db)
service = PublisherService(repo)

router = APIRouter(prefix='/publisher', tags=['publisher'])

@router.post('', response_model=PublisherResponse)
async def create_publisher(publisher_data: PublisherCreate):
    try:
        publisher = await service.create_publisher(**publisher_data.model_dump())
        logger.info('О публикации успешно создан')
        return publisher
    except Exception:
        logger.error('Ошибка при создании публикации')
        raise

@router.get('/{publisher_id}', response_model=PublisherResponse)
async def get_publisher(publisher_id:int):
    try:
        publisher = await service.get_by_id(publisher_id)
        logger.info(f'Поиск книги с id  {publisher_id} прошла успешно')
        return publisher
    except Exception:
        logger.error(f'Публикацию с id{publisher_id} не удалось создать')
        raise

@router.delete('/{publisher_id}')
async def delete(publisher_id):
    try:
        publisher = await service.delete(publisher_id)
        logger.info(f'Удалили запись с id{publisher_id}')
        return publisher
    except Exception:
        logger.error(f'Книгу с id {publisher_id} не удалось удалить')
        raise

@router.put('/{publisher_id}', response_model=PublisherResponse)
async def update(publisher_id: int, publisher_data: PublisherUpdate):
    try:
        publisher = await service.update(
            publisher_id,
            **publisher_data.model_dump(exclude_unset=True)
        )
        logger.info(f'Запись с id{publisher_id} успешно обновили')
        return publisher
    except Exception:
        logger.error(f'Запись c id {publisher_id} не удалось обновить')
        raise
