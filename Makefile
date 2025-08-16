.PHONY: help setup install install-dev test lint format type-check clean build docker-build docker-run version pre-commit

# Default target
help:
	@echo "Available commands:"
	@echo "  setup         Create venv, install project in editable mode, install dependencies, pre-commit hooks, and run tests"
	@echo "  install       Install the package"
	@echo "  install-dev   Install package with development dependencies"
	@echo "  test          Run tests"
	@echo "  lint          Run linting (flake8)"
	@echo "  format        Format code (black + isort)"
	@echo "  type-check    Run type checking (mypy)"
	@echo "  pre-commit    Run pre-commit hooks on all files"
	@echo "  pre-commit-install Install pre-commit hooks"
	@echo "  clean         Clean build artifacts"
	@echo "  build         Build the package"
	@echo "  version       Show current version"
	@echo "  docker-build  Build Docker image"
	@echo "  docker-run    Run Docker container"

# Setup target - Complete project setup
setup:
	@echo "Setting up the project..."
	@echo "1. Creating virtual environment..."
	python3 -m venv venv
	@echo "2. Activating virtual environment and installing project in editable mode with dev dependencies..."
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -e ".[dev]"
	@echo "3. Installing pre-commit hooks..."
	./venv/bin/pre-commit install
	@echo "4. Running unit tests..."
	./venv/bin/pytest
	@echo "Setup complete! Activate the virtual environment with: source venv/bin/activate"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

# Testing
test:
	pytest

test-cov:
	pytest --cov=src --cov-report=html --cov-report=term

# Code quality
lint:
	flake8 src tests

format:
	black src tests
	isort src tests

type-check:
	mypy src

# All quality checks
check: lint type-check test

# Pre-commit hooks
pre-commit-install:
	pre-commit install

pre-commit:
	pre-commit run --all-files

# Cleanup
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Build
build: clean
	python -m build

# Version
version:
	python -c "import template_python_project; print(f'Package version: {template_python_project.__version__}')"

# Docker
docker-build:
	docker build -t template_python_project .

docker-run:
	docker run template_python_project
