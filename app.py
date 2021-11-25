from flask import Flask, render_template, request
from helpers import data_finder
import finnhub
from tabulate import tabulate
from helpers import *
from helpers import display_stock, request_list
#import pandas as pd

# Client setup
finnhub_client = finnhub.Client(api_key="c67jj0qad3iai8rb0ht0")

app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
async def index():
    global stock
    global stocks
    
    if request.method == "POST":

        global stock_table_link
        global html_stock_table_link
        global display_stock

        finnhub_client = finnhub.Client(api_key="c67jj0qad3iai8rb0ht0")
        stock = request.form['stock']
        print(stock)
        data_finder(stock)

        if stock == '':
            return(render_template("index.html"))

        return render_template('index.html', stock=stock)

    return render_template('index.html', stock=stock)

@app.route("/my-list", methods=["GET", "POST"])
async def my_list():
    global stocks
    global display_stock
    if request.method == "POST":
        data_finder(display_stock)
        return render_template('stock_table.html')
    else:
        return render_template("my-list.html", request_list = request_list, display_stock = display_stock, stocks = stocks)


@app.route("/stock_table", methods=["GET"])
async def stock_table():
    return render_template("stock_table.html")


if __name__ == '__main__':
    app.run(debug=True)