# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""
from historical import query
from latest import latest_prices
from comp_name import search
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('home copy.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/output/', methods=['POST'])
def hello():
    fromdate=request.form['fromdate']
    todate=request.form['todate']
    keyword=request.form['keyword']
    print ({
        "fromdate": fromdate,
        "todate": todate,
        "keyword": keyword
    })

@app.route('/<string:company>+from=<string:y_s>-<string:m_s>-<string:d_s>&<string:y_e>-<string:m_e>-<string:d_e>')
@app.route('/index/<string:company>+from=<string:y_s>-<string:m_s>-<string:d_s>&<string:y_e>-<string:m_e>-<string:d_e>')
def get_price(company,y_s, m_s, d_s, y_e, m_e, d_e):
    asx = search(company)
    cn = str(asx[1] + " ")
    ind = str(asx[2])
    cc = str(asx[0])
    late = latest_prices(cc)
    date_s = str(y_s + "-" + m_s + "-" + d_s)
    date_e = str(y_e + "-" + m_e + "-" + d_e)
    qu = query(cc, y_s, m_s, d_s, y_e, m_e, d_e)
    return render_template('news.html', cc=cc, cn=cn, ind=ind, late=late, qu=qu,date_s = date_s,date_e = date_e)

if __name__ == "__main__":
    app.run(debug = True)