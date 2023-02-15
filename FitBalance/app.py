from flask import Flask, flash, redirect, render_template, request, session
import requests

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True




# App Route
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/macros", methods=["GET"])
def macros():
    return render_template("macros.html")

@app.route("/BMI")
def bmi():
    return render_template("BMI.html")


@app.route("/bf" )
def bf():
    return render_template("bf.html")


@app.route("/calories", methods=["GET", "POST"])
def calories():
    if request.method == "GET":
        return render_template("calories.html")

@app.route("/search", methods=["GET"])
def search():
    if request.method == "GET":
        return redirect("/calories")
