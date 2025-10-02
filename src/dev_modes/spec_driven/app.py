"""
Spec-driven FastAPI app.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from dev_modes.spec_driven.calculator import final_price


app = FastAPI(title="Spec-Driven Mode - Price API")


class PriceRequest(BaseModel):
    """Request schema per specification."""
    amount: float
    vat_pct: float
    code: Optional[str] = None


class PriceResponse(BaseModel):
    """Response schema per specification."""
    final: float


@app.post("/price", response_model=PriceResponse)
def calculate_price(request: PriceRequest) -> PriceResponse:
    """
    Calculate final price according to specification.

    Spec: POST /price endpoint
    - Input: amount (float), vat_pct (float), code (string, optional)
    - Output: final (float)
    - Behavior: Apply VAT first, then 10% discount for "WELCOME10"
    """
    result = final_price(request.amount, request.vat_pct, request.code)
    return PriceResponse(final=result)

