import pymongo
import re
client = pymongo.MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
comcode = db['asxcode']

def get_company(company):
    test = str(company)
    tst = ('.*'+test+'.*')
    comp_inf =  []
    histor = comcode.find_one({"$or":[ {"ASX code":{'$in': [ re.compile(tst, re.IGNORECASE)]}}, {"Company name":{'$in': [ re.compile(tst, re.IGNORECASE)]}}]})
    for item in histor:
        compasx = histor.get("ASX code", {})
        compname = histor.get("Company name", {})
        compsec = histor.get("Sector", {})
        compmark = histor.get("Market Cap", {})
        compweight = histor.get("Weight", {})
    comp_inf.extend([compasx, compname, compsec, compmark, compweight])
    return comp_inf
    
def compare(sec):
    competitors=[]
    for item in comcode.find({"Sector": sec}).sort([
        ("Market Cap", pymongo.DESCENDING)
        ])[:3]:
        code = item.get('ASX code')
        marketc = item.get('Market Cap')
        name = item.get('Company name')
        competitors.extend([code, name, marketc])
    return competitors
    



