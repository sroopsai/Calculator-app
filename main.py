from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)


def take_inputs():
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
    return value1, value2


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/div')
def division():
    try:
        value1, value2 = take_inputs()
        try:
            result = value1 / value2
        except ZeroDivisionError:
            warning_msg = "B's value shouldn't be zero! \n"
            return warning_msg
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        return '%.2f \n' % result


if __name__ == "__main__":
    app.run()
