# My Python BDD Application

This is a Python-based project using Behavior-Driven Development (BDD) with pytest-bdd for testing business logic and related features. It is a beginner-friendly BDD project that offers readable Gherkin scenarios.

## Getting Started

### Using virtual environment venv

Python virtual environments enable you to set up a Python sandbox with its own set of packages separate from the system site-packages in which to work.

#### Create

```bash
python -m venv .venv
```

#### Activate

To activate on macOS and Linux.
```bash
source .venv/bin/activate
```

To activate on Windows.
```bash
.venv\Scripts\activate.bat
```

To activate on Windows with PowerShell.
```bash
.venv\Scripts\Activate.ps
```

#### Deactivate

When done, run:
```bash
deactivate
```

### Using pip to install Python packages

`pip` is the tool used to install Python packages, and it is installed as part of
your Python installation.

Confirm pip version by running:
```bash
pip --version
```

You should see:
```bash
pip 25.2 from /Users/ ... /.venv/lib/python3.11/site-packages/pip (python 3.13)
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
