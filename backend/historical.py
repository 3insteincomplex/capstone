# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:50 2016

@author: meemee
"""
import datetime
from pymongo import MongoClient
import pymongo

client = MongoClient('mongodb://admin1:admin1@ds019766.mlab.com:19766/heroku_51vsxq80')
db = client.get_default_database()
histo = db['hist_rec']
    
def query(company, y_s, m_s, d_s, y_e, m_e, d_e):
    comp_hist = []
    ccode = str(company + ".AX")
    syyyy = int(y_s)
    smm = int(m_s)
    sdd = int(d_s)
    eyyyy = int(y_e)
    emm = int(m_e)
    edd = int(d_e)
    date_s = datetime.datetime(syyyy, smm, sdd, 0, 0)
    date_e = datetime.datetime(eyyyy, emm, edd, 0, 0)
   
    for item in histo.find({"date": {'$gte': date_s, '$lte': date_e}, "asx_code": ccode}).sort([
        ("date", pymongo.ASCENDING)
        ]):
        datet = str(item.get('date'))
        dsplit = datet.split(' ')
        date = dsplit[0]
        close = item.get('price').get('close')
        opening = item.get('price').get('open')
        low = item.get('price').get('low')
        high = item.get('price').get('high')

        parsep = {
            "date": date,
            "close": float(close),
            "open":float(opening),
            "low": float(low),
            "high": float(high)
        }
        comp_hist.append(parsep)
    return comp_hist