from flask import Flask, render_template, request

app: Flask = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')