from pymongo import MongoClient
import re
client = MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
comcode = db['asxcode']

def search(company):
    test = str(company)
    tst = ('.*'+test+'.*').upper()
    histor = comcode.find_one({"$or":[ {"ASX code": company}, {"Company name":{'$in': [ re.compile(tst)]}}]})
    comp_inf =  []
    comp_inf.extend([])
    compasx = histor.get('ASX code')
    compname = histor.get('Company name')
    compsec = histor.get('Sector')
    compmark = histor.get('Market Cap')
    compweight = histor.get('Weight')
    comp_inf.extend([compasx, compname, compsec, compmark, compweight])
    return comp_inf
    
def sector_comp(company):
    seccomp = comcode.find({"ASX code": company})
    sector = seccomp.get("Sector")

