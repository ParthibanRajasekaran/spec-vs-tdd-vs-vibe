"""
Tests for vibe mode - added after implementation.
"""
import pytest
from fastapi.testclient import TestClient

from dev_modes.vibe.calculator import final_price
from dev_modes.vibe.app import app


client = TestClient(app)


def test_vat_then_discount():
    """Test VAT applied first, then 10% discount for WELCOME10."""
    result = final_price(100, 20, "WELCOME10")
    assert result == 108.0


def test_unknown_code_no_discount():
    """Test that unknown codes don't apply discount."""
    result = final_price(100, 20, "FOO")
    assert result == 120.0


def test_no_code():
    """Test price calculation without any code."""
    result = final_price(100, 20, None)
    assert result == 120.0


def test_rounding_smoke():
    """Test that rounding works correctly."""
    result = final_price(19.99, 8.5, None)
    assert result == 21.69  # 19.99 * 1.085 = 21.68915, rounds to 21.69


def test_case_insensitive_code():
    """Test that discount code is case-insensitive."""
    assert final_price(100, 20, "welcome10") == 108.0
    assert final_price(100, 20, "WELCOME10") == 108.0
    assert final_price(100, 20, "WeLcOmE10") == 108.0


def test_api_endpoint():
    """Test the FastAPI endpoint directly."""
    response = client.post(
        "/price",
        json={"amount": 100, "vat_pct": 20, "code": "WELCOME10"}
    )
    assert response.status_code == 200
    assert response.json() == {"final": 108.0}


def test_api_endpoint_no_code():
    """Test API endpoint without discount code."""
    response = client.post(
        "/price",
        json={"amount": 100, "vat_pct": 20}
    )
    assert response.status_code == 200
    assert response.json() == {"final": 120.0}

