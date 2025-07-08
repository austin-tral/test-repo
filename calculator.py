class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    Each method is a pure function, making it easy to test.
    """

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """

        Returns the division of two numbers.
        Raises a ValueError if division by zero is attempted.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

def is_even(number):
    """
    A standalone function to check if a number is even.
    Returns True if the number is even, False otherwise.
    """
    return number % 2 == 0

class AdvancedCalculator(Calculator):
    """
    An advanced calculator that extends the basic Calculator with more complex operations.
    """

    def power(self, base, exponent):
        """Returns the base raised to the power of the exponent."""
        return base ** exponent

    def sqrt(self, number):
        """
        Returns the square root of a number.
        Raises a ValueError if the number is negative.
        """
        if number < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return number ** 0.5
