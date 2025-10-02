"""
Spec-driven tests: treat the spec as the contract.
Tests verify that implementation matches the specification.
"""
import pytest
from fastapi.testclient import TestClient

from dev_modes.spec_driven.app import app


client = TestClient(app)


class TestSpecCompliance:
    """Tests derived directly from price.feature specification."""

    def test_scenario_vat_then_discount(self):
        """
        From spec: Given base=100, VAT=20%, code="WELCOME10", then final=108.0

        This is the contract defined in price.feature.
        """
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20, "code": "WELCOME10"}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 108.0}

    def test_spec_without_code(self):
        """
        Implied by spec: Without discount code, only VAT applies.

        This is an extension of the spec to handle the optional code field.
        Base=100, VAT=20% -> final=120.0
        """
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 120.0}

    def test_spec_invalid_code(self):
        """
        Implied by spec: Invalid codes don't apply discount.

        Only "WELCOME10" is specified to apply discount.
        """
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20, "code": "INVALID"}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 120.0}

    def test_spec_case_insensitive(self):
        """
        Spec extension: Code matching should be case-insensitive.

        This is a reasonable interpretation for user-friendly behavior.
        """
        response = client.post(
            "/price",
            json={"amount": 100, "vat_pct": 20, "code": "welcome10"}
        )
        assert response.status_code == 200
        assert response.json() == {"final": 108.0}


class TestSpecEdgeCases:
    """Edge cases to consider for future spec updates."""

    def test_rounding_behavior(self):
        """Verify 2 decimal place rounding per spec."""
        response = client.post(
            "/price",
            json={"amount": 19.99, "vat_pct": 8.5, "code": None}
        )
        assert response.status_code == 200
        # 19.99 * 1.085 = 21.68915 -> 21.69
        assert response.json() == {"final": 21.69}

    def test_discount_rounding(self):
        """Verify rounding when discount is applied."""
        response = client.post(
            "/price",
            json={"amount": 50, "vat_pct": 15, "code": "WELCOME10"}
        )
        assert response.status_code == 200
        # 50 * 1.15 = 57.5, * 0.9 = 51.75
        assert response.json() == {"final": 51.75}

