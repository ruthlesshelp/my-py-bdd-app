#!/usr/bin/env python3
"""
Simple setup script for my-py-bdd-app.

This script helps beginners set up the project quickly by installing
all necessary dependencies.
"""

import subprocess
import sys


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"📦 {description}...")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - SUCCESS")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Main setup function."""
    print("🚀 Setting up my-py-bdd-app for development...\n")
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: You're not in a virtual environment!")
        print("   It's recommended to create and activate a virtual environment first:")
        print("   python -m venv .venv")
        print("   source .venv/bin/activate  # On macOS/Linux")
        print("   .venv\\Scripts\\activate     # On Windows")
        print("")
        response = input("Continue anyway? (y/N): ").lower()
        if response not in ['y', 'yes']:
            print("Setup cancelled. Please create a virtual environment first.")
            return 1
        print("")
    
    # Install core dependencies
    if not run_command("pip install -r requirements.txt", "Installing core dependencies"):
        return 1
    
    print("")
    
    # Install development dependencies
    if not run_command("pip install -r requirements-dev.txt", "Installing development dependencies"):
        print("⚠️  Core dependencies installed, but development dependencies failed.")
        print("   You can still run tests, but code quality tools may not work.")
        return 1
    
    print("")
    
    # Validate installation
    print("🔍 Validating installation...")
    if run_command("python validate_dependencies.py", "Dependency validation"):
        print("\n🎉 Setup complete! You can now:")
        print("   • Run tests: pytest tests/ -v")
        print("   • Check code quality: flake8 src/ tests/")
        print("   • Format code: black src/ tests/")
        print("   • Sort imports: isort src/ tests/")
        print("   • Run with coverage: pytest tests/ -v --cov=src")
        return 0
    else:
        print("\n❌ Setup validation failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())