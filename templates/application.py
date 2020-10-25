from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  #index.html IS BY DEFAULT SEARCHED IN A SUBDIRECTORY CALLED "templates"