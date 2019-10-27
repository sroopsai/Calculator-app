from flask import Flask, request, jsonify
from fractions import Fraction

app = Flask(__name__)


def take_inputs():
    if request.method == 'POST':
        value1 = request.values.get('A', default=0, type=str)
    else:
        value1 = request.args.get('A', default=0, type=str)
    try:
        value1 = Fraction(value1)
    except ZeroDivisionError:
        return "A's denominator shouldn't be zero! \n"
    except ValueError:
        return "A's value should be a number (includes fraction, float, integer). \n"
    if request.method == 'GET':
        value2 = request.args.get('B', default=0, type=str)
    else:
        value2 = request.values.get('B', default=0, type=str)
    try:
        value2 = Fraction(value2)
    except ZeroDivisionError:
        return "B's denominator shouldn't be zero! \n"
    except ValueError:
        return "B's value should be a number (includes fraction, float, integer). \n"
    return value1, value2 


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'

@app.route('/add', methods=['POST','GET'])
def addition():
    try:
        value1, value2 = take_inputs()
        result = value1 + value2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.3f \n' % result


@app.route('/sub', methods=['POST', 'GET'])
def subtraction():
    try:
        value1, value2 = take_inputs()
        result = value1 - value2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.3f \n' % result


@app.route('/mul', methods=['POST', 'GET'])
def multiplication():
    try:
        value1, value2 = take_inputs()
        result = value1 * value2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.3f \n' % result


@app.route('/div', methods=['POST', 'GET'])
def division():
    try:
        value1, value2 = take_inputs()
        try:
            result = ((value1)/(value2))
        except ZeroDivisionError:
            warning_msg = "B's value shouldn't be zero! \n"
            return warning_msg
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.3f \n' % result


if __name__ == "__main __":
    app.run()
