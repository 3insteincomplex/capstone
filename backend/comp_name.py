from pymongo import MongoClient
import re
client = MongoClient('mongodb://admin1:admin1@ds019766.mlab.com:19766/heroku_51vsxq80')
db = client.get_default_database()
comcode = db['asxcode']

def search(company):
    test = str(company)
    tst = ('.*'+test+'.*').upper()
    histor = comcode.find_one({"$or":[ {"ASX code": company}, {"Company name":{'$in': [ re.compile(tst)]}}]})
    compname = histor.get('ASX code')
    return compname