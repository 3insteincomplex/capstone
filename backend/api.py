# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""

from historical import historical_prices
from latest import latest_prices


from flask import Flask
app = Flask(__name__)

@app.route('/get_latest/<string:company_code>')
def get_price(company_code):
    late = latest_prices(company_code)
    for item in late:
        print (item)
    return ("done")


@app.route('/get_history/<string:company_code>''+date=''<string:date_start>''&''<string:date_end>')
def get_hist(company_code, date_start, date_end):
    hist = historical_prices(company_code, date_start, date_end)
    print (hist)
    return ("done")


if __name__ == "__main__":
    app.run(debug = True)