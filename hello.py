from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
@app.route("/phyo")
def phyo():
    return "Hello My name is Phyo Phyo Ma"
