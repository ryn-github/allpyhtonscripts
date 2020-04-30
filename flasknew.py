from flask import Flask, render_template

app = Flask(__name__,template_folder="c:\\general")

@app.route("/")
def index():
    return render_template("first.html")

@app.route("/second.html")
def func2():
    return render_template("second.html")