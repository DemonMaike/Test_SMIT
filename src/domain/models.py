from sqlalchemy import Column, String, Float, Date, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Rate(Base):
    __tablename__ = "rates"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date, nullable=False)
    cargo_type = Column(String, nullable=False)
    rate = Column(Float, nullable=False)

