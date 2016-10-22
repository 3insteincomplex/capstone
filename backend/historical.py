# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:50 2016

@author: meemee
"""
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://admin1:admin1@ds019766.mlab.com:19766/heroku_51vsxq80')
db = client.get_default_database()
histo = db['hist_rec']
    
def query(company_code, y_s, m_s, d_s, y_e, m_e, d_e):
    ccode = str(company_code + ".AX")
    syyyy = int(y_s)
    smm = int(m_s)
    sdd = int(d_s)
    eyyyy = int(y_e)
    emm = int(m_e)
    edd = int(d_e)
    date_s = datetime.datetime(syyyy, smm, sdd, 0, 0)
    date_e = datetime.datetime(eyyyy, emm, edd, 0, 0)
    his = histo.find_one({"date": {'$gte': date_s, '$lt': date_e}, "asx_code": ccode})
   
    comp_hist = []
    for item in his:
        date = str(his.get('date'))
        dsplit = date.split('-')
        ysplit = dsplit[0].split("0")
        yy = ysplit[1]
        mm = dsplit[1]
        day = dsplit[2].split(' ')
        dd = day[0]

        close = his.get('price').get('close')
        opening = his.get('price').get('open')
        low = his.get('price').get('low')
        high = his.get('price').get('high')
        adj_close = his.get('price').get('adj_close')

        parsep = {
            "month": int(mm),
            "day": int(dd),
            "year": int(yy),
            "close": float(close),
            "open":float(opening),
            "low": float(low),
            "high": float(high),
            "adj": float(adj_close)
        }
    comp_hist.append(parsep)
    return comp_hist
    
def graph(data):
    close = []
    date = []
    for item in data:
        closep = item['close']
        mm = item['month']
        yy = item['year']
        m = str(mm)
        y = str(yy)
        my = m + "/" +y
        close.append(closep)
        date.append(my)
    return close, date