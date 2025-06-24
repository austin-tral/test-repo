
import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    """
    Test cases for the main function.
    This suite ensures that the main function executes without errors and
    produces the expected output.
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        """
        Test the main function's output to ensure it runs as expected.
        This test captures the standard output and verifies that it contains
        the expected introductory message.
        """
        main()
        # We are just checking if the main function runs without error
        # and produces some output.
        self.assertIn("--- Using the Calculator Class ---", mock_stdout.getvalue())

if __name__ == '__main__':
    """
    Standard entry point for running the tests.
    This allows the test suite to be executed directly from the command line.
    """
    unittest.main()
