# GitHub Copilot Instructions for this BDD project

## Project Overview

This is a beginner-friendly Python-based project using Behavior-Driven Development (BDD) with pytest-bdd for testing business logic and related features. The project emphasizes simplicity and uses a requirements.txt approach for dependency management.

## Project Structure

The project follows a clean BDD architecture with strict separation of concerns:

```
├── src/                          # Source code
│   ├── __init__.py
│   └── class_one.py              # Class1 with function_1 and function_2 methods
├── features/                     # BDD feature files (Gherkin scenarios)
│   └── Class1DataProcessing.feature
├── tests/                        # Test implementation
│   ├── step_definitions/         # Reusable BDD step definitions
│   │   ├── __init__.py
│   │   └── common_steps.py       # Shared step implementations
│   ├── test_*_bdd.py             # BDD test files linking scenarios
│   └── __init__.py
├── requirements.txt              # Core runtime dependencies
├── requirements-dev.txt          # Development dependencies
├── Makefile                      # Development commands and workflows
├── setup.py                      # Automated setup script for beginners
├── validate_dependencies.py     # Dependency validation script
├── .gitignore                    # Git ignore patterns
└── README.md                     # Project documentation
```

**Important**: This project uses ONLY BDD testing patterns. Traditional unit test files (`test_*.py` without `_bdd` suffix) should be avoided or removed if empty.

## Current Implementation

### Business Logic
- **Class1** in `src/class_one.py` with methods:
  - `function_1(value: int)` - Stores input value for processing
  - `function_2() -> List[int]` - Processes value and returns structured output array
  - Follows PEP 8 naming conventions (snake_case)

### Feature Coverage
- **Class1DataProcessing.feature** contains three scenarios:
  1. Handle invalid negative input (raises ValueError)
  2. Handle calling Function2 before Function1 (raises RuntimeError)
  3. Process input zero (returns array with coefficients and values)

### Gherkin vs Python Naming
- **Gherkin steps** use business language: "Function1", "Function2"
- **Python methods** use technical conventions: `function_1`, `function_2`
- **Step definitions** bridge the gap between business and technical language

## Tools and Dependencies

### Core Dependencies (requirements.txt)
- `pytest>=7.0.0` - Testing framework
- `pytest-bdd>=7.0.0` - BDD extension for pytest that parses Gherkin feature files

### Development Dependencies (requirements-dev.txt)
- `pytest-cov>=4.0.0` - Code coverage plugin for pytest
- `coverage[toml]>=7.0.0` - Coverage measurement with TOML support
- `flake8>=6.0.0` - Code linting and PEP 8 compliance
- `black>=23.0.0` - Code formatting
- `isort>=5.12.0` - Import sorting

### Python Version Support
- Python 3.8+ for modern language features
- Tested primarily on Python 3.13.2

## Development Workflow

### Installation and Setup
1. **Using Makefile (Recommended)**:
   ```bash
   make install  # Install all dependencies and validate setup
   make test     # Run tests with coverage
   ```

2. **Quick Setup**:
   ```bash
   python setup.py
   ```

3. **Manual Setup**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   python validate_dependencies.py
   ```

### Makefile Commands
The project includes a simplified Makefile for essential development tasks:
```bash
make help        # Show all available commands
make install     # Install all dependencies and validate setup
make lint        # Check code style and format code automatically
make test        # Run BDD tests with coverage report
make clean       # Clean up generated files
make all         # Complete workflow: install, lint, test
```

### Setup Script
A `setup.py` script is provided for beginners to automate the setup process:
```bash
python setup.py
```

### Dependency Validation
A `validate_dependencies.py` script checks for missing or extra packages:
```bash
python validate_dependencies.py
```

### Running Tests
```bash
# Run all BDD tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

# Validate dependencies
python validate_dependencies.py
```

### Code Quality Checks
```bash
# Check PEP 8 compliance
flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503,F403,F401

# Format code
black src/ tests/

# Sort imports
isort src/ tests/
```

## Code Coverage

The project aims for high code coverage using `pytest-cov`:
- All business logic in the `src/` directory should be tested
- Coverage includes both statement and branch coverage
- HTML coverage reports are generated in the `htmlcov/` directory
- Terminal coverage reports show complete coverage status

Current coverage: ~93% (missing only edge cases not covered by BDD scenarios)

## BDD Testing Patterns

### Step Definition Structure
Use `@given`, `@when`, `@then` decorators from pytest-bdd for step definitions. Place reusable step definitions in `tests/step_definitions/common_steps.py`.

### Data Extraction
For step definitions that extract data from Gherkin steps, use `parsers.parse()` with placeholders:
- `{value:d}` for integers
- `{rate:f}` for floats
- `{message}` for strings

### Fixture Pattern
```python
@pytest.fixture
@given("I have a Class1 object")
def class1_object():
    """Create a Class1 object for testing."""
    return Class1()
