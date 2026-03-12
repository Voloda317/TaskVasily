from src.repositories.books_repo import Book 
import logging 

logger = logging.getLogger(__name__)


class BookService:
    def __init__(self, book_repo: Book):
        self.book_repo = book_repo

    async def create_book(self, **book_sl ):
        book = await self.book_repo.add_book(**book_sl)
        return await self.book_repo.get_by_id(book)
    
    async def get_by_id(self, book_id:int):
        book = await self.book_repo.get_by_id(book_id)
        if book: 
            logger.info('Все проходит успешно')
            return book 
        else:
            logger.error('У нас где ошибка при выводе')

    async def delete(self, book_id:int):
        book = await self.book_repo.delete(book_id)
        if book: 
            logger.info('Удаление проходит успешно')
            return book
        
    async def update(self, book_id: int, **book_sl):
        await self.book_repo.update(book_id=book_id,**book_sl)
        return await self.book_repo.get_by_id(book_id)
    