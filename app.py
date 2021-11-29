from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello_world():
    print("Hello world is running")
    return "<p>Hello, World!</p>"


@app.route("/test")
def testing_function():
    print("Testing function is running")
    return "<p>Fuck You it works!</p>"


@app.route("/checkPrime")
@cross_origin()
def prime():
    x = int(request.args.get('numberToCheck'))
    # print(x)
    # print(type(x))
    for i in range(2, x):
        if x % i == 0:
            return jsonify(answer="False")
    return jsonify(answer="True")
