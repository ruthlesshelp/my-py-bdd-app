"""Common step definitions for BDD testing."""

import pytest
from pytest_bdd import given, parsers, then, when

from src.class_one import Class1


@pytest.fixture
@given("I have a Class1 object")
def class1_object():
    """Create a Class1 object for testing."""
    return Class1()


@when(parsers.parse("I call Function1 with value {value:d}"))
def call_function1(class1_object, value):
    """Call Function1 with the given value."""
    class1_object.function_1(value)


@when("I call Function2")
def call_function2(class1_object):
    """Call Function2 and store the result or exception."""
    try:
        class1_object._test_result = class1_object.function_2()
        class1_object._test_exception = None
    except Exception as e:
        class1_object._test_exception = e
        class1_object._test_result = None


@then("a ValueError should be raised")
def check_valueerror_raised(class1_object):
    """Verify that a ValueError was raised."""
    assert class1_object._test_exception is not None
    assert isinstance(class1_object._test_exception, ValueError)


@then("a RuntimeError should be raised")
def check_runtimeerror_raised(class1_object):
    """Verify that a RuntimeError was raised."""
    assert class1_object._test_exception is not None
    assert isinstance(class1_object._test_exception, RuntimeError)


@then(parsers.parse('the message should contain "{message}"'))
def check_error_message(class1_object, message):
    """Verify that the error message contains the expected text."""
    assert class1_object._test_exception is not None
    assert message in str(class1_object._test_exception)


@then("the output array should contain:")
def check_output_array(class1_object, datatable):
    """Verify that the output array contains the expected data."""
    assert class1_object._test_exception is None
    assert class1_object._test_result is not None

    # Parse the expected data from the datatable
    # First row is header, so skip it
    expected_coefficients = []
    expected_values = []

    for row in datatable[1:]:  # Skip header row
        expected_coefficients.append(int(row[0]))  # Coefficient column
        expected_values.append(int(row[1]))  # Value column

    # Build expected flat array format: [coeff1, value1, coeff2, value2, ...]
    expected_flat_array = []
    for i in range(len(expected_coefficients)):
        expected_flat_array.append(expected_coefficients[i])
        expected_flat_array.append(expected_values[i])

    # Compare the actual result with expected flat array
    actual_result = class1_object._test_result
    assert len(actual_result) == len(
        expected_flat_array
    ), f"Expected length {len(expected_flat_array)}, got {len(actual_result)}"
    assert (
        actual_result == expected_flat_array
    ), f"Expected {expected_flat_array}, got {actual_result}"

    # Also verify the coefficient-value pairs are correct
    for i in range(0, len(actual_result), 2):
        coeff_index = i // 2
        assert actual_result[i] == expected_coefficients[coeff_index]  # Coefficient
        assert actual_result[i + 1] == expected_values[coeff_index]  # Value
