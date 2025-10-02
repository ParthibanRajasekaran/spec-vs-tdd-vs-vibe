"""
TDD-mode FastAPI app.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from dev_modes.tdd.calculator import final_price


app = FastAPI(title="TDD Mode - Price API")


class PriceRequest(BaseModel):
    """Request model for price calculation."""
    amount: float
    vat_pct: float
    code: Optional[str] = None


class PriceResponse(BaseModel):
    """Response model for price calculation."""
    final: float


@app.post("/price", response_model=PriceResponse)
def calculate_price(request: PriceRequest) -> PriceResponse:
    """
    Calculate final price with VAT and optional discount code.

    Business rule: VAT is applied first, then discount.
    """
    result = final_price(request.amount, request.vat_pct, request.code)
    return PriceResponse(final=result)

