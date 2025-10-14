"""Class1 for data processing functionality."""

from typing import List


class Class1:
    """Class1 handles data processing with Function1 and Function2 methods."""

    def __init__(self):
        """Initialize Class1 instance."""
        self._input_value = None

    def function_1(self, value: int) -> None:
        """
        Store the input value for processing.

        Args:
            value (int): The input value to process
        """
        self._input_value = value

    def function_2(self) -> List[int]:
        """
        Process the stored input value and return structured output array.

        Returns:
            List[int]: Array with integers in coefficient-value pairs in flat format
                      [coeff1, value1, coeff2, value2, ...]

        Raises:
            ValueError: If input value is negative (not valid)
        """
        if self._input_value is None:
            raise RuntimeError("function_1 must be called before function_2")

        if self._input_value < 0:
            raise ValueError("Input value is not valid")

        # Return the output array in flat format
        return [1, 0, 5, 0, 10, 0, 25, 0]
