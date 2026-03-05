import sqlite3
from contextlib import contextmanager

DATABASE_URL = "db/library.db"

class Work_db:
    def __init__(self, DATABASE_URL):
        self.db_work = DATABASE_URL


    @contextmanager
    def get_conn(self):
        conn = sqlite3.connect(self.db_work)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()


    def create(self):
        with self.get_conn() as conn:
            with open("db/schema.sql", "r") as f:
                conn.executescript(f.read())
