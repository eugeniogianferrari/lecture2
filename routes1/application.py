from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/<string:name>")  #generalization of the routes in routes0
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"  #basic usage of HTML in this Flask apps