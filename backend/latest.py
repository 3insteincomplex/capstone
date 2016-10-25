# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:26 2016

@author: meemee
"""

import ystockquote as ysq

def latest_prices(company):
    ccode = str(company + ".AX")
    compdata = ysq.get_all(ccode)
    price = compdata.get('price')
    change = compdata.get('change')
    marketcap = compdata.get('market_cap')
    eps = compdata.get('earnings_per_share')
    pegr = compdata.get('price_earnings_growth_ratio')
    per = compdata.get('price_earnings_ratio')
    psr = compdata.get('price_sales_ratio')
    year_hi = compdata.get('fifty_two_week_high')
    year_lo = compdata.get('fifty_two_week_low')
    fdmv = compdata.get('fifty_day_moving_avg')
    thdmv = compdata.get('two_hundred_day_moving_avg')
    vol = compdata.get('volume')
    vol_avg = compdata.get('avg_daily_volume')

    latest = {
        "Price" : price,
        "Change from Previous Price" : change,
        "Market Cap" : marketcap,
        "Earnings Per Share" : eps,
        "Price-Earnings Growth Ratio" : pegr,
        "Price-Earnings Ratio" : per,
        "Price-Sales Ratio" : psr,
        "Yearly High" : year_hi,
        "Yearly Low" : year_lo,
        "Fifty-Day Moving Average" : fdmv,
        "Two Hundred-Day Moving Average" : thdmv,
        "Volume" : vol,
        "Volume (Avg)" : vol_avg
        }
    return latest 
    
     