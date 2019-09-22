import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_subtraction(self):
        """Tests page with /sub route, testing subtraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/sub?A=5&B=3')
        self.assertEqual(b'2 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/sub?A=5/3&B=3/4')
        self.assertEqual(b'0.92 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/sub?A=5.4&B=3.4678')
        self.assertEqual(b'1.93 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/sub?A=5&B=-3.4678')
        self.assertEqual(b'8.47 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/sub?A=-3.4678&B=5')
        self.assertEqual(b'-8.47 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/sub?A=3/4&B=5')
        self.assertEqual(b'-4.25 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/sub?A=5&B=3/4')
        self.assertEqual(b'4.25 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response_data = self.app.get('/sub?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be zero! \n", response_data.data)

        # when B = x/0 where x belongs to any integer
        response_data = self.app.get('/sub?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be zero! \n", response_data.data)

        # when A is a non-number type
        response_data = self.app.get('/sub?A=x&B=zingo')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when B is a non-number type
        response_data = self.app.get('/sub?A=1&B=y')
        self.assertEqual(b"B's value should be a number (includes fraction, float, integer). \n", response_data.data)


if __name__ == '__main__':
    unittest.main()
