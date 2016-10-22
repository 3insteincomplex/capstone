# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""
from historical import query
from latest import latest_prices
from flask import Flask

app = Flask(__name__)


@app.route('/get_latest/<string:company_code>')
def get_price(company_code):
    late = latest_prices(company_code)
    for item in late:
        print (item)
    return ("done")

@app.route('/get_history/<string:company_code>+date=<string:s_y>-<string:s_m>-<string:s_d>to<string:e_y>-<string:e_m>-<string:e_d>')
def get_hist(company_code, y_s, m_s, d_s, y_e, m_e, d_e):
    qu = query(company_code, y_s, m_s, d_s, y_e, m_e, d_e)
    print (qu)
    return ("done")


if __name__ == "__main__":
    app.run(debug = True)