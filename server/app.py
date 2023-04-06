#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    seq = range(parameter)
    x = ""
    for i in seq:
        x = x + str(i)+'\n'
    return x

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation not in ['+', '-', '*', '%', 'div']:
        raise Exception('Invalid operation')
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }

    return str(ops[operation](num1, num2))

if __name__ == '__main__':
    app.run(port=5555, debug=True)
