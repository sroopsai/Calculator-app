import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_empty_page(self):
        """Tests page with empty route or no route"""

        response_data = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response_data.data)

    def test_addition(self):
        """Tests page with /add route, testing addition feature of the calculator,
        right now only integers are being tested."""

        response_data = self.app.get('/add?A=5&B=3')
        self.assertEqual(b'8 \n', response_data.data)


if __name__ == '__main__':
    unittest.main()