# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""
from historical import query
from latest import latest_prices
from comp_name import search
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

   
@app.route('/', methods = ['POST', 'GET'])
def lookup():
    query = {}
    if request.method == 'POST':
        fromdate=request.form['fromdate']
        todate=request.form['todate']
        keyword=request.form['keyword']
        query = {'fromdate': fromdate, 'todate': todate, 'keyword': keyword}
        start = query.get('fromdate')
        end = query.get('todate')
        company = query.get('keyword')     
        return redirect(url_for('get_price', start=start, end = end, company=company))
    return render_template('home.html')

@app.route('/<string:company>+from<string:start>to<string:end>')
def get_price(company,start,end):
    asx = search(company)
    cc = str(asx[0])
    cn = str(asx[1] + " ")
    sec = str(asx[2])
    markc = str(asx[3])
    weight = float(asx[4])
    late = latest_prices(cc)
    qu = query(cc, start, end)
    return render_template('news.html', cc=cc, cn=cn, sec=sec, markc=markc, weight=weight, late=late, qu=qu, start=start, end = end)

if __name__ == "__main__":
    app.run(debug = True)
