import sqlite3
from flask import Flask
# import the necessary Python module for db

app = Flask(__name__)

class Drink:
    def __init__(self, name, description):
        self.name = name
        self.description = description


@app.route("/")
def index():
    return '<div style="text-align: center; margin: 7.5%;"><h1>Hello, Ya Crazy Muthafuggahz‼️</h1></div>'


@app.route("/drinks")
def get_index():

    return {"drinks": ["water", "soda", "juice"]}
