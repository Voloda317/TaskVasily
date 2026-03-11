from src.config import settings
from src.db.database import Conect

db = Conect(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    db=settings.DB_NAME,
    autocommit=False
)