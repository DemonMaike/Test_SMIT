from pydantic import BaseModel
from datetime import date


class RateCreate(BaseModel):
    cargo_type: str
    rate: float


class RateRequest(BaseModel):
    date: date
    rates: dict[str, RateCreate]


class CalculateRequest(BaseModel):
    cargo_type: str
    rate_date: date
    declared_value: float


class CalculateResponse(BaseModel):
    cargo_type: str
    rate: float
    declared_value: float
    insurance_cost: float
    date: date

    class Config:
        from_attributes = True
