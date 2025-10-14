#!/usr/bin/env python3
"""
Dependency validation script for my-py-bdd-app.

This script validates that all required dependencies from requirements.txt 
and requirements-dev.txt are properly installed and accessible.
"""

import sys
from importlib import import_module


def check_dependency(module_name, package_name=None):
    """Check if a dependency is installed and importable."""
    try:
        import_module(module_name)
        print(f"✅ {package_name or module_name} - OK")
        return True
    except ImportError:
        print(f"❌ {package_name or module_name} - MISSING")
        return False


def main():
    """Validate all dependencies."""
    print("🔍 Checking dependencies for my-py-bdd-app...\n")
    
    # Core runtime dependencies
    print("📦 Core Dependencies:")
    core_deps = [
        ("pytest", "pytest"),
        ("pytest_bdd", "pytest-bdd"),
    ]
    
    core_ok = all(check_dependency(mod, pkg) for mod, pkg in core_deps)
    
    # Development dependencies
    print("\n🛠  Development Dependencies:")
    dev_deps = [
        ("pytest_cov", "pytest-cov"),
        ("coverage", "coverage"),
        ("flake8", "flake8"),
        ("black", "black"),
        ("isort", "isort"),
    ]
    
    dev_ok = all(check_dependency(mod, pkg) for mod, pkg in dev_deps)
    
    # Summary
    print("\n" + "="*50)
    if core_ok and dev_ok:
        print("🎉 All dependencies are properly installed!")
        return 0
    elif core_ok:
        print("⚠️  Core dependencies OK, but some dev dependencies missing.")
        print("   Install with: pip install -r requirements-dev.txt")
        return 1
    else:
        print("❌ Missing core dependencies!")
        print("   Install with: pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())