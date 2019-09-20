import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_multiplication(self):
        """Tests multiplication feature.,
        // TODO Support Rational Numbers, fractions. """

        response_data = self.app.get('/mul?A=5&B=3')
        self.assertEqual(b'15 \n', response_data.data)


if __name__ == '__main__':
    unittest.main()
