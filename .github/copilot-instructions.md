# GitHub Copilot Instructions for this BDD project

## Project Overview

This is a Python-based project using Behavior-Driven Development (BDD) with pytest-bdd for testing business logic and related features.

## Project Structure

The project follows a clean BDD architecture with strict separation of concerns:
- `src/` - Contains the main business logic (`class_1.py`)
- `features/` - Gherkin feature files defining business scenarios (top-level directory)
- `tests/step_definitions/` - Python step implementations for BDD scenarios
- `tests/test_*_bdd.py` - BDD test files that link scenarios to step definitions
- `.gitignore` - Comprehensive ignore patterns for Python, IDE, and OS-specific files

Note: This project uses ONLY BDD testing patterns. Traditional unit test files (`test_*.py` without `_bdd` suffix) should be avoided or removed if empty.

## Tools and Dependencies

This project uses pytest-bdd for behavior-driven development testing. Key dependencies include:
- `pytest` - Testing framework
- `pytest-bdd` - BDD extension for pytest that parses Gherkin feature files
- `pytest-cov` - Code coverage plugin for pytest to measure test coverage
- Python 3.8+ for modern language features

## Code Coverage

The project should eventually achieve 100% code coverage using `pytest-cov`:
- All business logic in the `src/` directory is fully tested
- Coverage includes both statement and branch coverage
- HTML coverage reports are generated in the `htmlcov/` directory
- XML coverage reports are generated as `coverage.xml`
- Terminal coverage reports show complete coverage status

To run tests with coverage:
```bash
pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
```

Coverage analysis tools:
- Run `python analyze_coverage.py` for detailed coverage analysis
- View HTML report: `htmlcov/index.html`

## BDD Testing Patterns

When working with BDD tests, follow these patterns:

Use `@given`, `@when`, `@then` decorators from pytest-bdd for step definitions. Place reusable step definitions in `tests/step_definitions/common_steps.py`.

For step definitions that extract data from Gherkin steps, use `parsers.parse()` with placeholders like `{amount:d}` for integers and `{rate:f}` for floats.

BDD test files should import step definitions and use `scenarios('../features/filename.feature')` to load feature files from the top-level features directory. The wildcard import `from tests.step_definitions.common_steps import *` is acceptable and expected in BDD test files.

## Exception Handling

Use `ValueError` built-in exception when an operation or function receives an argument that has the correct type but is an inappropriate or invalid value.

Use `RuntimeError` for business rule violations or calculations that cannot be performed with the given parameters.

Use `NotImplementedError` for unimplemented features or functionality.

## Testing Conventions

**Important**: This project exclusively uses BDD testing. Do not create traditional unit test files (`test_*.py`). All testing should go through the BDD workflow with feature files and corresponding `test_*_bdd.py` files.

## Code Organization

Keep business logic separate from test code.

Step definitions should act as a bridge between Gherkin scenarios and business logic, handling data conversion and context management between steps.

## Project Maintenance

The project includes a comprehensive `.gitignore` file that excludes:
- Python bytecode and cache files (`__pycache__/`, `*.pyc`)
- Virtual environments (`.venv/`, `venv/`)
- IDE-specific files (VS Code, PyCharm)
- OS-specific files (macOS `.DS_Store`, Windows `Thumbs.db`)
- Testing artifacts (`.pytest_cache/`, coverage reports)

When adding new functionality, ensure:
1. Scenarios are defined in `.feature` files under `features/`
2. Step definitions are implemented in `tests/step_definitions/common_steps.py`
3. BDD tests are created as `tests/test_*_bdd.py` files
4. Empty or unused test files are removed to keep the project clean
5. All new code paths are tested to maintain 100% coverage