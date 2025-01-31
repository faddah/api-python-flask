from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<div style="text-align: center; margin: auto auto;"><h1>Hello, Ya Crazy Muthafuggahz‼️</h1></div>'
