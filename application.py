from flask import Flask         # import Flask() from flask module

app = Flask(__name__)           # creating a web application with Flask; __name__ represents this code, which is the web application itself

@app.route("/")                 # "routes" are the parts of an URL that define where the web page is; "/" represents the default route, the first to open when we enter in this web app 
def index():                    # when I go to "/" (default page) this function is executed 
    return "Hello, World!!!"       