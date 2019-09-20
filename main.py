from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/div')
def division():
    value1 = request.args.get('A', default=0, type=int)
    value2 = request.args.get('B', default=0, type=int)
    try:
        result = value1/value2
    except ZeroDivisionError:
        return "B's value shouldn't not be zero!"
    else:
        return '%.1f \n' % result


if __name__ == "__main__":
    app.run()
