from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, World!!!"  #acts as a HTML variable when used in index.html
    return render_template("index.html", headline = headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline = headline)