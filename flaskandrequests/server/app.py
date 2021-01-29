from flask import Flask

app = Flask("demoapp")

@app.route("/")
def home():
    return "home"

@app.route("/sayHi")
def sayHi():
    return "hello"

@app.route("/goodbye")
def bye():
    return "good bye"
