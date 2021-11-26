"""Generates tables of data for each stock in My List."""
 
 
from pandas.core.frame import DataFrame
from tabulate import tabulate
import finnhub
import pandas as pd
from werkzeug.wrappers import request

# Reassign the data's keys to be the full names for the table's column names
key_list: list[str] = ['current_price', 'change', 'percent_change', 'high_day_price', 'low_day_price', 'open_day_price', 'previous_close_price']
test_data = {'c':1, 'd':2, 'dp':3, 'h':4, 'l':5, 'o':6, 'pc': 7}
 


request_index = 0
request_index_list = []
last_index = 0
stock_table_link = ''
html_stock_table_link = ''
display_stock = ''
stock = ''
stocks: list[str] = []
request_data = pd.DataFrame()


finnhub_client = finnhub.Client(api_key="c67jj0qad3iai8rb0ht0")



def key_rename(input_data: dict) -> dict:
    """Reassign the data's keys to be the full names for the table's column names"""
    key_list: list[str] = ["Current Price", "Change", "% Change", "High", "Low", "Open", "Close"]
    i = 0
    result = {}
    for key in input_data:
        if i > 6:
            break
        else:
            result[key_list[i]] = input_data[key]
            i += 1
    input_data = result
    return input_data


def make_table(input_data: dict, stocks: list[str]) -> str:
    renamed_data = key_rename(input_data, key_list)
    # fake_data: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    print(input_data)
    table = tabulate(input_data, stocks, "html")
    print(f"The dict is: {table}")
    return table


class Request():
    stock: str
    request_index: int
    request_data: DataFrame

    def __init__(self, stock, request_index, request_data):
        """Initialize a request with the stock name and request number."""
        self.stock = stock
        self.request_index = request_index
        self.request_data = request_data

    def __getitem__(self, rhs: int) -> int:
        """Adds the ability to use subscription with Request objects."""
        reference_list: list = [self.stock, self.request_index, self.request_data]
        int_result = reference_list[rhs]
        return int_result
    
    def __repr__(self) -> str:
        """Automagically converts a Request object to a str."""
        return f"Request({self.stock}, {self.request_index})"




empty_request: Request = Request('', 0, pd.DataFrame())
request_list: list[Request] = [empty_request]


def data_finder(x):
    global request_index_list
    global request_index
    global stock
    global stocks
    global last_index
    global display_stock
    stock = x
    finnhub_client = finnhub.Client(api_key="c67jj0qad3iai8rb0ht0")
    data: dict = finnhub_client.quote(stock)

    stocks.append(stock)
    data = key_rename(data)
    print(f"Stocks in My List: {stocks}")
    print(f"Market information for {stocks[-1]}: {data}")

    df = pd.DataFrame(data, index = [0])
    print(df)
    df.to_html('templates/stock_table.html')

    request_list.pop(0)
    request_index_list.append(request_index)

    last_index = request_index_list[len(request_index_list) - 1]

    new_request: Request = Request(stock, request_index, df)

    request_list.append(new_request)

    # if new_request.request_index == 0:
    #     display_stock = request_list[0][0]
    # elif new_request.request_index == 1:
    #     display_stock = request_list[0][1]
    # elif new_request.request_index == 2:
    #     display_stock = request_list[0][2]
    # elif new_request.request_index == 3:
    #     display_stock = request_list[0][3]
    # else:
    #     display_stock = stocks[0][4]
    
    # print(display_stock)
    print(stocks)

    request_index += 1