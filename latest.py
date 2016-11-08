# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:26 2016

@author: meemee
"""

import ystockquote as ysq

def format_currency(value):
    return "{0:,}".format(value)
    
def replace(value):
    if value != "N/A":
        return value
    else:
        return "0.0"
    
def latest_prices(company):
    ccode = str(company)
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
    vol = int(compdata.get('volume'))
    vol_avg = int(compdata.get('avg_daily_volume'))

    latest = {
        "Price" : replace(price),
        "Change from Previous Price" : replace(change),
        "Market Cap" : replace(marketcap),
        "Earnings Per Share" : replace(eps),
        "Price-Earnings Growth Ratio" : replace(pegr),
        "Price-Earnings Ratio" : replace(per),
        "Price-Sales Ratio" : replace(psr),
        "Yearly High" : replace(year_hi),
        "Yearly Low" : replace(year_lo),
        "Fifty-Day Moving Average" : replace(fdmv),
        "Two Hundred-Day Moving Average" : replace(thdmv),
        "Volume" : replace(format_currency(vol)),
        "Volume (Avg)" : replace(format_currency(vol_avg))
        }

    return latest 
    
     