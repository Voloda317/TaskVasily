import aiomysql
import logging

logger = logging.getLogger(__name__)

class Conect():
    def __init__(self, host, port, 
                user, password, 
                db, autocommit=True
                ):
        self.host=host
        self.port=port
        self.user=user 
        self.password=password
        self.db=db 
        self.autocommit=autocommit

    async def connect(self): 
        try:    
            self.conn = await aiomysql.connect(
                host=self.host, 
                port=self.port, 
                user=self.user, 
                password=self.password, 
                db=self.db,
                autocommit=self.autocommit
            )
            logger.info('Успешно подключились')
        except: 
            logger.info('У нас ошибка с подключением')

    async def close(self):
        try:    
            self.conn.close()
            logger.info('Соединение с бд закрыто')
        except:
            logger.error('У нас какая-то ошибка')


    async def cursor(self):
        try:    
            async with self.conn.cursor() as cur:
                yield cur
                await self.conn.commit()
                logger.info('Успешно')
        except:
            logger.error('Проблема с соединением')
