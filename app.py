from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("Hello world is running")
    return "<p>Hello, World!</p>"


@app.route("/test")
def testing_function():
    print("Testing function is running")
    return "<p>Fuck You it works!</p>"


@app.route("/checkPrime")
def prime():

    x = 192921
    for i in range(2, x):
        if x % i == 0:
            return "False"
    return "True"
