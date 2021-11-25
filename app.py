from flask import Flask, render_template, request
from helpers import key_rename, make_table
import finnhub
from tabulate import tabulate
import pandas as pd

request_index = 0
request_index_list = []
last_index = 0


# Client setup
finnhub_client = finnhub.Client(api_key="c67jj0qad3iai8rb0ht0")


app: Flask = Flask(__name__)
stocks: list[str] = []

@app.route("/", methods=["GET", "POST"])
async def index():
    global stocks
    stock: str = ""
    
    if request.method == "POST":
        stock: str = request.form['stock']

        global request_index_list
        global request_index
        global last_index

        if stock == '':
            return(render_template("index.html"))

        finnhub_client = finnhub.Client(api_key="c67jj0qad3iai8rb0ht0")
        data: dict = finnhub_client.quote(stock)
        # print(finnhub_client.quote(stock))
        stocks.append(stock)
        data = key_rename(data)
        print(f"Stocks in My List: {stocks}")
        print(f"Market information for {stocks[-1]}: {data}")
        # table = make_table(data, stocks)
        df = pd.DataFrame(data, index = [0])
        print(df)
        df.to_html('templates/stock_table.html')

        request_index_list.append(request_index)

        last_index = request_index_list[len(request_index_list) - 1]

        request_index += 1

        return render_template('index.html', stock=stock)

    return render_template('index.html', stock=stock)

@app.route("/my-list", methods=["GET", "POST"])
async def my_list():
    if request.method == "POST":
        global stocks

        stock: list[str] = request.form['stock']

        stock_index_list = []

        global i
        i = 0
        while i < len(stocks):
            stock_index_list.append(i)
            i += 1

        if stock == '':
            return render_template("index.html", stocks=stocks)
        
        stocks.append(stock)

        return render_template("index.html", stocks=stocks)

    return render_template("my-list.html", stocks=stocks, last_index = last_index)


@app.route("/stock_table", methods=["GET"])
async def stock_table():
    return render_template("stock_table.html")


if __name__ == '__main__':
    app.run(debug=True)