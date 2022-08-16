import os
from flask import Flask, make_response, render_template

app = Flask(__name__)
application = app

try:
    color = os.environ['COLOR']
except KeyError:
    color = "white"
    print("Defaulting to white background")

@app.route("/")
def hello_world():
    resp = make_response(render_template('index.html', color=color))
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"

    return resp
