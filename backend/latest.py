# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:26 2016

@author: meemee
"""

import ystockquote as ysq

def latest_prices(company):
    ccode = str(company + ".AX")
    latest = []
    
    close = ysq.get_price(ccode)
    change = ysq.get_change(ccode)
    year_hi = ysq.get_52_week_high(ccode)
    year_lo = ysq.get_52_week_low(ccode)
    vol = ysq.get_volume(ccode)
    vol_avg = ysq.get_avg_daily_volume(ccode)
       
    latest.extend([close,change,year_hi,year_lo,vol,vol_avg])    
    
    return latest 
    
     