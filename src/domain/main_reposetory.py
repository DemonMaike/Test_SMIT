from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.models import Rate


class AbstractRepository[T](ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> T:
        pass

    @abstractmethod
    async def get_all(self) -> List[T]:
        pass

    @abstractmethod
    async def add(self, entity: T) -> None:
        pass

    @abstractmethod
    async def update(self, entity: T) -> None:
        pass

    @abstractmethod
    async def delete(self, entity: T) -> None:
        pass


class BaseRepository[T](AbstractRepository):
    def __init__(self, session: AsyncSession, model):
        self.session = session
        self.model = model

    async def get_by_id(self, id: int) -> T:
        result = await self.session.execute(select(self.model).filter_by(id=id))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[T]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def add(self, entity) -> None:
        self.session.add(entity)
        await self.session.commit()

    async def update(self, entity) -> None:
        await self.session.merge(entity)
        await self.session.commit()

    async def delete(self, entity) -> None:
        await self.session.delete(entity)
        await self.session.commit()


class RateRepository[T](BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Rate)