from fastapi import FastAPI
from src.routers.books import router as books_router
from src.routers.publisher import router as publisher_router
from src.routers.author import router as author_router
from src.db.config import db
from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.close()

app = FastAPI(
    title="Books API",
    lifespan=lifespan
    )


app.include_router(books_router)
app.include_router(publisher_router)
app.include_router(author_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)