import aiomysql
import logging

logger = logging.getLogger(__name__)

class Conect:
    def __init__(self, host, port, user, password, db, autocommit=True):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.autocommit = autocommit
        self.conn = None

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
        except Exception as e:
            logger.error(f'Ошибка подключения: {e}')
            raise

    async def close(self):
        if self.conn is None:
            logger.warning('Соединение уже закрыто или не было открыто')
            return
        try:
            self.conn.close()
            logger.info('Соединение с БД закрыто')
        except Exception as e:
            logger.error(f'Ошибка при закрытии соединения: {e}')
            raise

    async def cursor(self):
        if self.conn is None:
            raise RuntimeError('Соединение не установлено. Вызовите connect()')
        try:
            async with self.conn.cursor() as cur:
                yield cur
                await self.conn.commit()
        except Exception as e:
            logger.error(f'Ошибка при работе с курсором: {e}')
            raise

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()