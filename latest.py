# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:35:26 2016

@author: meemee
"""

import ystockquote as ysq

def format_currency(value):
    return "{0:,}".format(value)

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
        "Price" : price,
        "Change from Previous Price" : change,
        "Market Cap" : marketcap,
        "Earnings Per Share" : float(eps),
        "Price-Earnings Growth Ratio" : float(pegr),
        "Price-Earnings Ratio" : float(per),
        "Price-Sales Ratio" : float(psr),
        "Yearly High" : year_hi,
        "Yearly Low" : year_lo,
        "Fifty-Day Moving Average" : fdmv,
        "Two Hundred-Day Moving Average" : thdmv,
        "Volume" : format_currency(vol),
        "Volume (Avg)" : format_currency(vol_avg)
        }
    return latest 
    
     