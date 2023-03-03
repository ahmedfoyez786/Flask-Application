from flask import Flask

app = Flask(__name__)

@app.route('/cal/<int:num1>/<op>/<int:num2>')
def calculator(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Invalid operator"

    return f"{num1} {op} {num2} = {result}"

if __name__ == '__main__':
    app.run(debug=True)
