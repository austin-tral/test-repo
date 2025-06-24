import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMain(unittest.TestCase):

    def test_main_prints_hello_world(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
