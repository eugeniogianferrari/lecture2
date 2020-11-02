from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods = ["GET","POST"])
def index():
    if session.get("notes") is None:                    
        session["notes"] = []                           #create a "session" that lets differents users' data be independent from one another

    if request.method == "POST":                        #if the user adds a new note
        note = request.form.get("note")
        session["notes"].append(note)                   #add the new note
    
    return render_template("index.html", notes = session["notes"])