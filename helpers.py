"""Generates tables of data for each stock in My List."""
 
 
from tabulate import tabulate
 
# Reassign the data's keys to be the full names for the table's column names
key_list: list[str] = ['current_price', 'change', 'percent_change', 'high_day_price', 'low_day_price', 'open_day_price', 'previous_close_price']
test_data = {'c':1, 'd':2, 'dp':3, 'h':4, 'l':5, 'o':6, 'pc': 7}
 
 
# def key_rename(input_data: dict, key_list: list[str]) -> dict:
#     """Reassign the data's keys to be the full names for the table's column names"""
#     key_list: list[str] = ["Current Price", "Change", "% Change", "High", "Low", "Open", "Close"]

#     result = {}
#     for key in input_data:
#         for i in key_list:
#             result[i] = input_data[key]

#     return result


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