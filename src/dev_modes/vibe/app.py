"""
Vibe-mode FastAPI app.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from dev_modes.vibe.calculator import final_price


app = FastAPI(title="Vibe Mode - Price API")


class PriceRequest(BaseModel):
    amount: float
    vat_pct: float
    code: Optional[str] = None


class PriceResponse(BaseModel):
    final: float


@app.post("/price", response_model=PriceResponse)
def calculate_price(request: PriceRequest) -> PriceResponse:
    """Calculate final price with VAT and discount code."""
    result = final_price(request.amount, request.vat_pct, request.code)
    return PriceResponse(final=result)

