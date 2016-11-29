# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""
from historical import query, query_compare, news_search, news_ratio
from latest import latest_prices, get_asx
from search import get_company, compare, asxlist
from analysis import market_sentiment
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def lookup():
    asxl = asxlist()
    if request.method == 'POST':
        start =request.form['from-date']
        end = request.form['to-date']
        company =request.form['keyword']
        return redirect(url_for('get_price', start=start, end=end, company=company))
    return render_template('home.html',  asxl=asxl)

@app.route('/<string:company>+from=<string:start>to=<string:end>')
def get_price(company,start,end):
    asxl = asxlist()
    try:
        asx = get_company(company)
        cc = str(asx[0])
        sec = str(asx[2])
        late = latest_prices(cc)
        asxdata=get_asx()
        new_query = query(cc, start, end)
        news = news_search(cc, new_query)
        ratio = news_ratio(news)
        market = market_sentiment(new_query)
        competitors = compare(sec)
        comparison = query_compare(cc, competitors)

        return render_template('index.html', asx=asx,ratio=ratio, asxdata=asxdata, asxl=asxl, comparison=comparison, market=market,
                               late=late, new_query=new_query,competitors=competitors, news=news)
    except:
       errors = "No results found for the selected date range/company name. Please try again."                
       return render_template('home.html', errors=errors, asxl=asxl)
      
@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    errors = "No results found for the selected date range/company name. Please try again."                
    return render_template('home.html', errors=errors), 500

@app.errorhandler(404)
def page_not_found_error(exception):
    app.logger.error(exception)
    errors = "Please enter a date range and company name."                
    return render_template('home.html', errors=errors), 404

@app.errorhandler(400)
def bad_request(exception):
    app.logger.error(exception)
    errors = "Error processing request. Please try again."                
    return render_template('home.html', errors=errors), 400
    

if __name__ == "__main__":
    app.run(debug = True)
