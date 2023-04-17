"""This is the Flask app."""

from flask import Flask, render_template

app = Flask(__name__)


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
    return ''


if __name__ == "__main__":
    app.run(port=12345)
