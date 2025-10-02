"""
Vibe-mode calculator: straightforward implementation.
"""
from typing import Optional


def final_price(amount: float, vat_pct: float, code: Optional[str] = None) -> float:
    """
    Calculate final price with VAT and optional discount code.

    Args:
        amount: Base amount before VAT
        vat_pct: VAT percentage (e.g., 20 for 20%)
        code: Optional discount code (case-insensitive)

    Returns:
        Final price rounded to 2 decimal places
    """
    # Apply VAT first
    total_with_vat = amount * (1 + vat_pct / 100)

    # Apply discount if code matches
    if code and code.upper() == "WELCOME10":
        total_with_vat *= 0.9  # 10% discount

    # Round to 2 decimal places
    return round(total_with_vat, 2)

