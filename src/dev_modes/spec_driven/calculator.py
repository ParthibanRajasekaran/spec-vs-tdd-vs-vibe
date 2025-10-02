"""
Spec-driven calculator: implements the spec contract.
"""
from typing import Optional


def final_price(amount: float, vat_pct: float, code: Optional[str] = None) -> float:
    """
    Calculate final price according to spec.

    Specification:
    - Apply VAT percentage to base amount
    - If code is "WELCOME10" (case-insensitive), apply 10% discount
    - Round result to 2 decimal places

    Args:
        amount: Base amount before VAT
        vat_pct: VAT percentage (e.g., 20 for 20%)
        code: Optional discount code

    Returns:
        Final price rounded to 2 decimal places
    """
    # Step 1: Apply VAT
    total = amount * (1 + vat_pct / 100)

    # Step 2: Apply discount if code matches spec
    if code and code.upper() == "WELCOME10":
        total *= 0.9

    # Step 3: Round as per spec
    return round(total, 2)

