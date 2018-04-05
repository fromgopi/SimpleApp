from flask import Flask, request, abort, render_template, render_template_string
import logging
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en" class="full-height">
    <head>
        <title>Home | TravisCI</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="Social media analytic tool">
        <meta name="author" content="Michal Dyzma">
    </head>
    <body>
        <h1>Home Page</h1>
    </body>
</html>
"""

@app.route('/')
def hello_world():
    return HTML

@app.route('/calc')
def get_calc():
    return render_template('calc/calculator.html')


def mul_numbers(a, b):
    print('Inside Mul func')
    c = a*b
    return c


def div_numbers(a, b):
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
