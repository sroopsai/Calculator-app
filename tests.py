import unittest
import main



class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""

        main.app.testing = True
        self.app = main.app.test_client() 

    def test_empty_page(self):
        response_data = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response_data.data)

        # Testing POST Method
        response_data = self.app.post('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response_data.data)

    def test_addition(self):
        # integer numbers testing
        response_data = self.app.get('/add?A=5&B=3')
        self.assertEqual(b'8 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/add?A=5/3&B=3/4')
        self.assertEqual(b'2.417 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/add?A=5.4&B=3.4678')
        self.assertEqual(b'8.868 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/add?A=5&B=-3.4678')
        self.assertEqual(b'1.532 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/add?A=-3.4678&B=5')
        self.assertEqual(b'1.532 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/add?A=3/4&B=5')
        self.assertEqual(b'5.750 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/add?A=5&B=3/4')
        self.assertEqual(b'5.750 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response_data = self.app.get('/add?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be zero! \n", response_data.data)

        # when B = x/0 where x belongs to any integer
        response_data = self.app.get('/add?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be zero! \n", response_data.data)

        # when A is a non-number type
        response_data = self.app.get('/add?A=x&B=zingo')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when B is a non-number type
        response_data = self.app.get('/add?A=1&B=y')
        self.assertEqual(b"B's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # Handling of POST Method 
        response_data = self.app.post('/add',data=dict(A='1',B='2'))
        self.assertEqual(b'3 \n',response_data.data)

    def test_subtraction(self):
        """Tests page with /sub route, testing subtraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/sub?A=5&B=3')
        self.assertEqual(b'2 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/sub?A=5/3&B=3/4')
        self.assertEqual(b'0.917 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/sub?A=5.4&B=3.4678')
        self.assertEqual(b'1.932 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/sub?A=5&B=-3.4678')
        self.assertEqual(b'8.468 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/sub?A=-3.4678&B=5')
        self.assertEqual(b'-8.468 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/sub?A=3/4&B=5')
        self.assertEqual(b'-4.250 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/sub?A=5&B=3/4')
        self.assertEqual(b'4.250 \n', response_data.data)

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

        # Handling of POST Method
        response_data = self.app.post('/sub',data=dict(A='1', B='2'))
        self.assertEqual(b'-1 \n', response_data.data)

    def test_multiplication(self) :
        """Tests page with /mul route, testing multiplication feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/mul?A=5&B=3')
        self.assertEqual(b'15 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/mul?A=5/3&B=3/4')
        self.assertEqual(b'1.250 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/mul?A=5.4&B=3.4678')
        self.assertEqual(b'18.726 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/mul?A=5&B=-3.4678')
        self.assertEqual(b'-17.339 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/mul?A=-3.4678&B=5')
        self.assertEqual(b'-17.339 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/mul?A=3/4&B=5')
        self.assertEqual(b'3.750 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/mul?A=5&B=3/4')
        self.assertEqual(b'3.750 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response_data = self.app.get('/mul?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be zero! \n", response_data.data)

        # when B = x/0 where x belongs to any integer
        response_data = self.app.get('/mul?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be zero! \n", response_data.data)

        # when A is a non-number type
        response_data = self.app.get('/mul?A=x&B=zingo')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when B is a non-number type
        response_data = self.app.get('/mul?A=1&B=y')
        self.assertEqual(b"B's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # Handling of POST method
        response_data = self.app.post('/mul', data=dict(A='1',B='y'))
        self.assertEqual(b"B's value should be a number (includes fraction, float, integer). \n", response_data.data)

    def test_division(self):
        # printing integral value correctly
        response_data = self.app.get('/div?A=4&B=2')
        self.assertEqual(b'2 \n', response_data.data)

        # integer numbers testing
        response_data = self.app.get('/div?A=5&B=3')
        self.assertEqual(b'1.667 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/div?A=5/3&B=3/4')
        self.assertEqual(b'2.222 \n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/div?A=5.4&B=3.4678')
        self.assertEqual(b'1.557 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/div?A=5&B=-3.4678')
        self.assertEqual(b'-1.442 \n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/div?A=-3.4678&B=5')
        self.assertEqual(b'-0.694 \n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/div?A=3/4&B=5')
        self.assertEqual(b'0.150 \n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/div?A=5&B=3/4')
        self.assertEqual(b'6.667 \n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response_data = self.app.get('/div?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be zero! \n", response_data.data)

        # when B = x/0 where x belongs to any integer
        response_data = self.app.get('/div?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be zero! \n", response_data.data)

        # when A is a non-number type
        response_data = self.app.get('/div?A=x&B=zingo')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when B is a non-number type
        response_data = self.app.get('/div?A=1&B=y')
        self.assertEqual(b"B's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # Extra case when B is zero
        response_data = self.app.get('/div?A=1&B=0')
        self.assertEqual(b"B's value shouldn't be zero! \n", response_data.data)

        # Handling of POST Method
        response_data = self.app.post('/div', data=dict(A='1', B='0'))
        self.assertEqual(b"B's value shouldn't be zero! \n", response_data.data)

if __name__ == '__main__':
    unittest.main()
