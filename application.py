from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import the necessary Python module for db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route("/")
def index():
    return '<div style="text-align: center; margin: 7.5%;"><h1>Hello, Ya Crazy Muthafuggahz‼️</h1></div>'


@app.route("/drinks")
def get_index():

    return {"drinks": ["water", "soda", "juice"]}
