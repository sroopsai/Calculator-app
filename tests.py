import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""

        main.app.testing = True
        self.app = main.app.test_client()

    def test_subtraction(self):
        """Tests the subtraction feature -> applies to only integers right now."""

        response_data = self.app.get('/sub?A=5&B=5')
        self.assertEqual(b'0 \n', response_data.data)


if __name__ == '__main__':
    unittest.main()