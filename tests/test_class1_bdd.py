"""BDD tests for Class1 data processing functionality."""

from pytest_bdd import scenarios

# Import all step definitions
from tests.step_definitions.common_steps import *  # noqa: F403,F401

# Load all scenarios from the feature file
scenarios("../features/Class1DataProcessing.feature")
