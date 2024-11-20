from fastapi import APIRouter, File, HTTPException, Depends, UploadFile
import json
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from src.db.settings import get_async_session
from src.schemas import schema
from src.domain import models
from src.domain.repositories import RateRepository


router = APIRouter(tags=['For clients'])


@router.post("/rates/")
async def create_rates(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_async_session),
):
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="File must be a JSON file")

    contents = await file.read()
    try:
        data = json.loads(contents)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")

    rate_repository = RateRepository(db)

    try:
        for date_str, rates in data.items():
            rate_date = date.fromisoformat(date_str)
            for rate_info in rates:
                db_rate = models.Rate(
                    date=rate_date,
                    cargo_type=rate_info["cargo_type"],
                    rate=float(rate_info["rate"]),
                )
                await rate_repository.add(db_rate)

    # FIX only for testing
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding rates: {e}")

    return {"message": "Rates successfully added."}


@router.post("/calculate/", response_model=schema.CalculateResponse)
async def calculate_insurance(
    request: schema.CalculateRequest,
    db: AsyncSession = Depends(get_async_session),
):
    rate_repository = RateRepository(db)

    db_rate = await rate_repository.get_latest_by_type(request.cargo_type)
    if db_rate is None:
        raise HTTPException(
            status_code=404,
            detail="Rate not found for the given date and cargo type"
        )

    insurance_cost = request.declared_value * db_rate.rate

    return schema.CalculateResponse(
        cargo_type=request.cargo_type,
        rate=db_rate.rate,
        declared_value=request.declared_value,
        insurance_cost=insurance_cost,
        date=request.rate_date,
    )
