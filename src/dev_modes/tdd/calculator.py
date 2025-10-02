"""
TDD-mode calculator: built to satisfy tests.
Small, testable functions following red-green-refactor cycle.
"""
from typing import Optional


def price_with_vat(amount: float, vat_pct: float) -> float:
    """
    Apply VAT to a base amount.

    Args:
        amount: Base amount before VAT
        vat_pct: VAT percentage (e.g., 20 for 20%)

    Returns:
        Amount with VAT, rounded to 2 decimal places
    """
    return round(amount * (1 + vat_pct / 100), 2)


def apply_discount(total: float, code: Optional[str]) -> float:
    """
    Apply discount code to total if valid.

    Args:
        total: Amount before discount
        code: Discount code (case-insensitive)

    Returns:
        Discounted amount rounded to 2 decimal places, or original total if code invalid
    """
    if code and code.upper() == "WELCOME10":
        return round(total * 0.9, 2)
    return total


def final_price(amount: float, vat_pct: float, code: Optional[str] = None) -> float:
    """
    Calculate final price: VAT first, then discount.

    Args:
        amount: Base amount before VAT
        vat_pct: VAT percentage (e.g., 20 for 20%)
        code: Optional discount code

    Returns:
        Final price rounded to 2 decimal places
    """
    total_with_vat = price_with_vat(amount, vat_pct)
    return apply_discount(total_with_vat, code)

