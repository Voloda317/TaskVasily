from fastapi import APIRouter
from select import select

from src.db.config import db
from src.repositories.publisher_repo import PublicherRepo
from src.services.publisher import PublicherService

import logging

logger = logging.getLogger(__name__)

repo = PublicherRepo(db)
service = PublicherService(repo)

router = APIRouter(prefix='/publisher', tags=['publisher'])

@router.post('')
async def create_publicher(country: str, city: str,
            year_publicher: int):
    try:
        publisher = await service.create_publisher(
            country=country,
            city=city,
            year_publicher=year_publicher
        )
        logger.info('О публикации успешно создан')
        return publisher
    except Exception:
        logger.error('Ошибка при создании публикации')
        raise

@router.get('/{publisher_id}')
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

@router.put('/{publisher_id}')
async def update(publisher_id: int, country: str,
               city: str, year_publisher: str,
    ):
    try:
        publisher = await service.update(
            publisher_id=publisher_id,
            country=country,
            city=city,
            year_publisher=year_publisher
        )
        logger.info(f'Запись с id{publisher_id} успешно обновили')
        return publisher
    except Exception:
        logger.error(f'Запись c id {publisher_id} не удалось обновить')
        raise

