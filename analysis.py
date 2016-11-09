#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:17:35 2016

@author: meemee
"""
from math import sqrt

def avg(data):
    mean = float(sum(data)) / max(len(data), 1)
    return mean

def market_sentiment(data):
    marks = []
    highs = []
    lows = []
    closes = []
    dates = []
    increases = 0
    decreases = 0
    stdevs = []
    
    days = len(data)
    start = data[0]
    end = data[-1]
    if start.get("close") < end.get("close"):
        sentiment = "Bullish"
        description = "increased"
    else:
        sentiment = "Bearish"
        description = "decreased"
    
    change = end.get("close") - start.get("close")
    changeper= (change/start.get("close"))*100
    for item in data:
        hi = item.get("high")
        lo = item.get("low")
        close = item.get("close")
        date = item.get("date")
        highs.append(hi)
        lows.append(lo)
        closes.append(close)
        dates.append(date)
    
    peak = max(highs)
    trough = min(lows)
    best = max(closes)
    worst = min(closes)    
    
    peakdate = dates[highs.index(peak)]
    troughdate = dates[lows.index(trough)]
    bestdate = dates[closes.index(best)]
    worstdate = dates[closes.index(worst)]
    
    mean = avg(closes)

    for i in range(0, len(closes)-1):
        if closes[i] < closes[i+1]:
            increases += 1
        else:
            decreases += 1
        deviation = closes[i] - mean
        sqdev = pow(deviation,2)
        stdevs.append(sqdev)
        
    
    vol = sqrt(avg(stdevs))     
    marks.extend([days, sentiment, description, round(change,2), round(changeper,2), round(vol,2)*10, round(mean,2), peak, trough, best, worst, peakdate, troughdate, bestdate, worstdate, increases, decreases])
    return marks

