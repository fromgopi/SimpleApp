from flask import Flask, request, abort, render_template, render_template_string
import logging
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('calc/calculator.html')


def mul_numbers(a, b):
    print('Inside Mul func')
    c = a*b
    return c


def div_numbers(a, b):
    print('Inside Mul func')
    c = a / b
    return c


@app.route('/calculator', methods=['POST'])
def cal():
    req_dict = request.form
    print(req_dict)
    a = int(request.form['A'])
    b = int(request.form['B'])
    for key in req_dict:
        if key == 'add':
            res = add_numbers(a,b)
            return render_template('calc/calculator.html', value=res)
        if key == 'sub':
            res = sub_numbers(a,b)
            return render_template('calc/calculator.html', value=res)
        if key == 'mul':
            res = mul_numbers(a, b)
            return render_template('calc/calculator.html', value=res)
        if key == 'div':
            res = div_numbers(a, b)
            return render_template('calc/calculator.html', value=res)

    print(a, b)
    return render_template_string('ok')


def add_numbers(a,b):
    print("Inside add method")
    c = a+b
    return c


def sub_numbers(a,b):
    print("Inside sub method")
    c = b-a
    return c


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
