from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from src.logers.logger import setup_logging
from src.config import settings
from src.routers.books import router as books_router
from src.repositories.books import BookRepository 


setup_logging()
logger = logging.getLogger(__name__)

repo = BookRepository()

@asynccontextmanager
async def lifespan(app: FastAPI):
    repo.create_table()
    logger.info('Сервер начал работу')
    yield
    logger.info('Сервер завершил работу')

app = FastAPI(lifespan=lifespan, title=settings.APP_TITLE)

app.include_router(books_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host=settings.HOST, port=settings.PORT, reload=True)