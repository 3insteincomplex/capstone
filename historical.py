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

client = pymongo.MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
histo = db['hist_rec']
    
def query(company, start, end):
    comp_hist = []
    ccode = str(company)
    date_s = start.split('-')
    y_s = date_s[0]
    m_s = date_s[1]
    d_s = date_s[2]
    date_e = end.split('-')
    y_e = date_e[0]
    m_e = date_e[1]
    d_e = date_e[2]
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

def query_compare(company, competitors):
    c1_close = query(company, start, end)
    c2 = str(competitors[0])
    c2_close = query(c2, start, end)
    c3 = str(competitors[2])
    c3_close = query(c3, start, end)
    c4= str(competitors[4])
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
        print(parsep)
        
    return comparison
        
    
    
    
    
