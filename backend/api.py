# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""
from historical import query
from latest import latest_prices
from comp_name import search
from flask import Flask

app = Flask(__name__)


@app.route('/get_latest/<string:company>')
def get_price(company):
    cc = search(company)
    late = latest_prices(cc)
    for item in late:
        print(item)
    return "done"

@app.route('/get_history/<string:company>+date=<string:y_s>-<string:m_s>-<string:d_s>to<string:y_e>-<string:m_e>-<string:d_e>')
def get_hist(company, y_s, m_s, d_s, y_e, m_e, d_e):
    cc = search(company)
    qu = query(cc, y_s, m_s, d_s, y_e, m_e, d_e)
    print(str(qu))
    return "done"


if __name__ == "__main__":
    app.run(debug = True)