"""This is the Flask app."""

from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
from database import Database
from configparser import ConfigParser
from yaml import safe_load
import os


app = Flask(__name__)


database = Database()

config = ConfigParser()
print(config.read("config.ini"))

kinds_of_data = config["data"]["kinds"].split(',')
units = config["data"]["units"].split(',')
value_classes = config["data"]["value_classes"].split(',')

fr_file = open(os.path.join("langs","fr.yaml"), 'r', encoding="utf-8")
en_file = open(os.path.join("langs", "en.yaml"), 'r', encoding="utf-8")
es_file = open(os.path.join("langs", "es.yaml"), 'r', encoding="utf-8")
it_file = open(os.path.join("langs", "it.yaml"), 'r', encoding="utf-8")


try:
    with open(os.path.join("langs", "fr.yaml"), 'r', encoding="utf-8") as f:
        print(safe_load(f))

    langs = {
        "fr": safe_load(fr_file),
        "en": safe_load(en_file),
        "es": safe_load(es_file),
        "it": safe_load(it_file)
    }
finally:
    fr_file.close()
    en_file.close()
    es_file.close()
    it_file.close()

DATA_SPEC = []

for i, el in enumerate(kinds_of_data):
    DATA_SPEC.append({
        "name": el,
        "title": None,
        "unit": units[i].replace('Â°', '°'),
        "value": None,
        "value_class": value_classes[i]
    })


print(DATA_SPEC)


@app.route("/")
def home():
    global DATA_SPEC
    lang = request.accept_languages.best_match(langs.keys())
    if lang is None:
        lang = "en"
    data = database.get_last_data()
    for k in range(len(DATA_SPEC)):
        # print(data_spec[k])
        # print(data_spec[k]["value"])
        DATA_SPEC[k]["title"] = langs[lang][DATA_SPEC[k]["name"] + "-string"]
        DATA_SPEC[k]["value"] = data[DATA_SPEC[k]["name"]]
    print(DATA_SPEC)
    return render_template(
        "index.html",
        lang=lang,
        title=langs[lang]["app-name"].capitalize(),
        greeting=langs[lang]["greeting-morning"].capitalize(),
        name=config["user"]["name"],
        data_spec=DATA_SPEC
    )



@app.route("/archive/")
def get_archived_data():
    global DATA_SPEC
    lang = request.accept_languages.best_match(langs.keys())
    if lang is None:
        print('defaulting to english')
        lang = "en"
    data = request.args.get("data")
    if data not in [d["name"] for d in DATA_SPEC]:
        return BadRequest
    return render_template(
        "archive.html",
        data_name=langs[lang][f"{data}-string"],
        data_title=data
    )


@app.route("/archive_script.js")
def archive_script():
    data = request.args.get("data")
    print(data)
    if data not in [d["name"] for d in DATA_SPEC]:
        print('bad request')
        return "nope", 403
    all_data = database.get_all_datas(data)
    return render_template(
        "archive_script.js",
        chart_data=all_data
    )


@app.route("/add_data/", methods=['POST'])
def add_data():
    dictionary = dict()
    if "temperature" in request.json.keys():
        temperature = float(request.json["temperature"])
        temperature = round(temperature, 1)
        dictionary["temperature"] = temperature
    if "humidity" in request.json.keys():
        humidity = float(request.json["humidity"])
        humidity = round(humidity, 1)
        dictionary["humidity"] = humidity
    if "air_quality" in request.json.keys():
        air_quality = int(request.json["air_quality"])  # Qualité de l'air en entier

        dictionary["air_quality"] = air_quality
    if "pressure" in request.json.keys():
        pressure = int(request.json["pressure"])  # Pression en flottant
        dictionary["pressure"] = pressure
    database.add_data(dictionary)
    return 'OK', 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7657)