```

### Method Calls
Step definitions should call the Python methods (snake_case) while Gherkin uses business language:
```python
@when(parsers.parse("I call Function1 with value {value:d}"))
def call_function1(class1_object, value):
    """Call Function1 with the given value."""
    class1_object.function_1(value)  # Note: snake_case in Python
```

### Error Handling in Tests
Store both results and exceptions in test objects:
```python
try:
    class1_object._test_result = class1_object.function_2()
    class1_object._test_exception = None
except Exception as e:
    class1_object._test_exception = e
    class1_object._test_result = None
```

## Exception Handling

Use `ValueError` built-in exception when an operation or function receives an argument that has the correct type but is an inappropriate or invalid value.

Use `RuntimeError` for business rule violations or calculations that cannot be performed with the given parameters.

Use `NotImplementedError` for unimplemented features or functionality.

## Coding Standards

### PEP 8 Compliance
- **Function names**: Use snake_case (e.g., `function_1`, `function_2`)
- **Class names**: Use PascalCase (e.g., `Class1`)
- **Constants**: Use UPPER_CASE
- **Line length**: Maximum 88 characters (Black standard)

### Import Organization
- Standard library imports first
- Third-party imports second
- Local application imports last
- Blank line between each group

### Code Quality Tools Configuration
- **Flake8**: `--max-line-length=88 --extend-ignore=E203,W503,F403,F401`
- **Black**: Default configuration (88 character line length)
- **iSort**: Profile "black" for compatibility

## Testing Conventions

**Important**: This project exclusively uses BDD testing. Do not create traditional unit test files (`test_*.py`). All testing should go through the BDD workflow with feature files and corresponding `test_*_bdd.py` files.

### BDD Test File Structure
```python
"""BDD tests for Class1 data processing functionality."""

from pytest_bdd import scenarios

# Import all step definitions
from tests.step_definitions.common_steps import *

# Load all scenarios from the feature file
scenarios("../features/Class1DataProcessing.feature")
```

Note: The wildcard import `from tests.step_definitions.common_steps import *` is acceptable and expected in BDD test files.

## Code Organization

### Business Logic Separation
Keep business logic separate from test code:
- **Business logic**: `src/` directory
- **Test scenarios**: `features/` directory (Gherkin)
- **Test implementation**: `tests/` directory (Python)

### Step Definition Bridge
Step definitions should act as a bridge between Gherkin scenarios and business logic, handling:
- Data conversion between business language and technical implementation
- Context management between steps
- Exception handling and result storage

## Project Maintenance

### When Adding New Functionality
1. **Define scenarios** in `.feature` files under `features/`
2. **Implement step definitions** in `tests/step_definitions/common_steps.py`
3. **Create BDD tests** as `tests/test_*_bdd.py` files
4. **Implement business logic** in appropriate `src/` modules
5. **Run tests** to ensure all scenarios pass
6. **Check code quality** with flake8, black, and isort
7. **Validate coverage** to maintain high test coverage

### Dependency Management
- **Adding runtime dependencies**: Add to `requirements.txt`
- **Adding development dependencies**: Add to `requirements-dev.txt`
- **Installation**: Use `python setup.py` for beginners or manual pip commands
- **Validation**: Run `python validate_dependencies.py` after changes

### Git Workflow
The project includes a comprehensive `.gitignore` file that excludes:
- Python bytecode and cache files (`__pycache__/`, `*.pyc`)
- Virtual environments (`.venv/`, `venv/`)
- IDE-specific files (VS Code, PyCharm)
- OS-specific files (macOS `.DS_Store`, Windows `Thumbs.db`)
- Testing artifacts (`.pytest_cache/`, coverage reports)
- Package build artifacts (`dist/`, `build/`, `*.egg-info/`)

## Troubleshooting

### Common Issues
1. **Import errors**: Run `python validate_dependencies.py` to check dependencies
2. **Test failures**: Ensure virtual environment is activated and dependencies installed
3. **Code quality issues**: Run black and isort before committing
4. **Coverage gaps**: Review missing lines in coverage report

### Debug Commands
```bash
# Check Python environment
python --version
which python

# List installed packages
pip list

# Run specific test
pytest tests/test_class1_bdd.py::test_handle_invalid_negative_input -v

# Debug coverage
pytest tests/ --cov=src --cov-report=html
# Then open htmlcov/index.html in browser
```
