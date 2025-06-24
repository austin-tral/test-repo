
import unittest
from calculator import Calculator, is_even

class TestCalculator(unittest.TestCase):
    """
    Test cases for the Calculator class.
    This suite tests the functionality of each arithmetic method in the Calculator class.
    """

    def setUp(self):
        """
        Set up a new Calculator instance before each test.
        This ensures that each test is independent and does not share state.
        """
        self.calc = Calculator()

    def test_add(self):
        """
        Test the add method with a variety of inputs.
        - Positive numbers
        - Negative numbers
        - Zero
        """
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtract(self):
        """
        Test the subtract method with different scenarios.
        - Subtracting a smaller number from a larger one
        - Subtracting a larger number from a smaller one
        - Subtracting zero
        """
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test_multiply(self):
        """
        Test the multiply method.
        - Multiplying two positive numbers
        - Multiplying by zero
        - Multiplying by a negative number
        """
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide(self):
        """
        Test the divide method for both normal and edge cases.
        - Standard division
        - Division resulting in a fraction
        - Division by zero, which should raise a ValueError
        """
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

class TestIsEven(unittest.TestCase):
    """
    Test cases for the standalone is_even function.
    This suite ensures that the function correctly identifies even and odd numbers.
    """

    def test_is_even_with_even_numbers(self):
        """
        Test is_even with numbers that are expected to be even.
        - A standard even number
        - Zero, which is considered even
        - A negative even number
        """
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))

    def test_is_even_with_odd_numbers(self):
        """
        Test is_even with numbers that are expected to be odd.
        - A standard odd number
        - A negative odd number
        """
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-5))

if __name__ == '__main__':
    """
    Standard entry point for running the tests.
    This allows the test suite to be executed directly from the command line.
    """
    unittest.main()
