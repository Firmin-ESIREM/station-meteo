"""This is the Flask app."""

from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
from database import Database

app = Flask(__name__)


database = Database()

@app.route("/")
def home():
    return render_template(
        "index.html",
        greeting="Bonjour",
        name="Firmin",
        temp_string="Température",
        temp="19,2",
        temp_unit="°C",
        air_quality_string="Qualité de l’air",
        air_quality="0",
        air_quality_unit="/3",
        pressure_string="Pression ambiante",
        pressure="1,01",
        pressure_unit="\xa0bar"
    )


KINDS_OF_DATA = {
    'temperature': {
        "name": "Température"
    },
    'pressure': {
        "name": "Pression"
    },
    'air_quality': {
        "name": "Qualité de l’air"
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
    dictioniary = dict()
    if "temperature" in request.form:
        temperature = request.form["temperature"]
        dictioniary["temperature"] = temperature
    if "humidity" in request.form:
        humidity = request.form["humidity"]
        dictioniary["humidity"] = humidity
    if "air_quality" in request.form:
        air_quality = request.form["air_quality"]
        dictioniary["air_quality"] = air_quality
    if "pressure" in request.form:
        pressure = request.form["pressure"]
        dictioniary["pressure"] = pressure
    database.add_data()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12345)
