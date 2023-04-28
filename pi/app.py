"""This is the Flask app."""

from flask import Flask, render_template
from database import Database

app = Flask(__name__)


database = Database()

@app.route("/")
def home():
    return render_template(
        "index.html",
        greeting="Hello",
        name="talented developer",
        temp_string="Température",
        temp="19",
        temp_unit="°C",
        air_quality_string="Qualité de l’air",
        air_quality="0",
        air_quality_unit="/3",
        pressure_string="Pression ambiante",
        pressure="1,01",
        pressure_unit="bar"
    )


@app.route("/add_data/", methods=['POST'])
def add_data():
    dictioniary = dict()
    if "temperature" in request.form:
        temperature = request.form["temperature"]
        dictioniary["temperature"] = temperature
    if "humidity" in request.form:
        humidity = request.form["humidity"]
        dictioniary["humidity"] = humidity
    if "air_quality" in request.form:
        air_quality = request.form["air_quality"] # Qualité de l'air en entier
        dictioniary["air_quality"] = air_quality
    if "pressure" in request.form:
        pressure = request.form["pressure"] # Pression en flottant
        dictioniary["pressure"] = pressure
    database.add_data(dictioniary)


if __name__ == "__main__":
    app.run(port=12345)
