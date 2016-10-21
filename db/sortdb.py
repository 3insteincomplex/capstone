# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:06:07 2016

@author: meemee
"""
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://admin1:admin1@ds019766.mlab.com:19766/heroku_51vsxq80')
db = client.get_default_database()
histo = db['hist_rec']

for doc in histo.find().sort([
        ("year", pymongo.DESCENDING),
        ("month", pymongo.DESCENDING),
        ("day", pymongo.DESCENDING)
        ]):
    print(doc)