# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:36:05 2016

@author: meemee
"""
from eventregistry import *

er = EventRegistry()

def get_news(company, start, end):
    obamaUri = er.getConceptUri("Obama")

    q = GetCounts([obamaUri])
    ret = er.execQuery(q)
    print(er.format(ret))

# return the same data but only for a small date range
    q.setDateRange("2015-05-15", "2015-05-20")
    ret = er.execQuery(q)
    print(er.format(ret))

# get the sentiment expressed about Obama
    q = GetCounts(obamaUri, source="sentiment")
    ret = er.execQuery(q)