from flask import Flask, jsonify, request
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
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {"name": drink.name, "description": drink.description}
        output.append(drink_data)
    return {"drinks": output}


@app.route("/drinks/<id>")
def get_single_drink(id):
    drink = Drink.query.get_or_404(id)  # get_or_404 returns 404 if not found()

    return jsonify({"name": drink.name, "description": drink.description})


@app.route("/drinks", methods=["POST"])
def add_drink():
    drink = Drink(name=request.json["name"], description=request.json["description"])
    db.session.add(drink)
    db.session.commit()
    return {"Successfully Added! New Drink ID": drink.id}


@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": f"The Drink with ID {id} was not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"Successfully Totally Yeeted Drink ID": drink.id}
