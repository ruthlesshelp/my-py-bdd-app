# Makefile for My Python BDD Application
# Simplified commands for common development tasks

.PHONY: help install lint test clean

# Default target
help:
	@echo "Available commands:"
	@echo "  make install     - Install all dependencies and validate setup"
	@echo "  make lint        - Check and fix code style (flake8, black, isort)"
	@echo "  make test        - Run tests with coverage report"
	@echo "  make clean       - Clean up generated files"
	@echo "  make all         - Complete workflow (install, lint, test)"

# Install dependencies and validate setup
install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements-dev.txt
	@echo "🔍 Validating installation..."
	python validate_dependencies.py
	@echo "✅ Setup complete!"

# Code quality: lint and auto-fix
lint:
	@echo "🔍 Checking code style..."
	flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503,F403,F401
	@echo "🎨 Formatting code..."
	black src/ tests/
	isort src/ tests/
	@echo "✅ Code style checks and formatting completed!"

# Run tests with coverage
test:
	@echo "🧪 Running tests with coverage..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
	@echo "✅ Tests completed!"
	@echo "📊 Coverage report available at htmlcov/index.html"

# Clean up generated files
clean:
	@echo "🧹 Cleaning up..."
	rm -rf .pytest_cache/ htmlcov/ .coverage __pycache__/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "✅ Cleanup completed!"

# Complete development workflow
all: install lint test
	@echo "🎉 Complete workflow finished successfully!"