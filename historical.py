# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:50 2016

@author: meemee
"""
import datetime
now = datetime.datetime.now()
past = now - datetime.timedelta(days = 60)
start = past.strftime("%Y-%m-%d")
end = now.strftime("%Y-%m-%d")

import pymongo
from textblob import TextBlob

client = pymongo.MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
histo = db['hist_rec']
new = db['news_rec']

def splitdate(date):
    date_ = date.split('-')
    y_ = date_[0]
    m_ = date_[1]
    d_ = date_[2]
    yyyy = int(y_)
    mm = int(m_)
    dd = int(d_)
    date_final = datetime.datetime(yyyy, mm, dd, 0, 0)
    return date_final
    
    
def query(company, start, end):
    comp_hist = []
    ccode = str(company)
    date_s = splitdate(start)
    date_e = splitdate(end)
    
    for item in histo.find({"date": {'$gte': date_s, '$lte': date_e}, "asx_code": ccode}).sort([
        ("date", pymongo.ASCENDING)
        ]):
        close = item.get('price').get('close')
        opening = item.get('price').get('open')
        low = item.get('price').get('low')
        high = item.get('price').get('high')
        datet = str(item.get('date'))
        dsplit = datet.split(' ')
        date = dsplit[0]
     
        parsep = {
            "date": date,
            "close": float(close),
            "open":float(opening),
            "low": float(low),
            "high": float(high)
            }
        comp_hist.append(parsep)
    return comp_hist
    
def news_search(company, data):
    news_data = []
    ccode = str(company)
    for item in data:
        date_d = item.get("date")
        date_n = splitdate(date_d)
        news = []
        for listing in new.find({"Date": date_n, "ASX code": ccode}).sort([
                             ("date", pymongo.ASCENDING)
                             ]):
                                url = listing.get("URL")
                                title = listing.get("Title")
                                body = listing.get("Body")
                                blob = TextBlob(body)
                                polar = blob.sentiment.polarity
                                sent = round(polar, 2)
                                article = {"url": url, "title": title, "body": body, "sentiment":sent}
                                news.append(article)

        news_ = {
              "articles": news,
              "article_status": len(news),
              "close" : item.get('close'),
              "open" : item.get('open'),
              "high" : item.get('high'),
              "low" : item.get('low'),
              "date" : date_d
              }
        news_data.append(news_)
    return news_data
    
def query_compare(company, competitors):
    c1_close = query(company, start, end)
    c2 = str(competitors[0])
    c2_close = query(c2, start, end)
    c3 = str(competitors[3])
    c3_close = query(c3, start, end)
    c4= str(competitors[6])
    c4_close = query(c4, start, end)

    ca = []
    cb = []
    cc = []
    cd = []
    date = []
    comparison = []

    for item in c1_close[:40]:
        close1 = item.get('close')
        dates = item.get('date')
        ca.append(close1)
        date.append(dates)
    for item in c2_close[:40]:
        close2 = item.get('close')
        cb.append(close2)
    for item in c3_close[:40]:
        close3 = item.get('close')
        cc.append(close3)
    for item in c4_close[:40]:
        close4 = item.get('close')
        cd.append(close4)

        
    for x in range(0,29):
        parsep = {
            "date": str(date[x]),
            "a": float(ca[x]),
            "b":float(cb[x]),
            "c":float(cc[x]),
            "d":float(cd[x])
        }
        x += 1
        comparison.append(parsep)
        
    return comparison
    
        
        
            
    
    

            
    
        
    
    
    
    
