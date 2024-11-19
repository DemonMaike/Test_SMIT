from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.routes import router
from src.db.settings import create_db, drop_db

porcesses = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield
    await drop_db()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
