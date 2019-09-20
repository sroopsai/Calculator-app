from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1 = request.args.get('A', default=0, type=str)
    try:
        value1 = Fraction(value1)
    except ZeroDivisionError:
        return "A's denominator shouldn't be zero! \n"
    except ValueError:
        return "A's value should be a number (includes fraction, float, integer). \n"
    value2 = request.args.get('B', default=0, type=str)
    try:
        value2 = Fraction(value2)
    except ZeroDivisionError:
        return "B's denominator shouldn't be zero! \n"
    except ValueError:
        return "B's value should be a number (includes fraction, float, integer). \n"
    result = value1+value2
    return '%.1f \n' % result


if __name__ == "__main__":
    app.run()
