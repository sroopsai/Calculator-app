import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_division(self):
        """Tests page with /div route, testing division feature of the calculator,
        right now only integers are being tested.
        //TODO Support Rational Numbers, floats."""

        response_data = self.app.get('/div?A=5&B=3')
        self.assertEqual(b'1.7 \n', response_data.data)


if __name__ == '__main__':
    unittest.main()
