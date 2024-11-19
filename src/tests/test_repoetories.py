import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import (AsyncSession,
                                    async_sessionmaker,
                                    create_async_engine)
from datetime import date
from src.domain.models import Rate, Base
from src.domain.reposetoryies import RateRepository
from settings import settings


@pytest_asyncio.fixture(scope="session")
async def engine():
    engine = create_async_engine(settings.db.get_test_link(), echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture
async def async_session(engine):
    _async_session = async_sessionmaker(engine,
                                        expire_on_commit=False,
                                        class_=AsyncSession)
    async with _async_session() as session:
        yield session
    await session.__aexit__(None, None, None)


@pytest.mark.asyncio
async def test_add_rate(async_session):
    rate_repo = RateRepository(async_session)
    rate = Rate(date=date(2020, 4, 26), cargo_type="Glass", rate=0.05)
    await rate_repo.add(rate)
    getting_rate = await rate_repo.get_by_id(1)
    assert getting_rate is not None
    assert getting_rate.cargo_type == "Glass"


# TODO There will be a need to write all tests
...
