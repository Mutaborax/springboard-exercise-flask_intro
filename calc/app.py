# Put your app in here.
'''
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/add")
def add_view():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return str(f'The addition of {a} and {b} is {result} \n')


@app.route('/sub')
def sub_view():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return str(f'The subtraction of {a} and {b} is {result} \n')


@app.route('/mult')
def mult_view():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return str(f'The multiplication of {a} and {b} is {result} \n')


@app.route('/div')
def div_view():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return str(f'The result of {a} divided by {b} is {result} \n')


if __name__ == "__main__":
    app.run(debug=True)
'''
from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/math/<operation>")
def math_view(operation):
    operations = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mult": lambda a, b: a * b,
        "div": lambda a, b: a // b,  # considering integer division
    }

    if operation not in operations:
        return "<h1>Invalid operation</h1>"

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = operations[operation](a, b)

    return str(f'The result of {a} {operation} {b} is the following {result}\n')


if __name__ == "__main__":
    app.run(debug=True)
