"""This is the Flask app."""

from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
from database import Database

app = Flask(__name__)


database = Database()

@app.route("/")
def home():
    # data = database.get_last_data()
    data = {"temperature": 20.0, "humidity": 75.0, "air_quality": 2, "pressure": 10012.0}
    return render_template(
        "index.html",
        greeting="Bonjour",
        name="Firmin",
        temp_string="Température",
        temp=str(data["temperature"]),
        temp_unit="°C",
        air_quality_string="Qualité de l’air",
        air_quality=str(data["air_quality"]),
        air_quality_unit="/3",
        pressure_string="Pression ambiante",
        pressure=str(data["pressure"]),
        pressure_unit="\xa0bar",
        humidity_string="Taux d'humidité",
        humidity=str(data["humidity"]),
        humidity_unit="%"
    )


KINDS_OF_DATA = {
    'temperature': {
        "name": "température"
    },
    'pressure': {
        "name": "pression"
    },
    'air_quality': {
        "name": "qualité de l’air"
    },
    'humidity': {
        "name": "humidité"
    }
}


@app.route("/archive/")
def get_archived_data():
    data = request.args.get("data")
    if data is None or data not in KINDS_OF_DATA.keys():
        return BadRequest
    else:
        return render_template(
            "archive.html",
            data_name=KINDS_OF_DATA[data]["name"]
        )


@app.route("/add_data/", methods=['POST'])
def add_data():
    dictionary = dict()
    if "temperature" in request.form:
        temperature = request.form["temperature"]
        dictionary["temperature"] = temperature
    if "humidity" in request.form:
        humidity = request.form["humidity"]
        dictionary["humidity"] = humidity
    if "air_quality" in request.form:
        air_quality = request.form["air_quality"] # Qualité de l'air en entier
        dictionary["air_quality"] = air_quality
    if "pressure" in request.form:
        pressure = request.form["pressure"] # Pression en flottant
        dictionary["pressure"] = pressure
    database.add_data(dictionary)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
