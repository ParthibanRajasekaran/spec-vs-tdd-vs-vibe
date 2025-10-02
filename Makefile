.PHONY: help install test test-vibe test-tdd test-spec run-vibe run-tdd run-spec coverage clean

help:
	@echo "Available commands:"
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run all tests"
	@echo "  make test-vibe   - Run vibe mode tests only"
	@echo "  make test-tdd    - Run TDD mode tests only"
	@echo "  make test-spec   - Run spec-driven mode tests only"
	@echo "  make run-vibe    - Run vibe mode app (port 8000)"
	@echo "  make run-tdd     - Run TDD mode app (port 8001)"
	@echo "  make run-spec    - Run spec-driven mode app (port 8002)"
	@echo "  make coverage    - Run tests with coverage report"
	@echo "  make clean       - Clean cache files"

install:
	pip install -e .

test:
	pytest -q

test-vibe:
	pytest -q vibe/tests

test-tdd:
	pytest -q tdd/tests

test-spec:
	pytest -q spec_driven/tests

run-vibe:
	uvicorn dev_modes.vibe.app:app --reload --port 8000

run-tdd:
	uvicorn dev_modes.tdd.app:app --reload --port 8001

run-spec:
	uvicorn dev_modes.spec_driven.app:app --reload --port 8002

coverage:
	pytest --cov=src --cov-report=term-missing --cov-report=html

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

