"""
TDD tests: written before implementation.
Tests focus on behaviour, not implementation details.
"""
import pytest
from fastapi.testclient import TestClient

from dev_modes.tdd.calculator import price_with_vat, apply_discount, final_price
from dev_modes.tdd.app import app


client = TestClient(app)


class TestPriceWithVat:
    """Test VAT calculation in isolation."""

    def test_vat_calculation(self):
        """VAT should be applied correctly and rounded."""
        assert price_with_vat(19.99, 8.5) == 21.69

    def test_simple_vat(self):
        """Simple case: 100 with 20% VAT."""
        assert price_with_vat(100, 20) == 120.0

    def test_zero_vat(self):
        """Zero VAT returns original amount."""
        assert price_with_vat(100, 0) == 100.0


class TestApplyDiscount:
    """Test discount application."""

    def test_welcome10_code(self):
        """WELCOME10 applies 10% discount."""
        assert apply_discount(120.0, "WELCOME10") == 108.0

    def test_case_insensitive(self):
        """Code should be case-insensitive."""
        assert apply_discount(120.0, "welcome10") == 108.0
        assert apply_discount(120.0, "WeLcOmE10") == 108.0

    def test_invalid_code_no_discount(self):
        """Invalid code returns original total."""
        assert apply_discount(120.0, "nope") == 120.0

    def test_none_code_no_discount(self):
        """None code returns original total."""
        assert apply_discount(120.0, None) == 120.0

    def test_rounding(self):
        """Discount should round correctly."""
        assert apply_discount(100.0, "WELCOME10") == 90.0


class TestFinalPrice:
    """Test complete price calculation: VAT then discount."""

    def test_vat_then_discount(self):
        """100 + 20% VAT = 120, then -10% = 108."""
        assert final_price(100, 20, "WELCOME10") == 108.0

    def test_no_code(self):
        """Without code, only VAT applies."""
        assert final_price(100, 20, None) == 120.0

    def test_invalid_code(self):
        """Invalid code doesn't apply discount."""
        assert final_price(100, 20, "nope") == 120.0

    def test_complex_rounding(self):
        """Test rounding with complex numbers."""
        # 50 * 1.15 = 57.5, * 0.9 = 51.75
        assert final_price(50, 15, "WELCOME10") == 51.75


class TestAPI:
    """Test FastAPI endpoint."""

    def test_post_with_code(self):
        """API should calculate with discount code."""
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20, "code": "WELCOME10"}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 108.0}

    def test_post_without_code(self):
        """API should work without discount code."""
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 120.0}

    def test_post_invalid_code(self):
        """API should ignore invalid codes."""
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20, "code": "INVALID"}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 120.0}

