from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.domain.models import Base
from settings import settings

database_settings = settings.db
DB_URL = database_settings.get_prod_link()
TEST_DB_URL = database_settings.get_test_link()


engine = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(
    engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
