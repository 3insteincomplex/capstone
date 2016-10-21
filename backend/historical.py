# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:50 2016

@author: meemee
"""

import ystockquote as ysq
import json
import datetime
class mydict(dict):
    def __str__(self):
        return json.dumps(self)

now = datetime.datetime.now()
endm = now.strftime("%b")
endd = now.day
endy = now.year
past = now - datetime.timedelta(days = 2*365)
startm = past.strftime("b")
startd = past.day
starty = past.year



def historical_prices(company_code, date_start, date_end):
    ccode = str(company_code)
    dstart = str(date_start)
    dend = str(date_end)
    hist = ysq.get_historical_prices(ccode, dstart, dend)
    
    historical = mydict(hist)
    return historical