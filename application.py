from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<div style="text-align: center; margin: 7.5%;"><h1>Hello, Ya Crazy Muthafuggahz‼️</h1></div>'


@app.route("/drinks")
def get_index():

    return {"drinks": ["water", "soda", "juice"]}
