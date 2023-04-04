"""This is the Flask app."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_data/", methods=['POST'])
def add_data():
    return ''


if __name__ == "__main__":
    app.run(port=12345)
